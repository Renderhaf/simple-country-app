from flask import Flask, request
import mysql.connector as mysql
import os
import time

app = Flask(__name__)

time.sleep(5)
db = mysql.connect(
    host="db",
    user="api",
    port="3306",
    password=os.environ.get("DB_PASSWORD"),
)

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
