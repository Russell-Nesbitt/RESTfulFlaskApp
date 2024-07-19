# from models.addresses import Address

def example_post(val_one: str, val_two: str, val_three: int):
    return "Ran example_post with " + val_one + " " + val_two + " " + str(val_three)

def example_get(val_one: int):
    return "Ran example_get with " + str(val_one)

#def address_post(street_one: str, street_two: str, city: str, state: str, zip: str):
#   return "Added Address " + street_one + " " + city
#     toAddAddress = Address(street_one, street_two, city, state, zip)
#     toAddAddress.save()
#     return "Added Address " + street_one + " " + city

#def address_get(inputID: int):
#    return "Got Address " + str(inputID)
#     get_address = Address._get_by_id(inputID)
#     return get_address.toDict()