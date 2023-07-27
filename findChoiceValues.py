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
endpoint = '/qrs/custompropertydefinition/full'
xrfk = '?xrfkey={}'.format(xrf)
url = QS_Node + endpoint + xrfk
#print(url)
choiceValues = []
resp = requests.get(url, headers=headers, verify=False, cert=cert)
for i in resp.json():
    #print(i['inactive'])
    #print([i['userId'], i['inactive'], i['id']])
    choiceValues.append([i['id'], i['name'], i['choiceValues']])
#print(inactiveUsers)

#write list to csv
with open('choiceValues.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(choiceValues)