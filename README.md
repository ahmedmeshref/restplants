# REST plant
**Version 1.0.0**

A RESTful API which serves data about plants.


### Getting Started 
- Base URL: At the present, this API can only run locally and it is not hosted as a base URL. This backend is hosted 
at the default, `http://127.0.0.1:5000/`, which is set as a proxy in frontend configurations.

- Authentication: This version of the app doesn't require Authentication or API keys. 


### Errors Handling 
Rest plants returns errors as JSON objects in the following format:
``` 
    {
        'success': False,
        'error': 404,
        'message': 'Resource Not Found'
    }
```

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

#### GET All Plants
- Sample Request:
    
    `curl -X GET http://127.0.0.1:5000/plants`

- Attributes:

    - `Optional` Page: you can specific the desired results page in the request body as follows:
    
        `curl -X GET http://127.0.0.1:5000/plants?page={number}`
        
        `curl -X GET http://127.0.0.1:5000/plants?page=2`

        

- Sample Response: 
    - Notes: 
        - Number of plants to be returned per page is 5.
        - 404 error will be thrown in case page attribute is specified and no results match.    
    ```
    `{
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


#### GET Plant by ID
- Sample Request:
    
    `curl -X GET http://127.0.0.1:5000/plants/{number}`
    
    `curl -X GET http://127.0.0.1:5000/plants/1}`
    
        

- Sample Response: 
    - Notes: 
        - 404 error will be thrown in case no plant with the given id.    
    ```
    `{
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


