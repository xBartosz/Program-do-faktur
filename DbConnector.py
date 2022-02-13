import mysql.connector
from typing import Final

class DbConnector:
    DB_USER: Final[str] = "root"
    DB_PASSWORD: Final[str] = ""
    DB_HOST: Final[str] = "localhost"
    DB_NAME: Final[str] = "accounts"

    def __init__(self):
        self.connection = mysql.connector.connect(user=self.DB_USER, password=self.DB_PASSWORD, host=self.DB_HOST, database=self.DB_NAME)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def get_cursor(self):
        return self.cursor

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()

