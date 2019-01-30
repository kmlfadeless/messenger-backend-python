from v1.model.abstract import *


class User(Abstract):
    def get_json(self):
        return {
            "name": self.name,
            "password": self.password,
            "email": self.email,
        }

