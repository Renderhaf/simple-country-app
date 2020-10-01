# Simple Country App #
This is a little app that uses docker-compose to show a list of countries and some info about them

## Running the app locally ##
To run the app locally, just run `docker-compose up`

## App structure ##
The app is made up of 4 docker containers:
 - A MySQL Database
 - A Python (Flask) API that connects to the database
 - A Vue App to view the data sent from the API
 - An Nginx reverse proxy
