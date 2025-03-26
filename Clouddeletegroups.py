import requests
import csv
from CloudVariables import tenant_url, api_key
requests.packages.urllib3.disable_warnings()


# Set up necessary headers comma separated
headers = {'Authorization': 'Bearer: ' + api_key}

# Set the endpoint URL
endpoint = '/api/v1/groups/'
# pull analyzers
with open('groupsToDelete.csv', newline='', encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    for row in reader:
        # print(row[2])
        id = row[0]
        print(id)
        url = tenant_url + endpoint + id
        print(url)
        lresp = requests.delete(url, headers=headers, verify=False)
        print(lresp)
