import sqlite3

class TypeTables:

    def __init__ (self, fileName, name):
        self._db = sqlite3.connect(fileName, check_same_thread=False)
        self._cursor = self._db.cursor()
        self._name = name
        self._cursor.execute(f"CREATE TABLE IF NOT EXISTS {self._name}(id INTEGER, type TEXT);")

    def insert(self, id, type):
        self._cursor.execute(f"INSERT INTO {self._name} VALUES(\"{id}\", \"{type}\");")
        self._db.commit()

    def takeLastEntry(self):
        self._cursor.execute(f"SELECT type FROM {self._name} BY ID DESC LIMIT 1;")
        data= self_cursor.fetchone()
        return data

    def popById(self, id: int):
        assert self.idExists(id)

        self._cursor.execute(f"SELECT rowid, type from {self._name} WHERE rowid={id} LIMIT 1;")
        data = self._cursor.fetchone()
        self._cursor.execute(f"DELETE from {self._name} WHERE rowid={id};")
        self._db.commit()
        return data

class WordTables:

    def __init__(self, fileName, name):
        self._db= sqlite3.connect(fileName, check_same_thread=False)
        self._cursor = self._db.cursor()
        self._name = name
        self._curosr.execute(f"CREATE TABLE IF NOT EXISTS {self._name} ( id INTEGER, wordList ))

    def takelastEntry(self):
        self._cursor.execute(f"SELECT type FROM {self._name} WHERE rowid={id} LIMIT 1;")
        data =self._cursor.fetchone()
        return data

    def insert(self, id, word):
        self._cursor.execute(f"INSERT INTO {self._name} VALUES(\"{id}\", \"{type}\");")
        self._db.commit()

    def popById(self, id: int):
        assert self.idExists(id)

        self._cursor.execute(f"SELECT rowid, type from {self._name} WHERE rowid={id} LIMIT 1;")
        data = self._cursor.fetchone()
        self._cursor.execute(f"DELETE from {self._name} WHERE rowid={id};")
        self._db.commit()
        return data
