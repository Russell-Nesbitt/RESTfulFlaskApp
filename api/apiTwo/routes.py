from flask import request
from flask_restx import Resource

from api.apiTwo import api

from api.apiTwo.schemas import (full_schema, id_schema, partial_schema)

from api.apiTwo.handlers import (example_get, example_post, example_delete, example_put, example_patch)

@api.route("/<id_val>/urlExample")
class exampleAPIURL(Resource):
    #Should Get a resource by providing the Unique ID in the Request URL
    #Example
    #Operation: GET
    #URL: http://127.0.0.1:8060/api/v1/apiTwo/1/urlExample
    #Body: {}
    @api.response(400, "Validation Error")
    def get(self, id_val: int):
        return example_get(id_val), 200
    
    #Should Delete a resource by providing the Unique ID in the Request URL
    #Example
    #Operation: DELETE
    #URL: http://127.0.0.1:8060/api/v1/apiTwo/1/urlExample
    #Body: {}
    @api.response(400, "Validation Error")
    def delete(self, id_val: int):
        return example_delete(id_val), 200

@api.route("/example")
class exampleAPISchema(Resource):
    #Should Get a resource by providing the Unique ID in the Request Body, parsed using a Schema
    #Example:
    #Operation: GET
    #URL: http://127.0.0.1:8060/api/v1/apiTwo/example
    #Body: {"val_id": 1}
    api.expect(id_schema)
    @api.response(400, "Validation Error")
    def get(self):
        data = request.get_json()
        myValID = int(data.get("val_id"))

        return example_get(myValID), 200
    
    #Should create a new resource by providing the Fields in the Request Body, parsed using a Schema
    #Example:
    #Operation: POST
    #URL: http://127.0.0.1:8060/api/v1/apiTwo/example
    #Body: {"val_id": 1, "val_one": "str1", "val_two": "str2"}
    @api.expect(full_schema)
    @api.response(400, "Validation Error")
    def post(self):
        data = request.get_json()
        myValID = data.get("val_id")
        myValOne = data.get("val_one")
        myValTwo = data.get("val_two")

        return example_post(myValID, myValOne, myValTwo), 200

    #Should modify an existing resource by sending ALL fields in the Request Body, parsed using a Schema
    #Any fields not included in the request are set to None
    #Example:
    #Operation: PUT
    #URL: http://127.0.0.1:8060/api/v1/apiTwo/example
    #Body: {"val_id": 1} #sets val_one and val_two to None
    #Body: {"val_id": 1, "val_one": "newStr1"} #Changes val_one to newStr1, sets val_two to None
    #Body: {"val_id": 1, "val_two": "newStr2"} #Changes val_two to newStr2, sets val_one to None
    #Body: {"val_id": 1, "val_one": "newStr1", "val_two": "newStr2"} #Changes both val_one and val_two
    @api.expect(partial_schema)
    @api.response(400, "Validation Error")
    def put(self):
        data = request.get_json()
        myValID = data.get("val_id")
        myValOne = data.get("val_one")
        myValTwo = data.get("val_two")

        return example_put(myValID, myValOne, myValTwo), 200
    
    #Should modify an existing resource by sending ONLY the fields which you want to change in the Request Body, parsed using a Schema
    #Example:
    #Operation: PATCH
    #URL: http://127.0.0.1:8060/api/v1/apiTwo/example
    #Body: {"val_id": 1} #Changes nothing
    #Body: {"val_id": 1, "val_one": "newStr1"} #Changes val_one to newStr1
    #Body: {"val_id": 1, "val_two": "newStr2"} #Changes val_two to newStr2
    #Body: {"val_id": 1, "val_one": "newStr1", "val_two": "newStr2"} #Changes both val_one and val_two
    @api.expect(partial_schema)
    @api.response(400, "Validation Error")
    def patch(self):
        data = request.get_json()
        myValID = data.get("val_id")
        myValOne = data.get("val_one")
        myValTwo = data.get("val_two")

        return example_patch(myValID, myValOne, myValTwo), 200

    #Should Delete a resource by providing the Unique ID in the Request Body, parsed using a Schema
    #Example:
    #Operation: DELETE
    #URL: http://127.0.0.1:8060/api/v1/apiTwo/example
    #Body: {"val_id": 1}
    api.expect(id_schema)
    @api.response(400, "Validation Error")
    def delete(self):
        data = request.get_json()
        myValID = int(data.get("val_id"))

        return example_delete(myValID), 200