import requests

created_dog = requests.post(
    url="https://petstore.swagger.io/v2/pet",
    headers={},
    json={
    "id": 15022026,
    "category": {
        "id": 1,
        "name": "dog"
    },
    "name": "murka",
    "photoUrls": [
        "https://petstore.swagger.io/user/createUsersWithListInput",
    ],
    "tags": [
        {
        "id": 0,
        "name": "mur-mur"
        }
    ],
    "status": "available"
    }
)

print(created_dog.text)


upd_dog_name = requests.put(
    url="https://petstore.swagger.io/v2/pet",
    headers={},
    json={
    "id": 15022026,
    "category": {
        "id": 1,
        "name": "dog"
    },
    "name": "murka_upd",
    "photoUrls": [
        "https://petstore.swagger.io/user/createUsersWithListInput",
    ],
    "tags": [
        {
        "id": 0,
        "name": "mur-mur"
        }
    ],
    "status": "available"
    }
)

print(upd_dog_name.text)

respons_status = requests.get(
    url="https://petstore.swagger.io/v2/pet/findByStatus?status=available",
    headers={},
    params={}
)

print(respons_status.json())

delete_dog = requests.delete(
    url="https://petstore.swagger.io/v2/pet/15022026",
    headers={},
    params={}
)

print(delete_dog.status_code)

respons_upd_status = requests.get(
    url="https://petstore.swagger.io/v2/pet/findByStatus?status=available",
    headers={},
    params={}
)

print(respons_upd_status.json())