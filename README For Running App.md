
To Run:
Navigate to to .../RESTfulFlaskApp
IMPORTANT NOTE: All "pipenv run" prefixes can be removed if running commands in "pipenv shell" (RECOMMENDED)

If Fresh Pull - Only needs to be done ONCE
pipenv --python 3.12
pipenv install

To Run the App:
pipenv run python app.py
	- runs on port 8060
OR (NOT RECOMMENDED)
pipenv run flask app
	- Make note of the port number given after "Running on..." on your terminal. It should be the last four digits, e.g. "8060"

To Access API Endpoints:
Open Postman or other API Testing Tool of Choice

If running via <pipenv run python app.py>:
http://127.0.0.1:8060/api/v1/<URL_Suffix_Here>
If running via <pipenv run flask app>:
http://127.0.0.1:<Your_Port_Number>/api/v1/<URL_Suffix_Here>


API One Endpoints
http://127.0.0.1:8060/api/v1/apiOne/example

	
invites/<org_id>/vendor/bulk
POST {"email": ["stringOne, "stringTwo", "stringThree"]}
	Checks to see if any of the users are already present in the database 
		If so, stops and returns the first failing address - Nothing is added to the database.
    Retrieves the Org associated with org_id
    Creates New Users with Provided Emails and sign-up steps INVITED
	For each New User
        Creates a new Vendor with Empty Init
	    Sets the New User's Vendor to the New Vendor
	    Sets the New Vendor's User to the New User
	    Adds the New User to the Found Org
	    Saves the Org, the User, and the Vendor


STEP 2) AFTER THE USER OBJECT HAS BEEN INTIALIZED, CREATE THE ACCOUNT AND BEGIN FILLING OUT THE USER OBJECT
authentication/create_account
POST {"email": "string", "password": "string"}
	EMAIL MUST CORRESPOND TO AN INVITED (AND THUS INITIALIZED) USER OBJECT
	Retrives User object associated wih email
	Saves the user's password with firebase authentication
	Updates the User's sign-up step to ACOUNT_CREATED

user/<user_email>/confirm
PUT {"test_code": "string"}
	Gets the User associated with the provided user_email
	Checks to see if the User's invite_code field matches the provided test_code
	If so, sets the user's signup_step to CODE_CONFIRMED, saves the User, and returns 200
	If not, does nothing and returns 400

onboarding/<user_email>/profile_updated
onboarding/<user_email>/org_updated
onboarding/<user_email>/members_invited
onboarding/<user_email>/vendors_invited
onboarding/<user_email>/completed
For all: PUT {nothing}
	Gets the User associated with the provided user_email
	Sets the user's signup_step to the suffix (e.g. PROFILE_UPDATED, ect)
	Saves the User


STEP 3) AFTER THE USER, VENDOR AND ORG OBJECTS HAVE BEEN INITIALIZED, COMPLETE THE USER, VENDOR AND ORG OBJECTS
USER:
user/<user_email>
PUT {"first_name": "string", "last_name": "string", "phone": "1234567890"}
	Gets the User associated with the provided user_email
	Updates the User's first_name, last_name, and phone fields
	Saves the User

ORG:
org/<user_email>
WITH FULL ADDRESS
PUT {"street_one": "string", "street_two": "string", "city": "string", "state": "string", "zip": "string", "phone": "string"}
WITH PARTIAL ADDRESS
PUT {"street_one": "string", "city": "string", "state": "string", "zip": "string", "phone": "string"}
	Gets the User associated with the user_email provided
	User MUST be an Admin to access this endpoint. If the found user is Not an admin, do nothing and return badrequest.
	Gets the Org associated with the found user
	Creates a new Address using the information provided
	Saves the Address
	Updates the Org's phone field
	Updates the Org's address to the new Address
	Saves the Org

org/<org_id>/vendors
GET {nothing}
	Gets the Org associated with the org_id provided
	Returns a list of all the vendors associated with that org

VENDOR:
vendor/<user_email>
WITH FULL ADDRESS
PUT {"company": "string", "type": "string", "street_one": "string", "street_two": "string", "city": "string", "state": "string", 
"zip": "string"}
WITH PARTIAL ADDRESS
PUT {"company": "string", "type": "string", "street_one": "string", "city": "string", "state": "string", "zip": "string"}
	Gets the User associated with the User Email
	Gets the Vendor ID associated with that User
	Gets the Vendor associated with that Vendor ID
	Creates a new Address using the information provided
	Saves the Address
	Updates the Vendor's company and type fields
	Updates the Vendor's address to the new Address
	Saves the Vendor

#NOTE: DUE TO DIFFICULTY AUTOMATING, THESE THREE ENDPOINTS ARE NOT INCLUDED IN THE PYTEST SUITE AND MUST BE MANUALLY TESTED.
STEP 4) UPLOAD FILE OBJECTS AND ASSIGN TO USERS AND ORGS
FILE:
file/file_upload
POST {"file": FILE (NOT SURE HOW TO WRITE THIS IN JSON)}
	Takes the File sent in the request under the key 'file' #getFile = request.files['file']
	Parses the file's name, extracts the file type suffix
	If the file's type does not appear in the FileTypes enum, return 400.
	Otherwise, uploads the file to api/files/uploaded_files/<filename>
	Creates a new File using the file's name and uploads location
	Saves the File

file/setuserpic/<user_email>
PUT {"file_name": "string"}
	Gets the User associated with the User Email
	Gets the File associated with the File Name
	Sets that User's pic field to that File's ID
	Saves the User

file/setorglogo/<org_id>
PUT {"file_name": "string"}
	Gets the Org associated with the Org ID
	Gets the File associated with the File Name
	Sets that Org's logo field to that File's ID
	Saves the Org