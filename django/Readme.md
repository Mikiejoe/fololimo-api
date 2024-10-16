# FOLOLIMO API

This is a Django Rest Framework application for the FOLOLIMO API.

# Project Setup

1. ## Clone this repository

   ```
   git clone https://github.com/Mmust-Ihub/fololimo-api.git
   ```

2. ## Create a virtual environment
   ```
   python -m venv env
   env\Scripts\activate #for windows
   ```
3. ## Install dependencies
   ```
   pip install requirements.txt
   ```
4. ### Create a .env fle in the root of the project and add the following configurations

   ```
   DB_NAME =
   DB_PASSWORD =
   DB_HOST =
   DB_PORT = 5432
   DB_USER =
   ```

5. ### After installing the packages you run the following to create migrations for the database:

   ```
   python manage.py makemigrations
   ```

6. ### Run this to migrate the database:

   ```
   python manage.py migrate
   ```

7. ### After installing the packages you can now run:

   ```
   python manage.py runserver
   ```

#

<br>

# API DOCUMENTATION

> Root url: [https://fololimo-api-eight.vercel.app](https://fololimo-api-eight.vercel.app)

<br>
<br>

## Authentication

### Account Login

POST:/api/v1/users/login/

> Accept the following POST parameters: username, password Return the REST Framework Token Object's key.

> REQUEST BODY SCHEMA: **_application/json_**

```python
{
  "username": "string",
  "password": "string"
}
```

> Responses
>
> Status:201

```python
{
  "key":"token"
}
```

### Password Reset

POST:/api/v1/users/password/reset/

> Accepts the following POST parameters: email Returns the success/fail message.
>
> AUTHORIZATIONS:>**_Token_**
>
> REQUEST BODY SCHEMA: application/json

```python
{
  "email": "user@example.com"
}
```

> Response Samples
>
> Status:201
>
> RESPONSE SCHEMA: application/json

```python
{
  "email": "user@example.com"
}
```

POST:/api/v1/users/password/reset/confirm/

> Password reset e-mail link is confirmed, therefore this resets the user's password.
>
> Accepts the following POST parameters: token, uid, new_password1, new_password2 Returns the success/fail message.
>
> AUTHORIZATIONS>**_Token_**
>
> REQUEST BODY SCHEMA: application/json

```python
{
  "new_password1": "string",
  "new_password2": "string",
  "uid": "string",
  "token": "string"
}
```

> Reponse Samples
>
> Status:201
>
> RESPONSE SCHEMA: application/json

```python
{
  "new_password1": "string",
  "new_password2": "string",
  "uid": "string",
  "token": "string"
}
```

### Account Registration.

POST:/api/v1/users/register/
This is used when one wants to create an account.

> AUTHORIZATIONS: >**_Token_**
>
> REQUEST BODY SCHEMA: application/json

```python
{
  "username": "string",
  "email": "user@example.com",
  "password1": "string",
  "password2": "string"
}
```

> Response Samples
>
> Status:201
>
> RESPONSE SCHEMA: application/json

```python
{
  "username": "string",
  "email": "user@example.com",
  "password1": "string",
  "password2": "string"
}
```

#### Account Registration Email

POST:/api/v1/users//register/resend-email/
Account Register Resend Email

This is for requesting for the Email from the user.

> AUTHORIZATIONS:> **_Token_**
>
> REQUEST BODY SCHEMA: application/json

```python
{
  "email": "user@example.com"
}
```

> Response Samples
>
> Status:201
>
> RESPONSE SCHEMA: application/json

```python
{
  "email": "user@example.com"
}
```

Account Verify Email when Creating an Account

POST:/api/v1/users//register/verify-email/

> AUTHORIZATIONS:> **_Token_**
>
> REQUEST BODY SCHEMA: application/json

```python
{
  "key": "string"
}
```

> Response Samples
>
> Status:201
>
> RESPONSE SCHEMA: application/json

```python
{
  "key": "string"
}
```

Get user details

POST:/api/v1/users/user/

> AUTHORIZATIONS:> **_Token_**
>
> REQUEST BODY SCHEMA: application/json

```python
{
  "key": "string"
}
```

> Response Samples
>
> Status:200
>
> RESPONSE SCHEMA: application/json

```python
{
  "username": "my username",
  "email": "email@host.com",
  "firstname":"my firstname",
  "lastname":"my lastname",

}
```
Get all details

POST:/api/v1/details/

> AUTHORIZATIONS:> **_Token_**
>
> REQUEST BODY SCHEMA: application/json



> Response Samples
>
> Status:200
>
> RESPONSE SCHEMA: application/json

```python
{
  "weather": [
    {
      "id": 4,
      "temperature": 26.07,
      "description": "overcast clouds",
      "city": "Nakuru",
      "humidity": 39.0,
      "min_temp": 26.07,
      "max_temp": 26.07,
      "pressure": 1014.0
    },
    {
      "id": 26,
      "temperature": 25.16,
      "description": "light rain",
      "city": "Kakamega",
      "humidity": 56.0,
      "min_temp": 25.16,
      "max_temp": 25.16,
      "pressure": 1014.0
    }
  ],
  "profile": {
    "pk": 1,
    "username": "mike",
    "email": "mike@site.com"
  },
  "farms": [
    {
      "name": "My Farm",
      "location": "Nakuru East",
      "size": 26.0,
      "longitude": null,
      "latitude": null,
      "id": 24,
      "city": 7,
      "city_name": "Nakuru"
    },
    {
      "name": "Farm mike",
      "location": "Lurambi",
      "size": 1234.0,
      "longitude": null,
      "latitude": null,
      "id": 26,
      "city": 37,
      "city_name": "Kakamega"
    }
  ],
  "activities": []
}
```

## Farm

### Farm create

POST: /api/v1/insights/farms/

> Accept the following POST parameters: name,location,size,longitude,latitude Returns the created farm object.

> REQUEST BODY SCHEMA: **_application/json_**
> AUTHORIZATIONS:> **_Token_**

```python
{
  "name": "string",
  "location": "location",
  "size": float,
  "longitude":float,
  "latitude":float

}
```

> Responses
>
> Status:201

```python
{
  "name": "string",
  "location": "string",
  "size": float,
  "longitude":float,
  "latitude":float
  "id": int,
}
```

### Farms GET

GET: /api/v1/insights/farms/

> Returns a list of farms for the user making the request.

> REQUEST BODY SCHEMA: **_application/json_**
> AUTHORIZATIONS:> **_Token_**

> Responses
>
> Status:200

```python
[{
  "name": "string",
  "location": "string",
  "size": float,
  "longitude":float,
  "latitude":float
  "id": int,
},
{
  "name": "string",
  "location": "string",
  "size": float,
  "longitude":float,
  "latitude":float
  "id": int,
},....]
```

### Farm GET

GET: /api/v1/insights/farms/{id}

> Return the farm with the specified id.

> REQUEST BODY SCHEMA: **_application/json_**
> AUTHORIZATIONS:> **_Token_**

> Responses
>
> Status:200

```python

{
  "name": "string",
  "location": "string",
  "size": float,
  "longitude":float,
  "latitude":float
  "id": int,
}
```

## Locations

### Get Regions

> GET : https://fololimo-api-eight.vercel.app/api/v1/fololimo/regions/
> Return a list of all the regions.<br>
> REQUEST BODY SCHEMA: **_application/json_**<br>
> AUTHORIZATIONS:> **_Token_**

Response:

```
[
 {
   "id": 7,
   "region": "Central"
 },
 {
   "id": 8,
   "region": "Rift Valley"
 },
 {
   "id": 9,
   "region": "Eastern"
 },
 {
   "id": 10,
   "region": "Nyanza"
 },
 {
   "id": 11,
   "region": "Western"
 },
 {
   "id": 12,
   "region": "Coast"
 },
 {
   "id": 13,
   "region": "North Eastern"
 },
 {
   "id": 14,
   "region": "Nairobi"
 }
]
```

### Get Counties

> GET : https://fololimo-api-eight.vercel.app/api/v1/fololimo/cities/?region={id}<br>
> id is the id of the region.<br>
> Return a list of counties in a region.<br>
> REQUEST BODY SCHEMA: **_application/json_**<br>
> AUTHORIZATIONS:> **_Token_**

Example Request

```
https://fololimo-api-eight.vercel.app/api/v1/fololimo/cities/?region=12
```

Example Response

```
[
    {
        "id": 39,
        "city": "Kilifi",
        "region": 12
    },
    {
        "id": 40,
        "city": "Kwale",
        "region": 12
    },
    {
        "id": 41,
        "city": "Lamu",
        "region": 12
    },
    {
        "id": 42,
        "city": "Mombasa",
        "region": 12
    },
    {
        "id": 43,
        "city": "Taita-Taveta",
        "region": 12
    },
    {
        "id": 44,
        "city": "Tana River",
        "region": 12
    }
]
```

### GET Subcounties

> GET : https://fololimo-api-eight.vercel.app/api/v1/fololimo/subcounties/?city={id}<br>
> id is the id of the region.<br>
> Return a list of subcounties in a County.<br>
> REQUEST BODY SCHEMA: **_application/json_**<br>
> AUTHORIZATIONS:> **_Token_**

Example Request

```
https://fololimo-api-eight.vercel.app/api/v1/fololimo/subcouties/?city=12
```

Example Response

```
[
  {
    "id": 77,
    "sub_county": "Bomet Central",
    "city": 12
  },
  {
    "id": 78,
    "sub_county": "Bomet East",
    "city": 12
  },
  {
    "id": 79,
    "sub_county": "Chepalungu",
    "city": 12
  },
  {
    "id": 80,
    "sub_county": "Konoin",
    "city": 12
  },
  {
    "id": 81,
    "sub_county": "Sotik",
    "city": 12
  }
]
```

##Weather

### Get city's weather

> GET : https://fololimo-api-eight.vercel.app/api/v1/fololimo/weathers/{id}<br>
> id is the id of the city.<br>
> Return the weather condition for a city.<br>
> REQUEST BODY SCHEMA: **_application/json_**<br>
> AUTHORIZATIONS:> **_Token_**

example request

```
https://fololimo-api-eight.vercel.app/api/v1/fololimo/weathers/12/
```

Example response

```
{
  "id": 8,
  "temperature": 24.52,
  "description": "clear sky",
  "city": "Bomet",
  "humidity": 34.0,
  "min_temp": 24.52,
  "max_temp": 24.52,
  "pressure": 1015.0
}
```

## Activity

### POST Activity

POST: /api/v1/insights/activities/

> Accept the following POST parameters: activity, date, cost, duration, id, farm, status Returns the created farm object.

> REQUEST BODY SCHEMA: **_application/json_**
> AUTHORIZATIONS:> **_Token_**

Example Request

```
{
    "activity": "Planting",
    "date": "2024-10-25",
    "cost": 20000.0,
    "duration": 12,
    "farm": 1 #farm's id
  }
```

Example Response
<br>
status_code = 201

```
{
"activity": "Planting",
"date": "2024-10-25",
"cost": 20000.0,
"duration": 12,
"id": 1,
"status":"pending",
"farm": "Kariosh"
}
```

### GET Activities

GET: /api/v1/insights/activities/

> Returns list of activities for the requesting user object.<BR>
> REQUEST BODY SCHEMA: **_application/json_**<BR>
> AUTHORIZATIONS:> **_Token_**

Example Response<br>
>status_code = 200

```
[
  {
"activity": "Planting",
"date": "2024-10-25",
"cost": 20000.0,
"duration": 12,
"status":"pending",
"id": 1,
"farm": "Kariosh"
},
{
"activity": "Weeding",
"date": "2024-12-2",
"cost": 20000.0,
"duration": 12, # in days
"status":"pending",
"id": 2,
"farm": "My Farm"
}
]
```
### GET Activities

GET: /api/v1/insights/activities/{id}/

> Returns the activity with the specified name.<BR>
> REQUEST BODY SCHEMA: **_application/json_**<BR>
> AUTHORIZATIONS:> **_Token_**

Example Response
 /api/v1/insights/activities/2/<br>
 status_code = 200
```
{
"activity": "Weeding",
"date": "2024-12-2",
"cost": 20000.0,
"status":"pending",
"duration": 12, # in days
"id": 1,
"farm": "My Farm"
}
```