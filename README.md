# Cat Picture API Design Document

## Introduction


The Cat Picture API is a RESTful web service designed to manage and serve cat pictures. It allows users to upload, delete, update, and fetch cat pictures via HTTP requests. This document outlines the design, functionality, and usage of the Cat Picture API.

### API Overview

  The Cat Picture API supports the following operations:

  ``` 
  Upload a cat picture.
  Delete a cat picture.
  Update a previously uploaded cat picture.
  Fetch a particular cat picture by its ID.
  Fetch a list of uploaded cat pictures.

```
## Stepup

#### Create a virtual environment  

```
python -m venv apienv
```
activate virtual environment

``` 
source apienv/bin/activate

```
```
git clone git@github.com:balapavankumar333/image_rest_api.git
```
```
pip install requirements.txt
```
DB Migrations
```
python manage.py makemigartions
python manage.py migrate
```

Sample test Cases

```
python manage.py test
```


### API Endpoints

The API provides the following endpoints:

Upload a Cat Picture
```
URL: /api/cat-pictures/
Method: POST
Description: Uploads a new cat picture to the server.
Request Body:
Form data containing the cat picture file.
HTTP Status Code 201 Created on success.
```




Delete a Cat Picture
```
URL: /api/cat-pictures/{id}/
Method: DELETE
Description: Deletes the cat picture with the specified ID from the server.
Response:
HTTP Status Code 204 No Content on success.
HTTP Status Code 404 Not Found if the cat picture does not exist.
```

Update a Cat Picture
```
URL: /api/cat-pictures/{id}/
Method: PUT, PATCH
Description: Updates the cat picture with the specified ID on the server.
Request Body:
Form data containing the updated cat picture file.
Response:
HTTP Status Code 200 OK on success.
```
Fetch a Cat Picture by ID
```
URL: /api/cat-pictures/{id}/
Method: GET
Description: Retrieves the cat picture with the specified ID from the server.
Response:
HTTP Status Code 200 OK on success.
Binary data of the cat picture file.
HTTP Status Code 404 Not Found if the cat picture does not exist.

```

Fetch List of Cat Pictures
```
URL: /api/cat-pictures/
Method: GET
Description: Retrieves a list of all uploaded cat pictures from the server.
Response:
HTTP Status Code 200 OK on success.
JSON array containing details of all uploaded cat pictures.
```

