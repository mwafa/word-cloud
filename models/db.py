from models.var import DB_FILE
import sqlite3


class Database:

    db_file = None
    connection = None

    def __init__(self, db_file=DB_FILE) -> None:
        self.db_file = db_file
        self.connect()

    def __del__(self):
        self.close()

    def connect(self):
        if(self.connection):
            return self.connection
        self.connection = sqlite3.connect(self.db_file)
        return self.connection

    def query(self, q, data=()):
        conn = self.connection if self.connection else self.connect()
        cursor = conn.cursor()
        cursor.execute(q, data)
        conn.commit()
        return cursor

    def close(self):
        conn = self.connection if self.connection else self.connect()
        return conn.close()
