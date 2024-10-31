import requests
import csv
from Variables import user, QS_Node

requests.packages.urllib3.disable_warnings()

#Set up necessary headers comma separated
xrf = 'iX83QmNlvu87yyAB'
headers = {'X-Qlik-Xrfkey': xrf,
"Content-Type": "application/json",
"X-Qlik-User":user}
params = {"userselection": "3e342e4e-b412-4701-a52a-1e9c20e984be"}

#Set up the certificate path
cert = 'C:\\qscerts\\clientandkey.pem'

#Set the endpoint URL
endpoint = '/qrs/user/ownedresources'
xrfk = '?xrfkey={}'.format(xrf)
url = QS_Node + endpoint + xrfk
print(url)
#inactiveUsers = []
resp = requests.get(url, headers=headers, params=params, verify=False, cert=cert)
print(resp)
for i in resp.json():
    print(i)

""" for i in resp.json():
    #print(i['inactive'])
    if i['inactive'] == True:
        #print([i['userId'], i['inactive'], i['id']])
        inactiveUsers.append([i['userId'], i['inactive'], i['id']])
#print(inactiveUsers)

#write list to csv
with open('inactiveUsers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(inactiveUsers) """