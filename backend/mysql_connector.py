import configparser
import mysql.connector as mysql
import mysql.connector.cursor as cursors
import time

class MySQLDatabaseManager():
    def __init__(self, config:dict) -> None:
        time.sleep(5)
        self.db = mysql.connect(**config)
        self.cursor: cursors.MySQLCursor = self.db.cursor()

        # self.use_database(config.get('database', 'database1'))

    def get_server_info(self)->str:
        return self.db.get_server_info()

    def use_database(self, database_name:str):
        self.cursor.execute('use %s', (database_name,))