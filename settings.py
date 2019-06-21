import json


class Settings:
    ws = {}
    rpc = {}

    def __init__(self, jsondump):
        self.__dict__ = jsondump

    @classmethod
    def fromFile(cls, file):
        with open(file, 'r') as f:
            json_data = json.load(f)
            return Settings(json_data)
        return None
