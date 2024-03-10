import sys
if  sys.version_info < (3,0):
    input=raw_input
from telnet2.__init__ import *
c=sys.argv
user=""
pwd=""
host=''
port=23
timeout=5
commands=[]
command_timeout=5
new_line="\n"
shell=False
usage="""

usage: telnet2 options

options:

--host: set a host to connect to
--port: (23 by default) set port
--timeout: (5 by default) set timeout
--username: set a username
--password: set a password
--add-command: a command to execute after login
-command-timeout: timeout for command execution
--set-newline: set a new line indecator("\\n" or "\\r\\n")
--shell: run shell commands after authentication

example:

telnet2 --host 127.0.0.1 --username root --password root --add-command "echo ala" --add-command "dir"

"""
i=0
while(i<(len(c))):
    x=c[i]
    if (x=="--help"):
        print(usage)
        sys.exit()
    if (x=="--host"):
        host=c[i+1]
        i+=1
    if (x=="--port"):
        port=int(c[i+1])
        i+=1
    if (x=="--timeout"):
        timeout=int(c[i+1])
        i+=1
    if (x=="--username"):
        user=c[i+1]
        i+=1
    if (x=="--shell"):
        shell=True
    if (x=="--password"):
        pwd=c[i+1]
        i+=1
    if (x=="--add-command"):
     commands.append(c[i+1])
     i+=1
    if (x=="--command-timeout"):
        command_timeout=c[i+1]
        i+=1
    if (x=="--set-newline"):
        command_timeout=c[i+1]
        i+=1
    i+=1 

t=telnet()
try:
 print("[*]Authenticating: {} ==> {} : {} ...".format(host,user,pwd))
 t.login(host,username=user,password=pwd,timeout=timeout,p=port)
 print("[+]Logged in!!!")
 if len(commands)>0:
  for x in commands:
     print("[*]Command: "+str(x))
     print("[i]Output: "+str(t.execute(x,timeout=command_timeout,new_line=new_line)))
 if shell==True:
  while True:
      cmd=input(t.prompt)
      output=t.execute(cmd,timeout=command_timeout,new_line=new_line)
      if output==None:
        output=''
      print(output)
 t.close()
except Exception as e:
     print("[-]Error: "+str(e))
