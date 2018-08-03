import json
from collections import OrderedDict
def jsonDefault(OrderedDict):
    return OrderedDict.__dict__

class SampleClass(object):
    def __init__(self,*args,**kwargs):pass
    def __repr__(self):
        return json.dumps(self, default=jsonDefault, indent=4)
    def add_record_as_data(self,_record):
        self.__dict__.update(_record.__dict__)
    def add_record_as_attr(self,_record):
        self.record = _record
obj = SampleClass()
obj.name = 'name'
print (obj)