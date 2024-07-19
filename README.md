### Request methods

| Method   | URL                                      | Description                              |
| -------- | ---------------------------------------- | ---------------------------------------- |
| `GET`    | `/api/facility/`                         | Retrieve all facilities.                 |
| `GET`    | `/api/review/?facility=\(facility.id!)`  | Retrieve reviews for facility by id.     |
| `GET`    | `/api/facility/\(id)/`                   | Retrieve specific facility by id.        |
| `POST`   | `/api/api-token-auth/`                   | Create a new api token.                  |
| `POST`   | `/api/facility/`                         | Create a new facility.                   |
| `POST`   | `/api/review/`                           | Create a new review.                     |
| `PUT`    | `/api/facility/\(id)/`                   | Update facility information by id.       |
| `DEL`    | `/api/facility/\(id)/`                   | Delete a facility by id.                 |

## Headers

| Header key        | Description                              |
| ----------------- | ---------------------------------------- |
| `Accept`          | `application/json`                       |
| `Authorization`   | `AGRO_AUTH_TOKEN`                        |


#### facility item

```
{
        "id": 97,
        "name": "Your Citys Maid LLC",
        "category": "Cleaning",
        "phone_number": "(347) 591-1111",
        "address": "Manhattan 1574",
        "email_address": "yourcitysmaid@email.com",
        "lat": 40.7209,
        "lon": -74.0007,
        "reviews": [
            {
                "facility": 97,
                "title": "Great Service!",
                "body": "On time, efficient, and left my place spotless",
                "time": "1712025691",
                "stars": 5,
                "email": "jonathannunez@email-com",
                "user": "Jona Nunez"
            }
        ]
}
```

#### Post review item

```
{
    "facility": 97,
    "title": "Great Service!",
    "body": "On time, efficient, and left my place spotless",
    "time": "1712025691",
    "stars": 5,
    "email": "jonathannunez@email-com",
    "user": "Jona Punez"
}
```


#### Only 1 user review item

```
{
    "non_field_errors": [
        "The fields facility, user must make a unique set."
    ]
}
