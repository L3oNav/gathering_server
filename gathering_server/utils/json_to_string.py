import json

class JsonToString:

    def __init__(self, data):
        self.data = data

    def output_model(self):
        data = self.data
        for collection, i in zip(data['resources'], range(len(data['resources']))):
            for value, k in zip(collection['value'], range(len(collection['value']))):
                data['resources'][i]['value'][k] = json.dumps(value)
            data['resources'][i] = json.dumps(collection)
        for collection, i in zip(data['prices'], range(len(data['prices']))):
            for value, k in zip(collection['value'], range(len(collection['value']))):
                data['prices'][i]['value'][k] = json.dumps(value)
            data['prices'][i] = json.dumps(collection)
        return data
