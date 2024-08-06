import argparse
import base64
import os
import subprocess
from ruamel.yaml import YAML

# Initialize YAML parser
yaml = YAML()
current_path = os.getcwd()

# Initialize argument parser
parser = argparse.ArgumentParser(description="Process and encode files/folders in base64.")
parser.add_argument('-p', type=str, help="Path to folder to zip and encode in base64")
parser.add_argument('-k', type=str, help="Path to folder to encode each file in base64 and print names")
parser.add_argument('-t', type=str, help="Path to files to add to JKS truststore and encode in base64")
parser.add_argument('-s', type=str, help="Path to a single file to encode in base64")
parser.add_argument('-m', type=str, help="Path of helm values.yaml file")
parser.add_argument('-w', type=str, help=".jks file password")
parser.add_argument('-z', type=str, help="Path of empty jks file")
parser.add_argument('-b', type=str, help="Path of barfile url file")

args = parser.parse_args()

helm_file = args.m
passwd = args.w
jksfile = args.z
helm_file=os.path.join(current_path,helm_file)
jksfile=os.path.join(current_path,jksfile)

if args.p:
    folder_path = args.p
    folder_name = "Defaultpolicies.zip"
    file_name = os.path.join(current_path, folder_path, folder_name)

    try:
        os.chdir(folder_path)
        zip_command = f'zip -r "{folder_name}" "Defaultpolicies/"'
        subprocess.run(zip_command, shell=True, check=True)

        with open(file_name, 'rb') as file:
            encoded = base64.b64encode(file.read()).decode('utf-8')

        with open(helm_file, 'r') as file:
            yaml_data = yaml.load(file)

        yaml_data['policyprojectdata'] = encoded

        with open(helm_file, 'w') as file:
            yaml.dump(yaml_data, file)

        print(encoded)
    except Exception as e:
        print(f"Error processing folder {folder_path}: {e}")

#################################for keystore#######
if args.k:
    keystore_path = os.path.join(current_path, args.k)
    print("Hi")
    try:
        for root, _, files in os.walk(keystore_path):
            for file in files:
                file_name = os.path.join(root, file)
                # with open(file_name, 'rb') as keystore_file:
                #     keystore_encoded = base64.b64encode(keystore_file.read()).decode('utf-8')
                # print(file, keystore_encoded)
                with open(helm_file, 'r') as file:
                    yaml_data = yaml.load(file)
                #print("Hello",yaml_data['keystorename1'].split('.'))
                print(file_name.split('.')[1])
                if file_name.split('.')[1] == 'sth':
                    with open(file_name, 'rb') as file:
                        kencoded = base64.b64encode(file.read()).decode('utf-8')

                    with open(helm_file, 'r') as file:
                        yaml_data = yaml.load(file)

                    yaml_data['keystoredata2'] = kencoded
                    print("sth",kencoded)
                    with open(helm_file, 'w') as file:
                        yaml.dump(yaml_data, file)
                elif file_name.split('.')[1] == 'kdb':
                    with open(file_name, 'rb') as file:
                        kencoded = base64.b64encode(file.read()).decode('utf-8')

                    with open(helm_file, 'r') as file:
                        yaml_data = yaml.load(file)

                    yaml_data['keystoredata1'] = kencoded
                    print("kdb",kencoded)
                    with open(helm_file, 'w') as file:
                        yaml.dump(yaml_data, file)
                else:
                    print("No proper file present")

    except Exception as e:
        print(f"Error processing keystore folder {keystore_path}: {e}")

################################for truststore ########################
if args.t:
    truststore_path = os.path.join(current_path, args.t)

    try:
        for root, _, files in os.walk(truststore_path):
            for file in files:
                file_name = os.path.join(root, file)
                alias = file.split('.')[0]
                tcmd = f"keytool -import -trustcacerts -file {file_name} -alias {alias} -keystore {jksfile} -storepass {passwd}"
                subprocess.run(tcmd, shell=True, check=True)

        with open(jksfile, 'rb') as tconfig:
            trust_encoded = base64.b64encode(tconfig.read()).decode('utf-8')

        with open(helm_file, 'r') as file:
            yaml_data = yaml.load(file)

        yaml_data['serverconfdata'] = trust_encoded

        with open(helm_file, 'w') as file:
            yaml.dump(yaml_data, file)

        print(trust_encoded)
    except Exception as e:
        print(f"Error processing truststore files {truststore_path}: {e}")

###########################for server conf data ######################
if args.s:
    file_path = os.path.join(current_path, args.s)
    print(file_path)
    try:
        with open(file_path, 'rb') as config_file:
            config_encoded = base64.b64encode(config_file.read()).decode('utf-8')

        with open(helm_file, 'r') as file:
            yaml_data = yaml.load(file)

        yaml_data['serverconfdata'] = config_encoded.strip()

        with open(helm_file, 'w') as file:
            yaml.dump(yaml_data, file)

        print(config_encoded)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")


#######################################################update barurls from file#################
if args.b:
    barfile=args.b
    with open(barfile, 'r') as bfile:
        new_values = [line.strip() for line in bfile if line.strip()]
    with open(helm_file, 'r') as file:
        yaml_data = yaml.load(file)
    yaml_data['barURL'] = new_values
    with open(helm_file, 'w') as file:
        yaml.dump(yaml_data, file)




#python update_values.py -p configurations/dev/policy/ -k configurations/dev/config/keystore/ -s configurations/dev/config/server.conf.yaml -t configurations/dev/config/truststore/ -z truststore.jks -w poloPo10 -m values.yaml -b barfileurl.txt