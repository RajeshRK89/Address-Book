# Address-Book

Steps to run the code:

1) Clone the repository

2) change the env_dev to .env

3) Run docker-compose up 

4) Run python manage.py setup by getting inside the backend container shell

5) You will get the client id and secret id for the application 

6) To get the access token follow the below steps:
     
     In postman in authorisation section , provide your client_id and secret as generated before in the username and password section by choosing basic auth 

     provide password , username and grant_type  (for the first time use admin@addressbook.com as admin and password and swordfish , grant_type as password)

    or use 

    http://0.0.0.0:8000/user (user viewset to generate users which is of no restriction (allowny is provided))


7) Run the API's for crud
    keeping the access token in authorisation section by choosing bearer token

    1) http://0.0.0.0.8000/user (get, post, patch and delete)


    2)http://0.0.0.0.8000/address(get, post, patch and delete)
