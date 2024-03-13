import requests
import json

url = "https://na.lodestonenews.com/news/maintenance/current"
payload = {}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)

#get the next FFXIV Main Server Maintenance
def getMaintStatus():
    maintenanceList = response.json()
    currentGameMaint = maintenanceList['game']
    return(len(currentGameMaint))

def getMaintURL():
    maintenanceList = response.json()
    currentGameMaint = maintenanceList['game'][0]['url']
    return(currentGameMaint)
