from flask import Flask, request
import os
from mysql_connector import MySQLDatabaseManager

app = Flask(__name__)

db_config = {
    "host":"db",
    "user":"root",
    "port":"3306",
    "password":os.environ.get("DB_PASSWORD"),
    "database":'database1'
}
db = MySQLDatabaseManager(db_config)


@app.route("/")
def main():
    outstr = \
'''
<h1>Hello From Flask!</h1>
<h2>Message from database:</h2>
<code>{}</code>
'''.format(db.get_server_info())
    return outstr


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, True)
