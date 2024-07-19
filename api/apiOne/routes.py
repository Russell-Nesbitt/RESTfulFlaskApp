from flask import request
from flask_restx import Resource

from api.apiOne import api

from api.apiOne.schemas import (complex_schema, simple_schema)

from api.apiOne.handlers import (example_get, example_post)

@api.route("/<id_val>/example")
class inviteUser(Resource):
    @api.response(400, "Validation Error")
    def get(self, id_val: int):

        return example_get(id_val), 200

@api.route("/example")
class exampleAPI(Resource):
    #api.expect(simple_schema)
    #@api.response(400, "Validation Error")
    #def get(self):
        #print("Entered exampleAPI.get")
        #data = request.get_json()
        #print("Data: ", data)

        #myOnlyVal = int(data.get("val_only"))

        #return example_get(myOnlyVal), 200


        #return address_get(myID), 200
    
    @api.expect(complex_schema)
    @api.response(400, "Validation Error")
    def post(self):
        print("Entered exampleAPI.post")

        data = request.get_json()
        print("Data: ", data)
        myValOne = data.get("val_one")
        myValTwo = data.get("val_two")
        myValThree = data.get("val_three")

        return example_post(myValOne, myValTwo, myValThree), 200

        #myCity = data.get("city")
        #myState = data.get("state")
        #myZip = data.get("zip")
        #return address_post(myStreetOne, myStreetTwo, myCity, myState, myZip), 200

    def put(self):
        return 200
    
    def patch(self):
        return 200

    def delete(self):
        return 200