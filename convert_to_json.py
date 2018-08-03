import json
import re

dict2={"name":"storm","age": 30,"children":["a","b"]}
dict3={"name":"storm","age": 30,"children":["a","b"]}
dict1 = {"name":"storm","age": 30,"children":[dict2,dict3]}
print(dict1)
print(type(dict1))

j1 = json.dumps(dict1)
print(j1)
print(type(j1))
def read_callstack(t_dict,file_name):
    last_dict = {}
    is_duplicate_method=0
    with open(file_name, 'r') as f:
        while 1:
            line = f.readline()
            if not line:
                break
            # pass  # do something
            line=line.strip('\tat ')
            # print("line"+line)
            method=re.sub('\((.*?)\)','',line)
            clazz=re.findall('\((.*?)\)', line)[0]
            # print("stripe" + method)
            dict = {"name": "storm", "method": 30,"clazz":"class", "children": []};
            dict['name']=method
            dict['method']=method
            dict['clazz']=clazz
            if t_dict.get(method):
                print('already has this method'+method)
                is_duplicate_method=1
                dict=t_dict.get(method)
            else:
                t_dict[method]=dict
            if last_dict.get('name'):
                dict['children'].append(last_dict)

            last_dict = dict
class node:
    def __init__(self, name, children):
        self.name = name
        self.children = children

    def __str__(self):
        return 'node(' + self.name + ',' + self.children + ')'

if __name__ == '__main__':
    t_dict={}
    read_callstack(t_dict,'./callstacks/init/registerBeanDefinition.txt')
    read_callstack(t_dict,'./callstacks/init/registerSingleton.txt')
    print(t_dict.get('com.fjd.ssm.SSMApplication.main'))
    j1 = json.dumps(t_dict.get('com.fjd.ssm.SSMApplication.main'))
    print(j1)


