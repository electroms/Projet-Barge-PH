# Replacer par le point de terminaison
endpoint = 'url_endpoint' 
# Replacer par la clef
key = 'your_key' 

# Importer les librairies
import urllib.request
import json
import os

# Connexion et injection des données
data = {
    "Inputs": {
        "WebServiceInput0":
        [
            {
                'Column1': "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE" "[1643756400] CURRENT SERVICE STATE",
                'Column2': "localhost" "localhost" "localhost" "localhost" "localhost" "localhost""localhost" "localhost" "localhost" "localhost" "localhost" "localhost" "localhost" "localhost" "localhost" "localhost" "localhost" "localhost" "localhost" "localhost" "localhost" "localhost" "localhost",
                'Column3': "Current Load" "Current Users" "HTTP, PING" "Root Partition" "SSH" "Swap Usage" "Total Processes" "Total Processes" "Total Processes" "Current Load" "Current Load" "Current Load" "Current Load" "Current Load" "Current Load" "Current Load" "Current Load" "Swap Usage" "Swap Usage" "Swap Usage" "Swap Usage" "Swap Usage",
                'Column4': "OK" "OK" "OK" "OK" "OK" "OK" "OK" "OK" "CRITICAL" "OK" "CRITICAL" "CRITICAL" "CRITICAL" "CRITICAL" "WARNING" "OK" "CRITICAL" "OK" "CRITICAL" "CRITICAL" "OK",
                'Column5': "HARD" "HARD" "HARD" "HARD" "HARD" "HARD" "HARD" "HARD" "SOFT" "SOFT" "SOFT" "SOFT" "SOFT" "HARD" "HARD" "HARD" "SOFT" "SOFT" "SOFT" "SOFT" "SOFT" "SOFT" "SOFT",
                'Column6': "OK" "OK" "OK" "OK" "OK" "OK" "OK" "OK" "OK" "OK" "OK" "OK" "OK" "OK" "OK" "OK" "OK" "OK" "OK" "OK" "OK" "OK" "OK"
            },
        ],
    },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ key)}

req = urllib.request.Request(endpoint, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    json_result = json.loads(result)
    output = json_result["Results"]["WebServiceOutput0"][0]
    print('Cluster: {}'.format(output["Assignments"]))

except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Imprimer les en-têtes pour aider au débogage
    # print(error.info())
    # print(json.loads(error.read().decode("utf8", 'ignore')))
