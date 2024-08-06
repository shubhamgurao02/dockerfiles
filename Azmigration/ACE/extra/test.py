import os
from ruamel.yaml import YAML
import os
import argparse
import base64,requests

yaml = YAML()
current_path = os.getcwd()

buidlid=4217
if buidlid:
    
    config_file='Chart.yaml'
    file_name = os.path.join(current_path, config_file)
    with open(file_name, 'r') as file:
        chart = yaml.load(file)
    version=chart['version']
    print(version)
    chart_version=version.split('.')
    patch_version=int(chart_version[2])
    min_version=int(chart_version[1])
    maj_version=int(chart_version[0])
    if patch_version >= 100 and min_version < 50 :
        print("min",min_version)
        print("patch",patch_version)
        new_min_version=min_version+1
        new_patch_version=0
        new_maj_version=maj_version
    if  min_version == 50 :
        new_maj_version=maj_version+1
        new_min_version=0
        print("HI")
        new_patch_version=0
    
    if patch_version <= 100 and (0 <= min_version < 50):
        new_patch_version=patch_version+1
        print("mc")
        new_maj_version=maj_version
        new_min_version=min_version
    new_version=f"{new_maj_version}.{new_min_version}.{new_patch_version}"
    chart['version'] = new_version

    with open(file_name, 'w') as file:
        yaml.dump(chart, file)
    print(chart["appVersion"])
    l1=chart["appVersion"].split('.')
    l1.pop(2)
    l1.append(str(buidlid))
    chart['appVersion'] = str('.'.join(map(str,l1)))
    with open(file_name, 'w') as file:
        yaml.dump(chart, file)
    