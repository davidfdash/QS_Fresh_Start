import requests
import csv
from Variables import user, QS_Node, cert
import os

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
#print(resp.json()[0])
for i in resp.json():
    #print(i['inactive'])
    if i['removedExternally'] == True:
        #print([i['userId'], i['inactive'], i['id']])
        removedExternally.append([i['userId'], i['removedExternally'], i['id'], i['userDirectory'], i['userDirectory'] + '\\' + i['userId']])
# print(removedExternally)
#print(removedExternally[0])
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
#print(tasks[0])
filename = ""
summary = [['User Id', 'ID', 'Object Count']]
#objects = [['User Id', 'ID', 'Name', 'Type', 'Published', 'Name']]
os.makedirs('ObjectOutput', exist_ok=True)
for n in removedExternally:
    counter = 0
    objects = [['User Id', 'ID', 'Name', 'Type', 'Published', 'Name']]
    # search APPS
    for i in apps:
        if i['owner']['id'] == n[2] and i['published'] is True:
            objects.append([i['owner']['userId'], i['id'], i['name'], 'App', i['published'], i['name']])
            counter += 1

    # search sheets
    for i in sheets:
        if i['owner']['id'] == n[2] and i['published'] is True and i['objectType'] == 'sheet':
            objects.append([i['owner']['userId'], i['id'], i['app']['name'], i['objectType'], i['published'], i['name']])
            counter += 1

    # search connections
    for i in connections:
        if i['owner']['id'] == n[2]:
            objects.append([i['owner']['userId'], i['id'], i['name'], 'Data Connection', 'N/A', i['name']])
            counter += 1

    # search extensions
    for i in extensions:
        if i['owner']['id'] == n[2]:
            objects.append([i['owner']['userId'], i['id'], i['name'], 'Extension', 'N/A', i['name']])
            counter += 1

    # search tasks
    for i in tasks:
        if i['modifiedByUserName'] == n[4]:
            objects.append([i['modifiedByUserName'], i['id'], i['name'], 'Task', 'N/A', i['name']])
            counter += 1
    print(counter)
#    print(objects)
    filename = n[2] + '.csv'
    path = "ObjectOutput/" + filename
    summary.append([n[0], n[2], counter])
    #if len(objects) > 1:
    if counter > 0:
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(objects)
print(summary)
with open('ObjectOutput/summary.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(summary)

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
