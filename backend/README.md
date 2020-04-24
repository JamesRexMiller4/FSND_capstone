# Getting Started
### Pre-requisites and Local Development
Developers planning on cloning down and running this repo should already have the latest version of Python,
pip, and node installed on their local machines. Before installing the requirements, be sure to create a virtual environment
in the root repository. 

Instructions on how to do so can be found be visiting: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

Developers should also have PostgreSQL installed on their local machine before proceeding. Installation instructions can be found by 
visiting: https://www.postgresql.org/docs/9.3/tutorial-install.html

Once PostgreSQL is successfully installed on your machine you will need to create two new databases that ought to be named

**prestige_worldwide**


and


**prestige_worldwide_test**

The final change you will need is to update the models.py file where the database_path at the top of the file reflects your username for your
postgres database. By default this is set to postgres if you do not believe you created a username.

To seed the databases you can run: 

`psql prestige_worldwide < prestige_worldwide.psql`
`psql prestige_worldwide_test < prestige_worldwide.psql`

This database also utilizes Flask-Migrate which allows us to run migrations on our database, making updates to the models/schemas while still holding onto our already existing data.
To learn more about Flask-Migrate visit their site on documentation on how to utilize it: https://flask-migrate.readthedocs.io/en/latest/

## Backend

From the backend folder (backend/) run

`pip install requirements.txt`

This command will install all the necessary packages needed to get the application up and running.

To run the application run the following commands while in the backend directory in your terminal: 

`export FLASK_APP=app`


`export FLASK_ENV=development`


`flask run`


These commands put the application in development mode and directs our application to use app.py as our root file. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the Flask documentation.
The application is run on http://127.0.0.1:5000/ by default and is a proxy in the frontend configuration.


## API Reference

### Movies
**METHOD** | **REQUEST** | **RESPONSE**
--- | --- | ---
**GET** - */movies* | No request body required for GET requests | `{"success": true, "movies": [{"cast_filled": true, "id": 1, "release_date": "2020/11/12", "title": "No Time to Die"}, {"cast_filled": true, "id": 2, "release_date": "2020/06/04", "title": "Wonder Woman 1984"},...` 
**DELETE** - */movies/<int:movie_id>* | No request body required, but endpoint does require proper Authorization Headers and JWT from Executive Producer role | `{"success": true, "deleted": 4}`
**POST** - */movies* | Endpoint requires Executive Producer Auth Role JWT in request header. The request should be sent with a body of: `{"title: '<movie_title>', release_date: 'YYYY/MM/DD', cast_filled: Boolean` | `{"success": true, "id": 12, "title": "Bill and Ted's...", "release_date": "2025/06/04", "cast_filled": false}`
**PATCH** - */movies/<int:movie_id>* | Endpoint requires Executive Producer or Casting Director Auth Role. The request should be sent with a body of the attribute that is intended to be updated *(title, release_date, cast_filled)* - Ex: `{"release_date": "2022/07/26"}` | `{"success": true, "id": <movie_id>}`


### Actors
**METHOD** | **REQUEST** | **RESPONSE**
--- | --- | ---
**GET** - */actors* | No request body required for GET requests | `{"success": true, "actors": [{"age": 38, "gender": "Male", "id": 2, "name": "Rami Malek", "seeking_role": false}, {"age": 32, "gender": "Female", "id": 4, "name": "Lashana Lynch", "seeking_role": false}, {"age": 54, "gender": "Male", "id": 5, "name": "Jeffrey Wright", "seeking_role": false}....`  
**DELETE** - */actors/<int:actor_id>* | No request body required, but endpoint does require proper Authorization Headers from Executive Producer or Casting Director role | `{"success": true, "deleted": 4}`
**POST** - */actors* | Endpoint requires Executive Producer or Casting Director Auth Role. The request should be sent with a body of: `{"name": '<actor_name>', "age": Number, "gender": 'Male/Female' or (can be left blank), "seeking_role": Boolean}` | `{"success": true, "id": 32, "name": "Ralph Fiennes", "age": 57, "gender": "Male", "seeking_role": true}`
**PATCH** - */actors/<int:actor_id>* | Endpoint requires Executive Producer or Casting Director Auth Role. The request should be sent with a body of the attribute that is intended to be updated *(title, release_date, cast_filled)* - Ex: `{"seeking_role": false}` | `{"success": true, "id": <actor_id>}`


### Casts
**METHOD** | **REQUEST** | **RESPONSE**
--- | --- | ---
**GET** - */casts* | No request body required for GET requests | `{"success": true, "actors": [{"age": 38, "gender": "Male", "id": 2, "name": "Rami Malek", "seeking_role": false}, {"age": 32, "gender": "Female", "id": 4, "name": "Lashana Lynch", "seeking_role": false}, {"age": 54, "gender": "Male", "id": 5, "name": "Jeffrey Wright", "seeking_role": false}....`  
**DELETE** - */casts/<int:cast_id>* | No request body required, but endpoint does require proper Authorization Headers from Executive Producer or Casting Director role | `{"success": true, "deleted": 24}`
**POST** - */casts* | Endpoint requires Executive Producer or Casting Director Auth Role. The request should be sent with a body of: `{"movie_id": Number, "actor_id": Number}` | `{"success": true, "id": 32, "movie_id": 5, "actor_id": 30}`



## Testing

From the /backend directory, the test suite can be run using the following commands:


`dropdb prestige_worldwide_test`


`createdb prestige_worldwide_test`


`psql prestige_worldwide_test < trivia.psql`


`unit2 discover`



The first time you run the tests, omit the dropdb command


In addition to the unit tests their is a Postman Collection that be used to verify that the authorization requirements are being fulfilled. To run the test suite
you need to have Postman installed on your local machine : https://www.postman.com/downloads/

Once installed, you can import the collection by clicking import at the top and dragging the *prestige-worldwide.postman_collection.json* file to the import section.
To run the tests be sure to reset your database collection by running in the terminal:

`dropdb prestige_worldwide`


`createdb prestige_worldwide`


`psql prestige_worldwide < trivia.psql`


Then be sure to start up the server by running

`flask run`

Then from Postman you can run the test suites by hitting send for all the various endpoints in the respective role folders.

**Note** It is very likely the Authorization tokens will need to be updated in the collection before you run the collection. If you are getting a large number of failing tests, click on the menu for the folder and navigate to the Authorization tab to update the JWT token.


