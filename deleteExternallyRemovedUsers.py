import requests
import csv
from Variables import user, QS_Node, cert

requests.packages.urllib3.disable_warnings()

#Set up necessary headers comma separated
xrf = 'iX83QmNlvu87yyAB'
headers = {'X-Qlik-xrfkey': xrf,
"Content-Type": "application/json",
"X-Qlik-User":user}

#Set the endpoint URL
endpoint = '/qrs/user/full'
xrfk = '?xrfkey={}'.format(xrf)
url = QS_Node + endpoint + xrfk
#print(url)
removedExternally = []
resp = requests.get(url, headers=headers, verify=False, cert=cert)
for i in resp.json():
    #print(i['inactive'])
    #if i['removedExternally'] == True:
        #print([i['userId'], i['inactive'], i['id']])
    removedExternally.append([i['userId'], i['removedExternally'], i['id'], i['userDirectory']])
#print(removedExternally)

for i in removedExternally:
    objects = []
    counter = 0
    # GET SHEETS
    # Set the endpoint URL
    xrfk = '?xrfkey={}'.format(xrf)
    endpoint = '/qrs/app/object/full'
    url = QS_Node + endpoint + xrfk
    lresp = requests.get(url, headers=headers, verify=False, cert=cert)

    for i in lresp.json():
        if i['owner']['id'] == removedExternally['id'] and i['published'] is True and i['objectType'] == 'sheet':
            objects.append(
                [i['owner']['userId'], i['id'], i['app']['name'], i['objectType'], i['published'], i['name']])
    #        counter += 1
# GET APPS
# Set the endpoint URL
xrfk = '?xrfkey={}'.format(xrf)
endpoint = '/qrs/app/full'
url = QS_Node + endpoint + xrfk
aresp = requests.get(url, headers=headers, verify=False, cert=cert)
apps = aresp.json()

#GET SHEETS
# Set the endpoint URL
xrfk = '?xrfkey={}'.format(xrf)
endpoint = '/qrs/app/object/full'
url = QS_Node + endpoint + xrfk
lresp = requests.get(url, headers=headers, verify=False, cert=cert)
sheets = lresp.json()

# GET Dataconnections
# Set the endpoint URL
xrfk = '?xrfkey={}'.format(xrf)
endpoint = '/qrs/dataconnection/full'
url = QS_Node + endpoint + xrfk
lresp = requests.get(url, headers=headers, verify=False, cert=cert)
connections = lresp.json()

# GET Extensions
# Set the endpoint URL
xrfk = '?xrfkey={}'.format(xrf)
endpoint = '/qrs/extension/full'
url = QS_Node + endpoint + xrfk
lresp = requests.get(url, headers=headers, verify=False, cert=cert)
extensions = lresp.json()

# GET Tasks
# Set the endpoint URL
xrfk = '?xrfkey={}'.format(xrf)
endpoint = '/qrs/task/full'
url = QS_Node + endpoint + xrfk
lresp = requests.get(url, headers=headers, verify=False, cert=cert)
tasks = lresp.json()

# search APPS
for i in apps:
    if i['owner']['id'] == userid and i['published'] is True:
        objects.append([i['owner']['userId'], i['id'], i['name'], 'App', i['published'], i['name']])
#        counter += 1

# search sheets
for i in sheets:
    if i['owner']['id'] == userid and i['published'] is True and i['objectType'] == 'sheet':
        objects.append([i['owner']['userId'], i['id'], i['app']['name'], i['objectType'], i['published'], i['name']])

# search connections
for i in connections:
    if i['owner']['id'] == userid:
        objects.append([i['owner']['userId'], i['id'], i['name'], 'Data Connection', 'N/A', i['name']])

# search extensions
for i in extensions:
    if i['owner']['id'] == userid:
        objects.append([i['owner']['userId'], i['id'], i['name'], 'Extension', 'N/A', i['name']])

# search tasks
for i in tasks:
    if i['owner']['id'] == userid:
        objects.append([i['modifiedByUserName'], i['id'], i['name'], 'Task', 'N/A', i['name']])

print(objects)
filename =
with open('objects.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(objects)

#Set the endpoint URL
#endpoint = '/qrs/user/'

#for i in removedExternally:
#    #print(row[2])
#    id = i[2]
#    url = QS_Node + endpoint + id + xrfk
#    #print(url)
#    lresp = requests.delete(url, headers=headers, verify=False, cert=cert)
#    i.append(lresp)
#    print(lresp)

#write list to csv and add "userDirectory"
#with open('removedUsers.csv', 'w', newline='') as f:
#    writer = csv.writer(f)
#    writer.writerows(removedExternally)
