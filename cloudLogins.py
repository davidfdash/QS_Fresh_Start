import requests
import csv
import json
from CloudVariables import tenant_url, api_key
requests.packages.urllib3.disable_warnings()

#get list of users logged in in last 90 days
# Set up necessary headers comma separated
headers = {'Authorization': api_key}

#limit per page
params = {
    "limit": 100
}
endpoint = 'api/v1/audits?eventType=com.qlik.user-session.begin'
url = tenant_url + endpoint

all_data = []
while url != 'None':
    response = requests.get(url, headers=headers, params=params, verify=False)
    data = response.json()
    for i in data["data"]:
        if i['data']["subject"] not in all_data:
            all_data.append(i['data']["subject"])
    url = data["links"].get('next', {}).get('href', 'None')
print(all_data)