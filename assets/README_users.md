# Introduction.
This documentation assumes the app is running on http://localhost:8000/ In production, you will be using your own domain, hopefully starting with https!

In development you can visit http://localhost:8000/ to see the browseable api, but most of it's functionality will be disabled in a production setting. If you don't find what you need in this README, try looking at the browseable api.

## User Auth.
This api uses token authentication. You get a token by using /api/login, and you send the token to other endpoints by including it in a header called "Authorization". The value of Authorization should be the word "token", followed by a space, followed by the actual token.

If you do *not* include an Authorization header, then the user sending the request is considered anonymous.

### Login example using JS fetch.
#### Request
**Body**
username (string)
password (string)

```javascript
fetch('http://localhost:8000/api/login', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        username: 'Aaron Price',
        password: 'x*x*x*x*x*x*x*',
    })
})
```
#### Response
```javascript
{
    "token": "fb582c80c8bbe709399bac5608c570381d45171a",
    "id": 6,
    "name": "Aaron Price",
    "is_staff": false,
    "is_superuser": false,
    "is_active": true
}
```

### Accessing a private endpoint using JS fetch.
#### Request
**Headers**
Authorization (string 'token xxxxxxxxx')

```javascript
fetch('http://localhost:8000/api/something_private', {
    method: 'GET',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'token fb582c80c8bbe709399bac5608c570381d45171a'
    }
})
```
#### Response
```javascript
{
    "private": "Only certain users can see this!"
}
```

## CRUD
By default, all models have endpoints representing the following:
- List of all instances
- Details about a specific instance
- Creating a new instance
- Updating an existing instance
- Deleting an existing instance

### List
GET http://localhost:8000/api/model_name/
Returns an array of objects.

#### Request
```javascript
fetch('http://localhost:8000/api/model_name/', { method: 'GET' })
```
#### Response
```javascript
[
    {
        id: 1,
        name: 'foo'
    },
    {
        id: 2,
        name: 'bar'
    },
]
```

### Details
GET http://localhost:8000/api/model_name/:id/
Returns an object.

#### Request
```javascript
fetch('http://localhost:8000/api/model_name/1', { method: 'GET' })
```
#### Response
```javascript
{
    id: 1,
    name: 'foo'
}
```

### Create
POST http://localhost:8000/api/model_name/
Creates a new instance

#### Request
**Headers**
Authorization (string 'token xxxxxxxxx')

**Body**
owner (number. Matches user id)
Any other model fields

```javascript
fetch('http://localhost:8000/api/model_name/', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'token fb582c80c8bbe709399bac5608c570381d45171a'
    },
    body: {
        'name': 'my new instance',
        'owner': 6
    }
})
```
#### Response
```javascript
{
    pk: 42,
    owner: 6,
    name: 'my new instance'
}
```

### Update
PUT http://localhost:8000/api/model_name/:id/
Updates an existing instance

#### Request
**Headers**
Authorization (string 'token xxxxxxxxx')

**Body**
owner (number. Matches user id)
Any other model fields

```javascript
fetch('http://localhost:8000/api/model_name/42/', {
    method: 'PUT',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'token fb582c80c8bbe709399bac5608c570381d45171a'
    },
    body: {
        'name': 'CHANGED name',
        'owner': 6
    }
})
```
#### Response
```javascript
{
    pk: 42,
    owner: 6,
    name: 'CHANGED name'
}
```

### Delete
DELETE http://localhost:8000/api/model_name/:id/
Deletes an existing instance

#### Request
**Headers**
Authorization (string 'token xxxxxxxxx')

```javascript
fetch('http://localhost:8000/api/model_name/42/', {
    method: 'PUT',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'token fb582c80c8bbe709399bac5608c570381d45171a'
    }
})
```
#### Response
```javascript
{
    pk: 42,
    owner: 6,
    name: 'CHANGED name'
}
```
