from api.config import Config
import mysql.connector
from mysql.connector import Error


class DBManager:

    @property
    def isConnected(self):
        return self.conn.is_connected()

    def query(self, sqlQuery, *params, responseQuery=False):
        try:
            self.connect()
            assert self.isConnected
            cursor = self.conn.cursor()
            cursor.execute(sqlQuery, params)
            if not responseQuery:
                self.conn.commit()
                return cursor.rowcount
            else:
                return cursor.fetchall()
        except AssertionError:
            print("DBManager could not query: mysql connected")
        finally:
            self.disconnect()

    def connect(self):
        try:
            # Conecte-se ao host
            self.conn = mysql.connector.connect(**Config.MYSQL)
        except Error as e:
            print("Could not connect to MYSQL: ", e)

    def disconnect(self):
        if self.isConnected:
            self.conn.close()


db_manager = DBManager()

