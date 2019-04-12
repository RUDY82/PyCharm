import requests

url = "https://petstore.swagger.io/v2/pet/"

PetDic = {
  "id": 23,
  "category": {
    "id": 0,
    "name": " Bigg"
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
def GetForPet(url):
  CreatePet = requests.post(url, json = PetDic)

def UpdatesPet(url):
  Updates = requests.put(url, json = PutDic)
  print(Updates.json())

GetForPet(url)

PetRequest_byID = requests.get(url+"23")
print (PetRequest_byID.json())

UpdatesPet(url)

FindByStatus = requests.get(url + "findByStatus?status=OK")
print(FindByStatus.json())

UpdatesPet(url)


b tcx` jlby



#CreatePet = requests.post(url, json = PetDic)
#print (CreatePet.json())