import json


class Database:
    data = {}

    @staticmethod
    def write():
        with open("db.json", "w") as file:
            file.write(json.dumps(Database.data))

    @staticmethod
    def read():
        with open("db.json", "r") as file:
            try:
                Database.data = json.loads(file.read())
            except json.decoder.JSONDecodeError:
                pass
