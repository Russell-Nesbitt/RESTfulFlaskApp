This is a simple example of how to set up a fully RESTful API backend for a pip-integrated Flask App with multiple independent URL-accessed APIs. It includes examples for how to pass information both via the request bodies (parsed via the schemas in the schemas.py files) and in the request URLs themselves. Both APIs support GET, POST, PUT, PATCH, and DELETE operations, the intended use of which are explained in both this readme and in comments in the routes.py files. Currently, they all link to placeholder handler functions and just return a message indicating the successful transfer of data to the handler functions. Note that the two APIs have identical functionality, but have different URL paths and return messages to distinguish between them.

To Run:
Navigate to to .../RESTfulFlaskApp
IMPORTANT NOTE: All "pipenv run" prefixes can be removed if running commands in "pipenv shell" (RECOMMENDED)

If Fresh Pull - Only needs to be done ONCE
pipenv --python 3.12
pipenv install

To Run the App:
pipenv run python app.py
	- runs on port 8060 (Note that all examples below assume the use of this method)
OR (NOT RECOMMENDED)
pipenv run flask app
	- Make note of the port number given after "Running on..." on your terminal. It should be the last four digits, e.g. "8060"

To Access API Endpoints:
Open Postman or other API Testing Tool of Choice

If running via <pipenv run python app.py>:
http://127.0.0.1:8060/api/v1/<URL_Suffix_Here>
If running via <pipenv run flask app>:
http://127.0.0.1:<Your_Port_Number>/api/v1/<URL_Suffix_Here>


API One Endpoints:
Request Data in URL:
	Operation: GET
    Should Get a resource by providing the Unique ID in the Request URL
    Example:
    URL: http://127.0.0.1:8060/api/v1/apiOne/1/urlExample
    Body: {}

	Operation: DELETE
	  Should Delete a resource by providing the Unique ID in the Request URL
    Example:
    URL: http://127.0.0.1:8060/api/v1/apiOne/1/urlExample
    Body: {}

Request Data in Request Body:
  Operation: GET
    Should Get a resource by providing the Unique ID in the Request Body
    Example:
    URL: http://127.0.0.1:8060/api/v1/apiOne/example
    Body: {"val_id": 1}

	Operation: POST
	  Should create a new resource by providing the Fields in the Request Body
    Example:
    URL: http://127.0.0.1:8060/api/v1/apiOne/example
    Body: {"val_id": 1, "val_one": "str1", "val_two": "str2"}

	Operation: PUT
    Should modify an existing resource by sending ALL fields in the Request Body
    Any fields not included in the request are set to None
    Examples:
    URL: http://127.0.0.1:8060/api/v1/apiOne/example
    Body: {"val_id": 1} 
		  Sets val_one and val_two to None
    Body: {"val_id": 1, "val_one": "newStr1"} 
		  Changes val_one to newStr1, Sets val_two to None
    Body: {"val_id": 1, "val_two": "newStr2"} 
		  Changes val_two to newStr2, Sets val_one to None
    Body: {"val_id": 1, "val_one": "newStr1", "val_two": "newStr2"} 
		  Changes both val_one and val_two to respective new values

	Operation: PATCH
	  Should modify an existing resource by sending ONLY the fields which you want to change in the Request Body
    Examples:
    URL: http://127.0.0.1:8060/api/v1/apiOne/example
    Body: {"val_id": 1} 
		  Changes nothing
    Body: {"val_id": 1, "val_one": "newStr1"} 
		  Changes val_one to newStr1
    Body: {"val_id": 1, "val_two": "newStr2"} 
		  Changes val_two to newStr2
    Body: {"val_id": 1, "val_one": "newStr1", "val_two": "newStr2"} 
		  Changes both val_one and val_two to respective new values



API Two Endpoints:
Request Data in URL:
	Operation: GET
    Should Get a resource by providing the Unique ID in the Request URL
    Example:
    URL: http://127.0.0.1:8060/api/v1/apiTwo/1/urlExample
    Body: {}

	Operation: DELETE
	  Should Delete a resource by providing the Unique ID in the Request URL
    Example:
    URL: http://127.0.0.1:8060/api/v1/apiTwo/1/urlExample
    Body: {}

Request Data in Request Body:
  Operation: GET
    Should Get a resource by providing the Unique ID in the Request Body
    Example:
    URL: http://127.0.0.1:8060/api/v1/apiTwo/example
    Body: {"val_id": 1}

	Operation: POST
	  Should create a new resource by providing the Fields in the Request Body
    Example:
    URL: http://127.0.0.1:8060/api/v1/apiTwo/example
    Body: {"val_id": 1, "val_one": "str1", "val_two": "str2"}

	Operation: PUT
    Should modify an existing resource by sending ALL fields in the Request Body
    Any fields not included in the request are set to None
    Examples:
    URL: http://127.0.0.1:8060/api/v1/apiTwo/example
    Body: {"val_id": 1} 
		  Sets val_one and val_two to None
    Body: {"val_id": 1, "val_one": "newStr1"} 
		  Changes val_one to newStr1, Sets val_two to None
    Body: {"val_id": 1, "val_two": "newStr2"} 
		  Changes val_two to newStr2, Sets val_one to None
    Body: {"val_id": 1, "val_one": "newStr1", "val_two": "newStr2"} 
		  Changes both val_one and val_two to respective new values

	Operation: PATCH
	  Should modify an existing resource by sending ONLY the fields which you want to change in the Request Body
    Examples:
    URL: http://127.0.0.1:8060/api/v1/apiTwo/example
    Body: {"val_id": 1} 
		  Changes nothing
    Body: {"val_id": 1, "val_one": "newStr1"} 
		  Changes val_one to newStr1
    Body: {"val_id": 1, "val_two": "newStr2"} 
		  Changes val_two to newStr2
    Body: {"val_id": 1, "val_one": "newStr1", "val_two": "newStr2"} 
		  Changes both val_one and val_two to respective new values

