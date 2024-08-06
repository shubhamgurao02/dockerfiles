import requests
from requests.auth import HTTPBasicAuth

organization_url = "https://dev.azure.com/RL-Integration/"
project_name = "ACE"
pipelinename=""
file_name=""
# Personal Access Token (PAT) 
username="sgurao"
pat = "yoljoyqpawy3ufu3f7xay33ff2glyo3gpskeg6jlaphplbuoy7oaa"
headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {pat}'
    }

    # Get pipelines
pipelines_url = f"{organization_url}/{project_name}/_apis/build/builds?api-version=7.1-preview.7"
response = requests.get(pipelines_url, auth = HTTPBasicAuth(username,pat))

if response.status_code == 200:
    pipelines = response.json()

for pipeline in pipelines['value']:
    build_id = pipeline['id']
    print("build_id",build_id)
    pipeline_name = pipeline['name']
    if pipeline_name == "pipelinename":
        fileid_url=f"{organization_url}/{project_name}/_apis/build/builds/{build_id}/artifacts?artifactName=output&api-version=7.1-preview.5"
        runs_response = requests.get(fileid_url, auth = HTTPBasicAuth(username,pat))

        if runs_response.status_code == 200:
            pipeline_runs = runs_response.json()
            file_id=pipeline_runs['resource']['data']
            print("file id",file_id)
        blobid_url=f"{organization_url}/{project_name}/_apis/build/builds/{build_id}/artifacts?artifactName=output&fileId=file_id&fileName={file_name}&api-version=7.1-preview.5"
        blob_response = requests.get(blobid_url, auth = HTTPBasicAuth(username,pat))
