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
Error Code    | Description
------------- | -------------
400           | Bad Request
404           | Resource Not Found
405           | Method Not Allowed
422           | Not Processable
500           | Internal Server Error


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
        - 404 error will be thrown in case the specified page attribute has no results.    
    ```
    `{
      "current_page": 1,
      "number_of_plants": 12,
      "plants": [
        {
          "id": 9,
          "is_poisonous": true,
          "name": "Not Working",
          "primary_color": "Red",
          "scientific_name": "NAM"
        },
        {
          "id": 11,
          "is_poisonous": true,
          "name": "Not g",
          "primary_color": "Red",
          "scientific_name": "NA"
        },
        {
          "id": 15,
          "is_poisonous": true,
          "name": "ahmedm",
          "primary_color": "Red",
          "scientific_name": "meshref"
        },
        {
          "id": 16,
          "is_poisonous": true,
          "name": "NA",
          "primary_color": "Red",
          "scientific_name": "NA"
        },
        {
          "id": 17,
          "is_poisonous": true,
          "name": "Snake Plant",
          "primary_color": "Red",
          "scientific_name": "Snake"
        }
      ],
      "success": true
    }
    ```


