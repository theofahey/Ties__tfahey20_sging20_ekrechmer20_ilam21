import sqlite3

class Usernamepassword:

    def __init__ (self, fileName, name):
        self._db = sqlite3.connect(fileName, check_same_thread=False)
        self._cursor = self._db.cursor()
        self._name = name
        self._cursor.execute(f"CREATE TABLE IF NOT EXISTS {self._name}(username TEXT, password TEXT, unique(username));")

    def insert(self, username, password):
        self._cursor.execute(f"INSERT INTO {self._name} VALUES(\"{username}\", \"{password}\");")
        self._db.commit()

    def takeLastEntry(self):
        self._cursor.execute(f"SELECT type FROM {self._name} BY ID DESC LIMIT 1;")
        data= self_cursor.fetchone()
        return data
    def userExists(self, user):
        self._cursor.execute(f"SELECT * FROM {self._name} WHERE username=\"{user}\";")
        if self._cursor.fetchone() is not None:
            return True
        else:
            return False
    def passwordsMatch(self, username, password):
        self._cursor.execute(f"SELECT * FROM {self._name} WHERE username=\"{username}\" AND password=\"{password}\";")
        if self._cursor.fetchone() is not None:
            return True
        else:
            return False

class madlibTable:
    def __init__ (self, fileName, name):
        self._db = sqlite3.connect(fileName, check_same_thread=False)
        self._cursor = self._db.cursor()
        self._name = name
        self._cursor.execute(f"CREATE TABLE IF NOT EXISTS {self._name}(username TEXT, password TEXT, madlib TEXT, topic TEXT, unique(username));")

    def insert(self, username, password, madlib):
        self_cursor.execute(f"INSERT INTO {self._name}(username, password, madlib);")
        self_cursor.commit()

    def idExists(self, id: int):
        self._cursor.execute(f"SELECT * FROM {self._name} WHERE rowid=\"{id}\";")
        if self._cursor.fetchone() is not None:
            return True
        else:
            return False

    def getEntryById(self, id: int):
        # assert self.idExists(id)
        self._cursor.execute(f"SELECT rowid, * FROM {self._name} WHERE rowid={id} LIMIT 1;")
        data= self._cursor.fetchone()
        return data
    def searchByKeyword(self, topic, limit : int):
        self._cursor.execute(f"SELECT rowid, * from {self._name} WHERE topic LIKE /"{topic}\" LIMIT {limit};")
        data = self._cursor.fetchone()
        return data
        





    # def popById(self, id: int):
    #     assert self.idExists(id)
    #
    #     self._cursor.execute(f"SELECT rowid, type from {self._name} WHERE rowid={id} LIMIT 1;")
    #     data = self._cursor.fetchone()
    #     self._cursor.execute(f"DELETE from {self._name} WHERE rowid={id};")
    #     self._db.commit()
    #     return data
#
# class WordTables:
#
#     def __init__(self, fileName, name):
#         self._db= sqlite3.connect(fileName, check_same_thread=False)
#         self._cursor = self._db.cursor()
#         self._name = name
#         self._cursor.execute(f"CREATE TABLE IF NOT EXISTS {self._name} ( id INTEGER, wordList ))
#
#     def takelastEntry(self):
#         self._cursor.execute(f"SELECT type FROM {self._name} WHERE rowid={id} LIMIT 1;")
#         data =self._cursor.fetchone()
#         return data
#
#     def insert(self, id, word1, word2, word3, word4 , word5, word6, word6, word7, word8, word9, word10):
#         self._cursor.execute(f"INSERT INTO {self._name} VALUES(\"{id}\", \"{type}\", \"{type}\", \"{type}\", \"{type}\", \"{type}\", \"{type}\");")
#         self._db.commit()
#
#     def popById(self, id: int):
#         assert self.idExists(id)
#
#         self._cursor.execute(f"SELECT rowid, type from {self._name} WHERE rowid={id} LIMIT 1;")
#         data = self._cursor.fetchone()
#         self._cursor.execute(f"DELETE from {self._name} WHERE rowid={id};")
#         self._db.commit()
#         return data
