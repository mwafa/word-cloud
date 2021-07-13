from models.db import Database
import re
import time
from collections import Counter


class Word:
    __db = None

    def __init__(self) -> None:
        self.__db = Database()

    def __del__(self):
        self.__db.close()

    def getAll(self, limit=0):
        limit = "LIMIT %d" % limit if limit else ""
        q = "SELECT word, SUM(weight) as weight FROM word GROUP BY word ORDER BY weight DESC " + limit
        out = self.__db.query(q)
        return out.fetchall()

    def add(self, t: str):
        regex = r"\b\w+"
        matches = re.findall(regex, t, re.MULTILINE)
        matches = [match.lower() for match in matches]
        counter = Counter(matches)

        created_at = time.strftime('%Y-%m-%d %H:%M:%S')
        q = """INSERT INTO word (created_at, word, weight) VALUES(?,?,?);"""
        data = [(created_at, k, counter[k]) for k in counter.keys()]
        conn = self.__db.connect()
        cursor = conn.cursor()
        cursor.executemany(q, data)
        conn.commit()
        return cursor
