import yaml
import json

chart = {
    'apiVersion':'v2',
    'name': 'deploy-cmr-mx-sitio-publico',
    'description': 'Cmr mx sitio publico Chart',
    'version': '1.1.2',
    'dependencies':[{
        'name':'helm-base',
        'alias': 'sitio-publico',
        'version': '1.0.2',
        'repository': 'https://hub.fif.tech/chartrepo/sitio-publico'
    },{
        'name': 'helm-base',
        'alias': 'sitio-publico-next',
        'version': '1.0.2',
        'repository': 'https://hub.fif.tech/chartrepo/sitio-publico'
    }]
}

yalm_output = yaml.dump(chart, sort_keys=False)
print(yalm_output)


def write_yaml_to_file(py_obj,filename):
    dependencia = []
    data = ''
    alias = []
    for i in chart['dependencies']:            
        dependencia.append(i)            
    for j in dependencia:        
        data = j                
        alias.append(data["alias"])
    print(alias)    

# x here reprents the python object
    with open(f'{filename}.yaml', 'w',) as f :
        yaml.dump(py_obj,f,sort_keys=False) 

write_yaml_to_file(chart, 'Chart')