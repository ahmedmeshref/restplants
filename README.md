# REST plant
**Version 1.0.0**

A RESTful API which serves data about plants.


### Getting Started 

- Base URL: At the present, this API can only run locally and it is not hosted as a base URL. This backend is hosted 
at the default, `http://127.0.0.1:5000/`, which is set as a proxy in frontend configurations.

- Authentication: This version of the app doesn't require Authentication or API keys. 


### Errors Handling 

Rest plants returns errors as JSON objects in the following format:
    
    {
        'success': False,
        'error': 404,
        'message': 'Resource Not Found'
    }


#### Overview:

In general, the error codes that indicate failure of the API request are: 
- Codes in range `4xx` indicate the failure of the request. These errors can be programmatically corrected. You can get
more information about these errors, from the API response body attributes such as message, to fix them.
- Codes in range `5xx` indicate the failure of the request due to internal server errors. Running your API request again
might solve these error.


#### Types of Errors:

| Error Code            | Code
| -------------         | ------------
| Bad Request           | 400 
| Resource Not Found    | 404 
| Method Not Allowed    | 405 
| Not Processable       | 422 
| Internal Server Error | 500 



### API Endpoints

Below are described the REST endpoints available.

#### Get All Plants
    
- Sample Request:
    
    `curl -X GET http://127.0.0.1:5000/plants`

- Attributes:

    - `Optional` Page: you can specific the desired results page in the request body as follows:
    
        `curl -X GET http://127.0.0.1:5000/plants?page={number}`
        
        `curl -X GET http://127.0.0.1:5000/plants?page=2`

- Response: 

    - Returns json object with a list of plant objects, current page, success value, and total number of books
    - Results are paginated in groups of 5. 
    
    ```
    {
      "current_page": 1,
      "number_of_plants": 12,
      "plants": [
        {
          "id": 1,
          "is_poisonous": true,
          "name": "Snake Plant",
          "primary_color": "Red",
          "scientific_name": "NA"
        },
        {
          "id": 2,
          "is_poisonous": false,
          "name": "Qat",
          "primary_color": "Green",
          "scientific_name": "Quaking Aspen Trees"
        },
        {
          "id": 3,
          "is_poisonous": true,
          "name": "Rcp",
          "primary_color": "Red",
          "scientific_name": "Red Charm Peony."
        },
        {
          "id": 4,
          "is_poisonous": false,
          "name": "NA",
          "primary_color": "red",
          "scientific_name": "Red Hot Poker Plant"
        },
        {
          "id": 5,
          "is_poisonous": true,
          "name": "Salvia",
          "primary_color": "Red",
          "scientific_name": "Red Salvia"
        }
      ],
      "success": true
    }
    ```


#### Get Plant by ID

- Sample Request:
    
    `curl -X GET http://127.0.0.1:5000/plants/{number}`
    
    `curl -X GET http://127.0.0.1:5000/plants/1}`
    
- Response: 

    - Returns json object with a list of selected plant object, and success value.
    
    ```
    {
      "plant": [
        {
          "id": 1,
          "is_poisonous": true,
          "name": "Snake Plant",
          "primary_color": "Red",
          "scientific_name": "NA"
        }
      ],
      "success": true
    }
    ```


####  Create New Plant
    
- Sample Request:
    
    `curl -X POST http://127.0.0.1:5000/plants -H "Content-Type: application/json" -d '{"name": "Red Masla", "scientific_name": "Red Masla", "is_poisonous": True, "primary_color": "Red"}'`        

- Response: 
    - Returns json object with a list of plant objects, success value, new_plant_id, current_page_number, and number_of_plants.
    
    ```
    {
      "current_page_number": 1,
      "new_plant_id": 28,
      "number_of_plants": 12,
      "plants": [
        {
          "id": 1,
          "is_poisonous": true,
          "name": "Snake Plant",
          "primary_color": "Red",
          "scientific_name": "NA"
        },
        {
          "id": 2,
          "is_poisonous": false,
          "name": "Qat",
          "primary_color": "Green",
          "scientific_name": "Quaking Aspen Trees"
        },
        {
          "id": 3,
          "is_poisonous": true,
          "name": "Rcp",
          "primary_color": "Red",
          "scientific_name": "Red Charm Peony."
        },
        {
          "id": 4,
          "is_poisonous": false,
          "name": "NA",
          "primary_color": "red",
          "scientific_name": "Red Hot Poker Plant"
        },
        {
          "id": 5,
          "is_poisonous": true,
          "name": "Salvia",
          "primary_color": "Red",
          "scientific_name": "Red Salvia"
        }
      ],
      "success": true
    }
    ```
    
    
####  Update Existing Plant
    
- Sample Request:

    `curl -X PATCH http://127.0.0.1:5000/plants/{id} -H "Content-Type: application/json" -d '{attribute: value, attribute: value, ...}'`      
    
    `curl -X PATCH http://127.0.0.1:5000/plants/1 -H "Content-Type: application/json" -d '{"primary_color": "Green"}'`        

- Response: 
    - Returns a json object with success value, and id of updated plant.
    
    ```
    {
      "id": 1,
      "success": true
    }
    ```
    
####  Delete Existing Plant
    
- Sample Request:

    `curl -X DELETE http://127.0.0.1:5000/plants/{id}`   
   
    `curl -X DELETE http://127.0.0.1:5000/plants/1`        

- Response: 
    - Returns json object with a list of remaining plant objects, success value, delete_plant_id, current_page_number, and number_of_plants.
    
    ```
    {
      "current_page_number": 1,
      "deleted_plant_id": 9,
      "number_of_plants": 11,
      "plants": [
        {
          "id": 1,
          "is_poisonous": true,
          "name": "Snake Plant",
          "primary_color": "Red",
          "scientific_name": "NA"
        },
        {
          "id": 2,
          "is_poisonous": false,
          "name": "Qat",
          "primary_color": "Green",
          "scientific_name": "Quaking Aspen Trees"
        },
        {
          "id": 3,
          "is_poisonous": true,
          "name": "Rcp",
          "primary_color": "Red",
          "scientific_name": "Red Charm Peony."
        },
        {
          "id": 4,
          "is_poisonous": false,
          "name": "NA",
          "primary_color": "red",
          "scientific_name": "Red Hot Poker Plant"
        },
        {
          "id": 5,
          "is_poisonous": true,
          "name": "Salvia",
          "primary_color": "Red",
          "scientific_name": "Red Salvia"
        }
      ],
      "success": true
    }
    ```
