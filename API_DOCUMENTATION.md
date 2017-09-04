# Users
assuming users are needed in the first place, the following endpoints are exposed:

## Authentication
Send a header called "Authorization" with a value of "token" then a space, then your token.
For example

`headers: { "Authorization": "token 1234567890abcdefghijklmnopqrstuvwxyz" }`

If the token authenticates properly, you will have a permission level of Authenticated by default.

To acquire a token, send a POST request to /api/login

## www.url.com/api/login
Allowed methods: "POST", "OPTIONS"

#### POST
Description: Gets an authentication token for the user.
Permission required: Anonymous

Request body must contain the following fields:
- username
- password

Response body will contain the following field:
- token

## www.url.com/api/profile
Allowed methods: "GET", "POST", "HEAD", "OPTIONS"

#### GET
Description: Lists the existing users
Permission required: Authenticated

Response body contains an array of User objects, all with id, email, and name fields.

#### POST
Description: Creates a new user
Permission required: Anonymous

Request body must contain the following fields:
- name
- email
- password
