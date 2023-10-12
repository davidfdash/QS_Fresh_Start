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
endpoint = '/qrs/custompropertydefinition/'

#what custom property id?
custPropId = str(input("Enter custom property id: "))
#get /custompropertydefinition/{id} json
url = QS_Node + endpoint + custPropId + xrfk
response = requests.get(url, headers=headers, verify=False, cert=cert)
print('Get request response: ' + str(response))
custProp = json.loads(response.text)
#extract "choiceValues" as list
choiceValuesList = (custProp['choiceValues'])
#open csv as list with choiceValues to remove and remove list items from choiceValues list
with open('removeChoiceValues.csv', newline='', encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    for row in reader:
        value = row[0]
        if value in choiceValuesList:
            choiceValuesList.remove(value)
#put choiceValues back in json
(custProp['choiceValues']) = choiceValuesList
#put /custompropertydefinition/{id}
r = requests.put(url, headers=headers, verify=False, cert=cert, data=json.dumps(custProp))
print('Put request response: ' + str(r))