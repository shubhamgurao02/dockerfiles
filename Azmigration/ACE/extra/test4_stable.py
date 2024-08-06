import argparse
import base64
import os
import subprocess
from ruamel.yaml import YAML
from subprocess import Popen, PIPE
current_path = os.getcwd()
yaml = YAML()
parser = argparse.ArgumentParser(description="Process and encode files/folders in base64.")
parser.add_argument('-p', type=str, help="Path to folder to zip and encode in base64")
parser.add_argument('-k', type=str, help="Path to folder to encode each file in base64 and print names")
parser.add_argument('-t', type=str, help="Path to files to add to JKS truststore and encode in base64")
parser.add_argument('-s', type=str, help="Path to a single file to encode in base64")
parser.add_argument('-m', type=str, help="Path of helm values.yaml file")
parser.add_argument('-w', type=str, help=".jks file password")
parser.add_argument('-z', type=str, help="Path of empty jks file")
args = parser.parse_args()
helm_file=args.m
helm_file=os.path.join(current_path,helm_file)
passwd=args.w
jksfile=args.z
jksfile=os.path.join(current_path,jksfile)
if args.p:
    folder_path = args.p
    #print(folder_path)
    
    folder_name="Defaultpolicies.zip"
    file_name=os.path.join(current_path,folder_path,folder_name)
    #print(folder_path)
    os.chdir(folder_path)
    zip_command = f'zip -r "{folder_name}" "Defaultpolicies/"'
    subprocess.run(zip_command, shell=True, check=True)
    file= open(file_name, 'rb') 
    encoded = base64.b64encode(file.read()).decode('utf-8')
    with open(helm_file, 'r') as file:
        yaml_data = yaml.load(file)
    yaml_data['policyprojectdata'] = encoded
    with open(helm_file, 'w') as file:
        yaml.dump(yaml_data, file)  
    print(encoded) 

if args.k:
    keystore_path = args.k
    keystore_path=os.path.join(current_path,keystore_path)
    filenames = [file for _, _, fnames in os.walk(keystore_path) for file in fnames]
    for i in filenames:
        file_name=os.path.join(keystore_path,i)  #keystorename1 #keystoredata1
        #print("k",file_name)
        keystore_file= open(file_name, 'rb') 
        keystore_encoded = base64.b64encode(keystore_file.read()).decode('utf-8')
        print(i,keystore_encoded)
    #print(filenames)
    #print(keystore_path)
if args.t:
    truststore_path = args.t
    truststore_path=os.path.join(current_path,truststore_path)
    filenames = [file for _, _, tnames in os.walk(truststore_path) for file in tnames]
    for i in filenames:
        file_name=os.path.join(truststore_path,i)
        #print(file_name)
        alias=i.split('.')[0]  #truststoredata
        print(alias)
        tcmd=f"keytool -import -trustcacerts -file {file_name} -alias {alias} -keystore {jksfile} -storepass {passwd}"
        #print(tcmd)
        subprocess.run(tcmd, shell=True, check=True)
    tconfig=open(jksfile, 'rb') 
    trust_encoded = base64.b64encode(tconfig.read()).decode('utf-8')
    print(trust_encoded)
    with open(helm_file, 'r') as file:
        yaml_data = yaml.load(file)
    yaml_data['serverconfdata'] = trust_encoded
    with open(helm_file, 'w') as file:
        yaml.dump(yaml_data, file) 
    
if args.s:
    file_path = args.s
    server_configname=os.path.join(current_path,file_path)
    #print(server_configname)
    config_file= open(server_configname, 'rb') 
    config_encoded = base64.b64encode(config_file.read()).decode('utf-8')
    print(config_encoded)
    with open(helm_file, 'r') as file:
        yaml_data = yaml.load(file)
    yaml_data['serverconfdata'] = config_encoded
    with open(helm_file, 'w') as file:
        yaml.dump(yaml_data, file)  
    

##############################################
#python test4_stable.py -p configurations/dev/policy/ -k configurations/dev/config/keystore/ -s configurations/dev/config/server.conf.yaml -t configurations/dev/config/truststore/ -hv values.yaml -e truststore.jks -pw poloPo10