import mysql.connector as mysql
import mysql.connector.cursor as cursors
import time


class MySQLDatabaseManager():
    def __init__(self, config: dict) -> None:
        time.sleep(5)
        self.db = mysql.connect(**config)
        self.cursor: cursors.MySQLCursor = self.db.cursor()

        self.cursor.execute('use database1')

        # self.cursor.execute('show tables')
        # print('Tables are', self.cursor.fetchall())

    def get_server_info(self) -> str:
        return self.db.get_server_info()

    def insert_country(self, table_name, *data):
        # Format the data for the query
        formated_data = list(data)
        for i in range(len(formated_data)):
            value = data[i]
            if value == None:
                return

            elif type(value) == str:
                value = value.replace("'", "") #Remove single quotes from the string
                formated_data[i] = "'" + value + "'"

            elif type(value) in [int, float]:
                formated_data[i] = str(value)

        sql_query = "INSERT INTO {} (name, capital, population, area) values ({})".format(table_name, ",".join(formated_data))
        self.cursor.execute(sql_query)
        self.db.commit()

    def count_rows(self, tablename):
        sql_query = "SELECT COUNT(*) FROM {}".format(tablename)
        self.cursor.execute(sql_query)
        return self.cursor.fetchone()[0]

    def get_all_countries(self):
        sql_query = "SELECT * FROM countries"
        self.cursor.execute(sql_query)
        return self.cursor.fetchall()
