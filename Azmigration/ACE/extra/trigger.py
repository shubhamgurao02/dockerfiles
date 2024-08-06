#piplineID
import requests
from requests.auth import HTTPBasicAuth

import base64 , json
import os
import argparse
import base64,requests

current_path = os.getcwd()
parser = argparse.ArgumentParser(description="Process and trigger pipeline.")

parser.add_argument('-u', type=str, help="azure devops username")
parser.add_argument('-t', type=str, help="azure devops token")
parser.add_argument('-p', type=str, help="azure devops pipeline name")

args = parser.parse_args()
################################variables#################
org_name="RL-Integration"
proj_name="ACE"
sec_token=args.t
username=args.u
pipeline_name=args.p
headers = {
            
            'Content-Type': 'application/json',
            }
base_url = f'https://dev.azure.com/{org_name}/{proj_name}/_apis/pipelines?api-version=7.1-preview.1'

payload = '''{
    "resources": {
        "repositories": {
            "self": {
                "refName": "refs/heads/main"
            }
        }
    },
    
}'''
response = requests.get(base_url, auth=HTTPBasicAuth(username, sec_token))
if response.status_code == 200:
    for i in response.json()['value']:
        
        if i['name'] == pipeline_name:
            
            pipelineId=i['id']
            
            run_url=f'https://dev.azure.com/{org_name}/{proj_name}/_apis/pipelines/{pipelineId}/runs?api-version=7.1-preview.1'
            run_response=requests.post(run_url,headers=headers, auth=HTTPBasicAuth(username, sec_token),data=payload)
            
            #print(run_response.json())
            if run_response.status_code == 200:
                print(f"{i['name']} Pipeline Triggered ")
            else:
                print(f"Something wrong while triggering {pipeline_name}")
    #print("File pushed successfully.")
else:
    print(f"Failed to run pipeline . Status code: {response.status_code}, Error: {response.text}")

