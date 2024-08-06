import os
from collections import defaultdict
import time
import shutil
import re
import json
import requests
import subprocess
from requests.auth import HTTPBasicAuth
from zipfile import ZipFile
h="OMSRLNA"
env="PROD"
bid={}
response = requests.get('https://dev.azure.com/Prolifics-InnovationCenter/POC/_apis/build/builds?api-version=7.0',
			auth = HTTPBasicAuth('SGurao','q3v4pxhsefzkrwzdehivnrbcdzr26rish47xgpoyxeebgjjntdiq'))
response=response.json()
#print(response['value'])
mydict={}
for i in response['value']:
    if i['definition']['name'] == "mft" :
        print(i['definition']['name'])
        print(i['definition']['id'])
