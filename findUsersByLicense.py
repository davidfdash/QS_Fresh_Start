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

#Set the endpoint URL
xrfk = '?xrfkey={}'.format(xrf)

#create blank list
userAccessDates = []

#check for analyzers
endpoint = '/qrs/license/analyzeraccesstype/count'
url = QS_Node + endpoint + xrfk

countresp = requests.get(url, headers=headers, verify=False, cert=cert)
if (countresp.json().get('value')) > 0:
    #pull analyzers
    endpoint = '/qrs/license/analyzeraccesstype/full'
    url = QS_Node + endpoint + xrfk
    lresp = requests.get(url, headers=headers, verify=False, cert=cert)
    # add analyzer users to list
    for lic in lresp.json():
        #print('{} {}'.format(lic['user']['userId'], lic['lastUsed']))
        userAccessDates.append([[lic['user']['userId']], lic['lastUsed'],[lic['user']['id']]])

# check for professionals
endpoint = '/qrs/license/professionalaccesstype/count'
url = QS_Node + endpoint + xrfk

countresp = requests.get(url, headers=headers, verify=False, cert=cert)
if (countresp.json().get('value')) > 0:
    #pull professional users
    endpoint = '/qrs/license/professionalaccesstype/full'
    url = QS_Node + endpoint + xrfk
    lresp = requests.get(url, headers=headers, verify=False, cert=cert)
    #add professional users to list
    for lic in lresp.json():
        #print('{} {}'.format(lic['user']['userId'], lic['lastUsed']))
        userAccessDates.append([[lic['user']['userId']], lic['lastUsed'],[lic['user']['id']]])

# check for tokens
endpoint = '/qrs/license/useraccesstype/count'
url = QS_Node + endpoint + xrfk

countresp = requests.get(url, headers=headers, verify=False, cert=cert)
if (countresp.json().get('value')) > 0:
    #pull token users
    endpoint = '/qrs/license/useraccesstype/full'
    url = QS_Node + endpoint + xrfk
    lresp = requests.get(url, headers=headers, verify=False, cert=cert)
    #add token users to list
    for lic in lresp.json():
        #print('{} {}'.format(lic['user']['userId'], lic['lastUsed']))
        userAccessDates.append([[lic['user']['userId']], lic['lastUsed'],[lic['user']['id']]])

#write list to csv
with open('userAccessDateslist.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(userAccessDates)