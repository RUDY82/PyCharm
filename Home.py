import requests

url = "http://testapi.novaposhta.ua/v2.0/json/Address/searchSettlements/"

NPdoK = {
"apiKey": "[ВАШ КЛЮЧ]",
 "modelName": "Address",
    "calledMethod": "searchSettlements",
    "methodProperties": {
        "CityName": "київ",
        "Limit": 5
    }
}

Request_NP = requests.post(url, json = NPdoK )
#Respons = requests.post(url)
print(Request_NP.json())