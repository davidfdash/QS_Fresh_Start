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
endpoint = '/qrs/app/full'
url = QS_Node + endpoint + xrfk
lresp = requests.get(url, headers=headers, verify=False, cert=cert)
print(lresp.status_code)
# add apps to list
for lic in lresp.json():

    appReloadDates.append([lic['name'],lic['lastReloadTime'], lic['id']])
#print(appReloadDates)

#write list to csv
with open('appReloadDateslist.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(appReloadDates)