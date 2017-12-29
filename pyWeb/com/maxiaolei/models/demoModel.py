import json

class ResDemo:
    age=0
    name=''
    def toJSON(self):
        return json.dumps(self.__dict__)

