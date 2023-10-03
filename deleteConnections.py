import requests
requests.packages.urllib3.disable_warnings()
import csv
from Variables import user, QS_Node

#Set up necessary headers comma separated
xrf = 'iX83QmNlvu87yyAB'
headers = {'X-Qlik-xrfkey': xrf,
"Content-Type": "application/json",
"X-Qlik-User":user}

#Set up the certificate path
cert = 'C:\qscerts\clientandkey.pem'

#create blank dict
userAccessDates = {}

#Set the endpoint URL
xrfk = '?xrfkey={}'.format(xrf)
endpoint = '/qrs/dataconnection/'
#pull analyzers
with open('connectionsToDelete.csv', newline='', encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    for row in reader:
        #print(row[2])
        id = row[0]
        url = QS_Node + endpoint + id + xrfk
        #print(url)
        lresp = requests.delete(url, headers=headers, verify=False, cert=cert)
        print(lresp)
