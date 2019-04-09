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
def read_callstack(node_dict,link_dict,file_name):
    last_dict = {}
    is_duplicate_method=0
    with open(file_name, 'r') as f:
        while 1:
            line = f.readline()
            if not line:
                break
            # pass  # do something
            line=line.strip('\tat ')
            line = line.strip('\n')
            # print("line"+line)
            method_all=re.sub('\((.*?)\)','',line)
            position=re.findall('\((.*?)\)', line)[0]
            method_all1=method_all
            method_splits=method_all1.rsplit('.', 2)
            package=method_splits[0]
            clazz=method_splits[1]
            method=method_splits[2]

            springtype=clazz
            if clazz.endswith("Reader"):
                springtype='Reader'
            elif clazz.endswith("Scanner"):
                springtype='Scanner'
            elif clazz.endswith("Parser"):
                springtype='Parser'
            elif clazz.endswith("Utils"):
                springtype='Utils'
            elif clazz.endswith("Context"):
                springtype='Context'
            elif clazz.endswith('Application'):
                springtype='Application'
            elif clazz.endswith('Listener'):
                springtype='Listener'
            elif clazz.endswith('Multicaster'):
                springtype='Multicaster'
            elif clazz.endswith('Registrar'):
                springtype='Registrar'
            elif clazz.endswith('PostProcessor'):
                springtype='PostProcessor'


            # print("stripe" + method)
            dict = {"name": "storm", "method": 30,"clazz":"class"};
            dict['package'] = package
            dict['clazz'] = clazz
            dict['method']=method

            dict['position']=position
            dict['springtype']=springtype

            dict['name'] = method_all
            if node_dict.get(method_all):
                print('already has this node '+method_all)
                is_duplicate_method=1
                dict=node_dict.get(method_all)
            else:
                node_dict[method_all]=dict
            if last_dict.get('name'):
                from_node_name=dict.get('name')
                to_node_name=last_dict.get('name')
                path_name=from_node_name+"#"+to_node_name
                if link_dict.get(path_name):
                    num=link_dict.get(path_name)
                    num=num+1
                    link_dict[path_name]=num
                else:
                    link_dict[path_name] = 1

            last_dict = dict
def convert_to_sankey_json(node_dict,link_dict):
    result_dict = {}
    nodes_list=[]
    nodes_index_dict={}
    i=0
    for (k, v) in node_dict.items():
        link_dict_item={}
        link_dict_item['name']=k
        # nodes_list.append(link_dict_item)
        nodes_list.append(v)
        nodes_index_dict[k]=i
        i=i+1
    result_dict['nodes']=nodes_list
    links_list=[]
    for (k, v) in link_dict.items():
        link_dict_item={}
        print(k)
        k_patitions=k.partition('#')
        print(nodes_index_dict)
        print(k_patitions)
        link_dict_item['source']=nodes_index_dict[k_patitions[0]]
        link_dict_item['target']=nodes_index_dict[k_patitions[2]]
        link_dict_item['value']=v
        if link_dict_item['source'] != link_dict_item['target']:

            links_list.append(link_dict_item)
    result_dict['links']=links_list
    return result_dict

class node:
    def __init__(self, name, children):
        self.name = name
        self.children = children

    def __str__(self):
        return 'node(' + self.name + ',' + self.children + ')'

if __name__ == '__main__':
    node_dict={}
    link_dict={}
    read_callstack(node_dict,link_dict,'./callstacks/init/startEvent.txt')
    read_callstack(node_dict,link_dict,'./callstacks/init/registerBeanDefinition.txt')
    read_callstack(node_dict,link_dict,'./callstacks/init/registerSingleton.txt')
    read_callstack(node_dict,link_dict,'./callstacks/init/onApplicationEvent.txt')
    read_callstack(node_dict,link_dict,'./callstacks/init/registerResolvableDependency.txt')
    read_callstack(node_dict,link_dict,'./callstacks/init/multitenantConfigurationBeanDefinitionRegister.txt')
    read_callstack(node_dict,link_dict,'./callstacks/init/autowireConfig.txt')
    read_callstack(node_dict,link_dict,'./callstacks/init/beanTypeRegistry.txt')

    result_dict=convert_to_sankey_json(node_dict,link_dict)
    print(result_dict)
    j1 = json.dumps(result_dict)
    print(j1)


