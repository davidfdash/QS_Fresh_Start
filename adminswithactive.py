import json
import requests
import csv
from Variables import user, QS_Node
requests.packages.urllib3.disable_warnings()

#Set up necessary headers comma separated
xrf = 'iX83QmNlvu87yyAB'
headers = {'X-Qlik-xrfkey': xrf,
"Content-Type": "application/json",
"X-Qlik-User":user}

#Set up the certificate path
cert = 'C:\qscerts\clientandkey.pem'

#create blank dict
appReloadDates = []

#Set the endpoint URL
xrfk = '?xrfkey={}'.format(xrf)

#pull apps
endpoint = '/qrs/user/full'
url = QS_Node + endpoint + xrfk
data = requests.get(url, headers=headers, verify=False, cert=cert)


# Dictionary to store the result
result = {}

# Iterate through the JSON data
for entry in data:
    # Check if 'roles' exists and contains 'rootadmin'
    if 'roles' in entry and 'rootadmin' in entry['roles']:
        # Add userId and inactive status to the result dictionary
        result[entry['userId']] = entry['inactive']

# Print the result
print(result)
