# Introduction.
This documentation assumes the app is running on http://localhost:8000/ In production, you will be using your own domain, hopefully starting with https!

In development you can visit http://localhost:8000/ to see the browseable api, but most of it's functionality will be disabled in a production setting. If you don't find what you need in this README, try looking at the browseable api.

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
**Body**
Any other model fields

```javascript
fetch('http://localhost:8000/api/model_name/', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
    body: {
        'name': 'my new instance',
    }
})
```
#### Response
```javascript
{
    pk: 42,
    name: 'my new instance'
}
```

### Update
PUT http://localhost:8000/api/model_name/:id/
Updates an existing instance

#### Request
**Body**
All model fields

```javascript
fetch('http://localhost:8000/api/model_name/42/', {
    method: 'PUT',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: {
        'name': 'CHANGED name',
    }
})
```
#### Response
```javascript
{
    pk: 42,
    name: 'CHANGED name'
}
```

### Delete
DELETE http://localhost:8000/api/model_name/:id/
Deletes an existing instance

#### Request

```javascript
fetch('http://localhost:8000/api/model_name/42/', {
    method: 'PUT',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
})
```
#### Response
```javascript
{
    pk: 42,
    name: 'CHANGED name'
}
```
