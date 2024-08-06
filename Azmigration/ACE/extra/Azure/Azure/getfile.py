import requests
from requests.auth import HTTPBasicAuth
import json
organization_url = "https://dev.azure.com/RL-Integration/"
project_name = "ACE"
pipelinename="DEV-OMSRLAP_SFCC2MULTISYS_OrderCreate_App"
file_name="dev-omsrlap-sfcc2multisysordercreateapp.bar"
# Personal Access Token (PAT) 
demo=open('names.txt','r')
demo=demo.readlines()

username="sgurao"
pat = "token"
#print(pipelinename)

headers = {
        'Content-Type': 'application/json'
    }

    # Get pipelines
pipelines_url = f"{organization_url}/{project_name}/_apis/build/builds?api-version=7.1-preview.7"
response = requests.get(pipelines_url, auth = HTTPBasicAuth("sgurao","token"))
#print(response )
if response.status_code == 200:
    pipelines = response.json()
    for io in demo:
        print(io)
        file_name=io.split(' ')[0]
        p1=io.split(' ')[1]
        for pipeline in pipelines['value']:
            build_id = pipeline['id']
  #      print("build_id",build_id)
            try:
                pipeline_name = pipeline["definition"]['name']
            #print(pipeline_name)
            except:
                pass

            if pipeline_name == p1:
                print("build_id",build_id)
                print(pipeline_name)

                fileid_url=f"{organization_url}/{project_name}/_apis/build/builds/{build_id}/artifacts?artifactName=output&api-version=7.1-preview.5"
                runs_response = requests.get(fileid_url, auth = HTTPBasicAuth("sgurao","token"))
                #print("Hi")
                if runs_response.status_code == 200:
                    pipeline_runs = runs_response.json()
                    file_id=pipeline_runs['resource']['data']
                    print("file id",file_id)
                blobid_url=f"{organization_url}/{project_name}/_apis/build/builds/{build_id}/artifacts?artifactName=output&fileId={file_id}&fileName={file_name}&api-version=7.1-preview.5"
                blob_response = requests.get(blobid_url, auth = HTTPBasicAuth("sgurao","token"))
                #print(blob_response.json())
                break
