import requests
import csv
from Variables import user, QS_Node
requests.packages.urllib3.disable_warnings()


# Set up necessary headers comma separated
xrf = 'davedavedavedave'
headers = {'X-Qlik-xrfkey': xrf,
           "Content-Type": "application/json",
           "X-Qlik-User": user}

# Set up the certificate path
cert = 'C:\\qscerts\\clientandkey.pem'

userid = '3e342e4e-b412-4701-a52a-1e9c20e984be'
objects = []
counter = 0
#GET SHEETS
# Set the endpoint URL
xrfk = '?xrfkey={}'.format(xrf)
endpoint = '/qrs/app/object/full'
url = QS_Node + endpoint + xrfk
lresp = requests.get(url, headers=headers, verify=False, cert=cert)

for i in lresp.json():
    if i['owner']['id'] == userid and i['published'] is True and i['objectType'] == 'sheet':
        objects.append([i['owner']['userId'], i['id'], i['app']['name'], i['objectType'], i['published'], i['name']])
#        counter += 1
#GET APPS
# Set the endpoint URL
xrfk = '?xrfkey={}'.format(xrf)
endpoint = '/qrs/app/full'
url = QS_Node + endpoint + xrfk
aresp = requests.get(url, headers=headers, verify=False, cert=cert)
#print(aresp.json())
for i in aresp.json():
    if i['owner']['id'] == userid and i['published'] is True:
        objects.append([i['owner']['userId'], i['id'], i['name'], 'App', i['published'], i['name']])
#        counter += 1

#GET Dataconnections
# Set the endpoint URL
xrfk = '?xrfkey={}'.format(xrf)
endpoint = '/qrs/dataconnection/full'
url = QS_Node + endpoint + xrfk
lresp = requests.get(url, headers=headers, verify=False, cert=cert)

for i in lresp.json():
    if i['owner']['id'] == userid:
        objects.append([i['owner']['userId'], i['id'], i['name'], 'Data Connection', 'N/A', i['name']])


print(objects)

with open('objects.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(objects)
#print(counter)
