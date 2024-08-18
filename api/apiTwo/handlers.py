def example_post(val_id: int, val_one: str, val_two: str):
    return "Ran apiTwo's example_post with " + str(val_id) + " " + val_one + " " + val_two

def example_get(val_id: int):
    return "Ran apiTwo's example_get with " + str(val_id)

def example_delete(val_id: int):
    return "Ran apiTwo's example_delete with " + str(val_id)

def example_put(val_id: int, val_one, val_two):
    returnStr = "Ran apiTwo's example_post with " + str(val_id)

    if val_one == None:
        returnStr += " None "
    else:
        returnStr += " " + val_one + " "
    
    if val_two == None:
        returnStr += "None"
    else:
        returnStr += val_two
    
    return returnStr

def example_patch(val_id: int, val_one, val_two):
    returnStr = "Ran apiTwo's example_patch with " + str(val_id)

    if val_one == None:
        returnStr += " None "
    else:
        returnStr += " " + val_one + " "
    
    if val_two == None:
        returnStr += "None"
    else:
        returnStr += val_two
    
    return returnStr