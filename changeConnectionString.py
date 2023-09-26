import requests
requests.packages.urllib3.disable_warnings()
import csv
import json
from Variables import user, QS_Node

#Set up necessary headers comma separated
xrf = 'iX83QmNlvu87yyAB'
headers = {'X-Qlik-xrfkey': xrf,
"Content-Type": "application/json",
"X-Qlik-User":user}

#Set up the certificate path
cert = 'C:\qscerts\clientandkey.pem'

#Set the endpoint URL
xrfk = '?xrfkey={}'.format(xrf)
endpoint = '/qrs/dataconnection/'
#pull analyzers
with open('connectionsToEdit.csv', newline='', encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    for row in reader:
        #print(row[0])
        id = row[0]
        #id = '6f2fc6e7-9d56-48a7-955c-dc1bbfa61e19'
        url = QS_Node + endpoint + id + xrfk
        #print(url)
        response = requests.get(url, headers=headers, verify=False, cert=cert)
        print('Get request response: ' + str(response))
        connection = json.loads(response.text)
        connString = (connection['connectionstring'])
        newConnString = connString.replace('Apt05cnhw', 'ApP67cnhw')
        #print(newConnString)
        connection['connectionstring'] = newConnString
        #print(connection['connectionstring'])
        #print(connection)
        r = requests.put(url, headers=headers, verify=False, cert=cert, data=json.dumps(connection))
        print('Put request response: ' + str(r))
