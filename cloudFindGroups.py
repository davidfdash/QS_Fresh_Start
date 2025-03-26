import requests
import csv
from CloudVariables import tenant_url, api_key
requests.packages.urllib3.disable_warnings()


# Set up necessary headers comma separated
headers = {'Authorization': api_key}

#Set the endpoint URL
endpoint = 'api/v1/groups/'
url = tenant_url + endpoint
print(url)
groups = []
resp = requests.get(url, headers=headers, verify=False)
print(resp)
for i in resp.json():
    groups.append([i['id'], i['name']])
#print(inactiveUsers)

#write list to csv
with open('groups.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(groups)