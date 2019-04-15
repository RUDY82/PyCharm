import requests

url = "https://petstore.swagger.io/v2/pet/"

PetDic = {
  "id": 23,
  "category": {
    "id": 0,
    "name": " Bigg"
  },
  "name": "Time",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "See"
    }
  ],
  "status": "available"
}

PutDic = {
  "id": 23,
  "category": {
    "id": 0,
    "name": " WWWWW"
  },
  "name": "mmm",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "zzz"
    }
  ],
  "status": "OK"
}

PetData = {
  "id": 23,
  "category": {
    "id": 100,
    "name": "Umka"
  },
  "name": "Busya",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 111,
      "name": "Marusya"
    }
  ],
  "status": "UP"
}
def GetForPet(url):
  CreatePet = requests.post(url, json=PetDic)

def UpdatesPet(url):
  Updates = requests.put(url, json=PutDic)
  print(Updates.json())

def UpdatesFormData(url):
  UpdatesF = requests.post(url, json=PetData)

  print(UpdatesF.json())

GetForPet(url)

PetRequest_byID = requests.get(url+"23")
print(PetRequest_byID.json())

UpdatesPet(url)

FindByStatus = requests.get(url + "findByStatus?status=OK")
print(FindByStatus.json())

UpdatesFormData(url)

#CreatePet = requests.post(url, json = PetDic)
#print (CreatePet.json())

#Онлайн поиск в справочнике населенных пунктов
