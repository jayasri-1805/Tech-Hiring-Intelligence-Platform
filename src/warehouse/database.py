import pymysql
from .config import DB_CONFIG

class Database:
    def connect(self):
        return pymysql.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"],
            port=DB_CONFIG["port"],
            autocommit=True,
        )
