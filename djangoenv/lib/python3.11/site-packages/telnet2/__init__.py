import telnetlib,socket
class telnet:
 def __init__(self):
  self.prompt=''
  self.prompt_end=b''
  self.telnet=None
  self.logs={}#where we save input and output logs
 def login(self,u,username=None,password=None,p=23,timeout=3):
  try:
   usr=False
   pwd=False
   self.telnet = telnetlib.Telnet(u,p,timeout=timeout)
   while True:
    m=self.telnet.expect([b'ser:',b'Name:',b'sername:',b'name:',b'ogin:',b'assword:',b'Pass:',b'pass:'],timeout=timeout)#expected login prompts
    s=m[2]
    if (('name:' in str(s).lower()) or ('login:' in str(s).lower()) or ('user:' in str(s).lower())):#in case it asked for username
     if usr==True:
        raise Exception("Authentication Failed")#so we don't tricked into sending username multiple times after failure
     self.telnet.write("{}\n".format(username).encode('utf-8'))#send username
     usr=True
    elif (("password:" in str(s).lower()) or ("pass:" in str(s).lower())):#in case it asked for password
     self.telnet.write("{}\n".format(password).encode('utf-8'))#send password
     pwd=True
     break
    else:
      c=str(s).lower()
      c=c.replace("b'",'')
      c=c.replace("'",'')
      c=c.replace('b"','')
      c=c.replace('"','')
      c=c.strip()
      if ((c[-1:]=='$') or (c[-1:]=='#') or (c[-1:]=='%') or (c[-1:]=='>')):#in case this is unauthenticated server
       self.prompt=c.strip()
       if (c[-1:]=='$'):
           self.prompt_end=b'$'
       if (c[-1:]=='>'):
           self.prompt_end=b'>'
       if (c[-1:]=='#'):
           self.prompt_end=b'#'
       if (c[-1:]=='%'):
           self.prompt_end=b'%'
       return None
      break
   while True:
      c=str(self.telnet.read_some()).lower()#keep reading the data till get the login result
      c=c.replace("b'",'')
      c=c.replace("'",'')
      c=c.replace('b"','')
      c=c.replace('"','')
      c=c.strip()
      if (('denied' in c) or ('enter>' in c) or ('bad' in c) or ("incorrect" in c) or ('failed' in c) or ('wrong' in c) or ('invalid' in c) or ('name:' in c) or ('login:' in c) or ('user:' in c) or ('password:' in c) or  ('pass:' in c)):
          raise Exception("Authentication Failed")#if login failed
      if ((c[-1:]=='$') or (c[-1:]=='#') or (c[-1:]=='%') or (c[-1:]=='>')):#if a prompt was received
       self.prompt=c.strip()#we set the prompt and then next we set the end of the prompt
       if (c[-1:]=='$'):
           self.prompt_end=b'$'
       if (c[-1:]=='>'):
           self.prompt_end=b'>'
       if (c[-1:]=='#'):
           self.prompt_end=b'#'
       if (c[-1:]=='%'):
           self.prompt_end=b'%'
       return None
  except socket.timeout:
   raise Exception("Timed out")
 def execute(self,cmd,new_line='\n',timeout=5,more_timeout=2):#this function executes any command and returns the output
    if cmd.strip()!='':
     self.telnet.write("{} {}".format(cmd.strip(),new_line).encode('utf-8'))#send the command
     c=self.telnet.read_until(self.prompt_end,timeout=timeout)#read data until it receive the end of the prompt after executing the command
     if "---- More ----" in c:
         while True:
             self.telnet.write("\n".format(cmd.strip(),new_line).encode('utf-8'))
             o=self.telnet.read_until(b"---- More ----",timeout=more_timeout)
             c+=o
             if self.prompt_end in c:
                 break
     c=str(c)
     c=c.replace("b'",'')
     c=c.replace("'",'')
     c=c.replace('b"','')
     c=c.replace('"','')
     c=c.strip()
     c=c.split(cmd)[1]#remove the command sent from output
     c="\r\n".join(c.split('\r\n')[:-1])#remove the prompt from output
     self.logs.update({cmd.strip():c.strip()})#save the input and output into dict as logs
     return c.strip()
 def close(self):
     self.telnet.close()#close telnet connection
 def logout(self,timeout=1):
     self.execute("logout",timeout=timeout)#logout of the telnet session
 def exit(self,timeout=1):
     self.execute("exit",timeout=timeout)#exit the telnet session
