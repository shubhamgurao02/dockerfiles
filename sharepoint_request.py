import requests

# Set the SharePoint site URL
site_url = "https://prolificscorporationltd.sharepoint.com"

# Set the Azure AD tenant ID, client ID, and client secret
tenant_id = "ef03601c-2e22-4313-adbf-9ff5407825e1"
client_id = "4068bd66-344d-4acf-8680-42e4b20a27fc"
client_secret = "v5SumcKdqvt2o73hcZbBzhECed/l4LnpWyP6thWlElc="

# Set the resource URL for SharePoint API
resource_url = site_url + "/_api/web"
tenant="/Documents"
# Define the token endpoint URL
token_url = f"https://accounts.accesscontrol.windows.net/{tenant_id}/tokens/OAuth/2"
resource=f"00000003-0000-0ff1-ce00-000000000000/{site_url}@{tenant_id}"
#token_url=token_url1.format(tenant_id)
print(token_url)
# Prepare the payload for token request
payload = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "resource": resource
    
}

# Send the token request
response = requests.post(token_url, data=payload)
print(response)
# Check if the request was successful
if response.status_code == 200:
    # Extract the access token from the response
    access_token = response.json()["access_token"]
    print("Access token:", access_token)
else:
    print("Failed to obtain access token")
