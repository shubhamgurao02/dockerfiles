from ruamel.yaml import YAML
import os
import argparse
import base64,requests

yaml = YAML()
current_path = os.getcwd()
parser = argparse.ArgumentParser(description="Process and encode files/folders in base64.")
parser.add_argument('-c', type=str, help="Path to file which contains file need to be push azure repose")
parser.add_argument('-b', type=str, help="build id")
parser.add_argument('-f', type=str, help="Path to chart file ")
#parser.add_argument('-u', type=str, help="azure devops username")
parser.add_argument('-p', type=str, help="azure devops token")
parser.add_argument('-r', type=str, help="azure devops repose name")

args = parser.parse_args()
################################variables#################
org_name="RL-Integration"
proj_name="ACE"
sec_token=args.p
azrepo_name=args.r
if args.f and args.b:
    buidlid=args.b
    config_file=args.f
    file_name = os.path.join(current_path, config_file)
    with open(file_name, 'r') as file:
        chart = yaml.load(file)
    version=chart['version']
    chart_version=version.split('.')
    patch_version=int(chart_version[2])
    min_version=int(chart_version[1])
    maj_version=int(chart_version[0])
    if patch_version == 100 and min_version < 50 :
        min_version+=1
        patch_version=0
    if  min_version == 50 :
        maj_version+=1
        min_version=0
        patch_version=0
    
    if patch_version == 0 and (0 <= min_version <= 50):
        patch_version+=1
    new_version=f"{maj_version}.{min_version}.{patch_version}"
    chart['version'] = new_version

    with open(file_name, 'w') as file:
        yaml.dump(chart, file)

    l1=chart["appVersion"].split('.')
    l1.pop(2)
    l1.append(buidlid)
    chart['appVersion'] = '.'.join(map(str,l1))
    with open(file_name, 'w') as file:
        yaml.dump(chart, file)
    
    

if args.c:
    con_file=args.c 
    fname=os.path.join(current_path, con_file)
    with open(fname, 'r') as file:
        file=file.readlines()
    print(file)
    cleaned_list = [filename.strip() for filename in file]
    print(cleaned_list)
    for i in cleaned_list:
        print(i)
        push_file=os.path.join(current_path, i)
        try:
            with open(push_file, "rb") as tempfile:
                file_content = tempfile.read()
        except FileNotFoundError:
                print(f"Error: File not found at {push_file}")
                #return

        url = f'https://dev.azure.com/{org_name}/{proj_name}/_apis/git/repositories/{azrepo_name}/commits?searchCriteria.itemVersion.versionType=branch&searchCriteria.itemVersion.version=main&$top=1&api-version=6.1'

        headers = {
        'Authorization': 'Basic ' + base64.b64encode(bytes(f':{sec_token}', 'ascii')).decode('ascii'),
        'Content-Type': 'application/json',
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            commits_data = response.json()
            latest_commit_id = commits_data['value'][0]['commitId']  # Assuming the latest commit is at index 0
            print(f"Latest commit ID: {latest_commit_id}")

        else:
            print(f"Failed to retrieve commits. Status code: {response.status_code}")
        commit_message="updated [skip ci]"    
        push_body = {
            "refUpdates": [
            {
                "name": f"refs/heads/main",
                "oldObjectId": latest_commit_id
            }
            ],
            "commits": [
            {
                "comment": commit_message,
                "changes": [
                    {
                        "changeType": "edit",
                        "item": {
                            "path": i ,  # Use only the filename
                            # "content": base64.b64encode(file_content).decode('ascii'),
                            # 'contentType': 'base64encoded'#file_content.decode('utf-8')  # Convert binary data to string for display
                        } ,
                        'newContent': {
                            "content": base64.b64encode(file_content).decode('ascii'),
                            'contentType': 'base64encoded'#file_content.decode('utf-8')  # Convert binary data to string for display
                            }
                    }
                ]
            }
            ]
            }
        headers = {
            'Authorization': 'Basic ' + base64.b64encode(bytes(f':{sec_token}', 'ascii')).decode('ascii'),
            'Content-Type': 'application/json',
            }
        base_url = f'https://dev.azure.com/{org_name}/{proj_name}/_apis/git/repositories/{azrepo_name}/pushes?api-version=6.1'

        response = requests.post(base_url, headers=headers, json=push_body)

        if response.status_code == 201:
            print("File pushed successfully.")
        else:
            print(f"Failed to push file. Status code: {response.status_code}, Error: {response.text}")

    
