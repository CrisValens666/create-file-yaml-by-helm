import yaml

values = {
    # foreach servicio ['sitio-publico:','sitio-publico-next']
    
        'sitio-publico':{ 
            'helmGlobalDependency': { 'podSecurityContext': { 'runAsUser':0 }},
            'replicaCount':1,
            'fullnameOverride': 'cmr-mx-sitio-publico',
            'environment': 'qa',
            'team': 'axmos',
            'dependencies': { 
                'vault': True 
                },
            'image': { 
                'repository': 'sitio-publico/cmr-mx-sitio-publico-qa',
                'pullPolicy': 'IfNotPresent',
                'tag': 'de7bf9da32132b9e1f8106efa73b320fe33e42cb',
                'addEnvironment': False
                },
            'selectorLabels': {
                'country': 'chile',
                'component': 'web',
                'partOf': 'axmos-poc'
                },
            'env': [],
            'resources': {},
            'args': [],
            'volumeMounts': [{
                'name': 'falabella-com-mx-cert',
                'readOnly': True,
                'mountPath': '/run/secrets/wildcard.falabella.com.mx.crt',
                'subPath': 'wildcard.falabella.com.mx.crt'
            },{
                'name': 'falabella-com-mx-cert',
                'readOnly': True,
                'mountPath': '/run/secrets/wildcard.falabella.com.mx.key',
                'subPath': 'wildcard.falabella.com.mx.key'
            },{
                'name': 'fif-tech-cert',
                'readOnly': True,
                'mountPath': '/run/secrets/wildcard.fif.tech.bundle.crt',
                'subPath': 'wildcard.fif.tech.bundle.crt'
            },{
                'name': 'fif-tech-cert',
                'readOnly': True,
                'mountPath': '/run/secrets/wildcard.fif.tech.key',
                'subPath': 'wildcard.fif.tech.key'
            }],
            'volumes':[{
               'name': 'falabella-com-mx-cert',
               'secret':{
                   'secretName': 'falabella-com-mx-cert',
                   'items':[{
                       'key': 'tls.crt',
                       'path': 'wildcard.falabella.com.mx.crt'
                   },{
                       'key': 'tls.key',
                       'path': 'wildcard.falabella.com.mx.key'
                   }]
               }
            },{
               'name': 'fif-tech-cert',
               'secret':{
                   'secretName': 'fif-tech-cert',
                   'items':[{
                       'key': 'tls.crt',
                       'path': 'wildcard.fif.tech.bundle.crt'
                   },{
                       'key': 'tls.key',
                       'path': 'wildcard.fif.tech.key'
                   }]
               }
            }],
        'vault':{
            'role':'crm-mx-qa',
            'path':'canales-cl-swarm-preprod',
            'serviceAccount':'vault-auth-fif'
        },
        'service':[{
            'portName': 'https',
            'type': 'ClusterIP',
            'protocol': 'TCP',
            'port': 443
        }],
        'autoscaling':{
            'enabled': False,
            'minReplicas': 1,
            'maxReplicas': 2,
            'targetCPUUtilizationPercentage': 60,
            'targetMemoryUtilizationPercentage': 80
        },
        'nodeSelector': {},
        'tolerations': [],
        'affinity': {},
        'configmap':{
            'enabled': False,
            'data':{
                'EXAMPLE': 'test'
            }        
        },
        'livenessProbe':{
            'enabled': False,
            'yaml':{
                'initialDelaySeconds': 10,
                'periodSeconds': 3
            }
        },
        'readinessProbe':{
            'enabled': False,
            'yaml':{
                'initialDelaySeconds': 10,
                'periodSeconds': 3
            }
        },
        'containerExtraSpec':{
            'yml':''
        },
        'hostAliases':{
            'enabled': False,
            'hostNames':[{
                'ip':'0.0.0.0',
                'hostnames':[
                  'falabella-test'  
                ]   
            }]
        },
        'lifecycle':{
            'enabled': False,
            'preStop':{
                'exec':{
                    'command': '' #["sleep","10"]         
                }                    
            }      
        },
        'virtualService':{
            'enabled': False,
            'annotations': {},
            'gateways':[{
                'my-gateway'
            }],
            'hosts':[{
                '*'
            }],
            'http':[{
                'match':{
                    'uri':{
                        'prefix': '/my-path'
                    },
                    'route':{
                        'destination':{
                            'host':'my-destination',
                            'port': 80
                        }
                    }
                }    
            }],
            'enableCorsPolicy': False,
            'corsPolicy': {}  
        },
        'secrets':[{
            'name':'falabella-com-mx-cert',
            'stringData':{
                'tls.crt':'vault:kv/domains/falabella_com_mx/certificate#falabella_com_mx_crt',
                'tls.key':'vault:kv/domains/falabella_com_mx/certificate#falabella_com_mx_key'
            }
        },{
            'name':'fif-tech-cert',
            'stringData':{
                'tls.crt':'vault:kv/domains/fif_tech/certificate#fif_tech_crt',
                'tls.key':'vault:kv/domains/fif_tech/certificate#fif_tech_key'
            }
        }]                
        },
        'sitio-publico-next':{}
    
}

yalm_output = yaml.dump(values, sort_keys=False)
print(yalm_output)

def write_yaml_to_file(py_obj,filename):
# x here reprents the python object
    with open(f'{filename}.yaml', 'w',) as f :
        yaml.dump(py_obj,f,sort_keys=False) 

write_yaml_to_file(values, 'values')