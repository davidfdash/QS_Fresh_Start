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
cert = 'C:\\qscerts\\clientandkey.pem'

# Set the endpoint URL
xrfk = '?xrfkey={}'.format(xrf)
endpoint = '/qrs/custompropertydefinition/'
url = QS_Node + endpoint + xrfk
lresp = requests.get(url, headers=headers, verify=False, cert=cert)
#print(lresp)
for i in lresp:
    print(i)

