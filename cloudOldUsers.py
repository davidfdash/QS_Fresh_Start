import requests
import json
from CloudVariables import tenant_url, api_key
requests.packages.urllib3.disable_warnings()


# Set up necessary headers comma separated
headers = {'Authorization': api_key}

# get list of all users
endpoint = 'api/v1/users/'
url = tenant_url + endpoint
#print(url)

resp = requests.get(url, headers=headers, verify=False)
#print(resp)
allUserData = resp.json()
allUsers = []
for i in allUserData["data"]:
    allUsers.append(i['subject'])
#print(allUsers)

# get list of users logged in in last 90 days
# Set up necessary headers comma separated
headers = {'Authorization': api_key}

# limit per page
params = {
    "limit": 100
}
endpoint = 'api/v1/audits?eventType=com.qlik.user-session.begin'
url = tenant_url + endpoint

currentUsers = []
while url != 'None':
    response = requests.get(url, headers=headers, params=params, verify=False)
    data = response.json()
    for i in data["data"]:
        if i['data']["subject"] not in currentUsers:
            currentUsers.append(i['data']["subject"])
    url = data["links"].get('next', {}).get('href', 'None')
#print(currentUsers)

# check all user list against current user list to find inactive users
inactiveUsers = []
for i in allUsers:
    if i not in currentUsers:
        inactiveUsers.append(i)
print(inactiveUsers)

# deallocate licenses from Qlik Cloud inactive users
endpoint = 'api/v1/licenses/assignments/actions/delete'
url = tenant_url + endpoint

for i in inactiveUsers:
    body = {"delete": [{"type": "professional", "subject": i}]}
    response = requests.post(url, headers=headers, json=body, verify=False)
    print(response, i)
    body = {"delete": [{"type": "analyzer", "subject": i}]}
    response = requests.post(url, headers=headers, json=body, verify=False)
    print(response, i)
