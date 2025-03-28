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
cert = 'C:\qscerts\clientandkey.pem'

# Set the endpoint URL
xrfk = '?xrfkey={}'.format(xrf)
endpoint = '/qrs/app/object/'
# pull analyzers
with open('objectsToDelete.csv', newline='', encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    for row in reader:
        # print(row[2])
        id = row[0]
        print(id)
        url = QS_Node + endpoint + id + xrfk
        print(url)
        lresp = requests.delete(url, headers=headers, verify=False, cert=cert)
        print(lresp)
