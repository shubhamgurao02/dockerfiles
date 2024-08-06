import argparse
import base64
import os
import requests
from requests.auth import HTTPBasicAuth
import json
import subprocess
from subprocess import Popen, PIPE
########################################
organization_url = "https://dev.azure.com/RL-Integration/"
project_name = "ACE"

##########################################
current_path = os.getcwd()
parser = argparse.ArgumentParser(description="Process and encode files/folders in base64.")
parser.add_argument('-u', type=str, help="username to connect to azure devops")
parser.add_argument('-t', type=str, help="azure devops PAT tokken to connect")
parser.add_argument('-f', type=str, help="file path of pipeline names and bar file names")
parser.add_argument('-n', type=str, help="file path of bar url file ")

args = parser.parse_args()
if args.u and args.f and args.t and args.n:
    barfile=args.n
    group_file_name=args.f
    group_file=open(group_file_name,'r')
    group_file=group_file.readlines()
    username=args.u
    pat = args.t
    headers = {
        'Content-Type': 'application/json'
    }
    pipelines_url = f"{organization_url}/{project_name}/_apis/build/builds?api-version=7.1-preview.7"
    response = requests.get(pipelines_url, auth = HTTPBasicAuth(username,pat))
    #print(response )
    if response.status_code == 200:
        pipelines = response.json()
        for io in group_file:
        #print(io.split())
            file_name=io.split()[0].strip()
            p1=io.split()[1].strip()
            for pipeline in pipelines['value']:
                build_id = pipeline['id']
  #      print("build_id",build_id)
                try:
                    pipeline_name = pipeline["definition"]['name']
            #print(pipeline_name)
                except:
                    pass
                if pipeline_name == p1:
                    #print("build_id",build_id)
                    #print(pipeline_name)

                    fileid_url=f"{organization_url}/{project_name}/_apis/build/builds/{build_id}/artifacts?artifactName=output&api-version=7.1-preview.5"
                    runs_response = requests.get(fileid_url, auth = HTTPBasicAuth(username,pat))
                    if runs_response.status_code == 200:
                        pipeline_runs = runs_response.json()
                        file_id=pipeline_runs['resource']['data']
                    blobid_url=f"{organization_url}/{project_name}/_apis/build/builds/{build_id}/artifacts?artifactName=output&fileId={file_id}&fileName={file_name}&api-version=7.1-preview.5"
                    try:
                        blob_response = requests.get(blobid_url, auth = HTTPBasicAuth("sgurao","sk4fngxkmuau5gtmujw7yf6punzpm74jgt35ghpeivwqnugzqvmq"))
                        bid=blob_response.json()['items'][0]['blob']['id']
                        blobid_url=f"{organization_url}/{project_name}/_apis/build/builds/{build_id}/artifacts?artifactName=output&fileId={bid}&fileName={file_name}&api-version=7.1-preview.5"
                        #print(pipeline_name, file_name ,  blobid_url)
                        with open(barfile, 'a') as barurl:
                            barurl.write(blobid_url + '\n')
                    except:
                        pass
                    break



#######################################User guide #############################
#python barurls.py -f names.txt -t token -u sgurao -n /home/baru.txt
# -f -- for file path which contains name of barfile name and pipelines names it should be same format as mentioned 
# -u -- username of azure devops account
# -t -- token of azure devops account
# -n -- barurl file name where it will get stored to file
