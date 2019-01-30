from v1.db import *


class Abstract(object):
    def __init__(self):
        self.db = db()

    def get_json(self):
        return {}

    def save(self):
        self.db[self.__class__.__name__].insert_one(self.get_json())

