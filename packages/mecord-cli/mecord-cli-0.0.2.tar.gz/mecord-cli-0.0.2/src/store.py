import os
import json

def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner

@singleton
class Store(object):
    def __init__(self):
        self.path = 'data.json'
        
        if not os.path.exists(self.path):
            with open(self.path, 'w') as f:
                json.dump({}, f)
                
    def read(self):
        with open(self.path, 'r') as f:
            data = json.load(f)
            
        return data
    
    def write(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f)

    

# if __name__ == '__main__':
#     store = Store()

#     data = store.read()
#     print(data)

#     data['key'] = 'value'
#     store.write(data)