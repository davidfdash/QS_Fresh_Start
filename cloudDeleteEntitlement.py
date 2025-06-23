import requests
import csv
from CloudVariables import tenant_url, api_key
requests.packages.urllib3.disable_warnings()

# Set the endpoint URL
endpoint = 'api/v1/licenses/assignments/actions/delete'
url = tenant_url + endpoint
# Set up necessary headers comma separated
headers = {'Authorization': api_key}
body = {"delete": [{"type": "professional", "subject": i}]}

response = requests.post(url, headers=headers, json=body, verify=False)
print(response)
