from flask import Flask, request, jsonify
import os
from mysql_connector import MySQLDatabaseManager
import requests, json

app = Flask(__name__)

db_config = {
    "host":"db",
    "user":"root",
    "port":"3306",
    "password":os.environ.get("DB_PASSWORD"),
    "database":'database1'
}

db = MySQLDatabaseManager(db_config)

#Init the db data
if db.count_rows('countries') == 0:
    countries = requests.get("https://restcountries.eu/rest/v2/all").json()
    for country in countries:
        db.insert_country("countries", country["name"], country["capital"], country["population"], country["area"])

@app.route("/countries", methods=['GET'])
def main(response):
    data = []
    data.append(db.get_titles())
    data.extend(db.get_all_countries())
    return jsonify(data)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, True)
