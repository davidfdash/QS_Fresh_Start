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
    if i['removedExternally'] == True:
        #print([i['userId'], i['inactive'], i['id']])
        removedExternally.append([i['userId'], i['removedExternally'], i['id']])
print(removedExternally)

#Set the endpoint URL
endpoint = '/qrs/user/'
#pull analyzers

for i in removedExternally:
    #print(row[2])
    id = i[2]
    url = QS_Node + endpoint + id + xrfk
    #print(url)
    lresp = requests.delete(url, headers=headers, verify=False, cert=cert)
    print(lresp)

