from pydantic import BaseModel
from typing import Optional
from typing import List
from pydantic import TypeAdapter


#class User(BaseModel):
    #name: str
    #age: int

#Optional[str] - Поле может быть str или None
#str = None - Поле по умолчанию None, но необязательно в JSON

#json_data = {
    #"name": "Alex"
            #}


#validation = User.model_validate(json_data)
#validation_data = User(**json_data)

#print(validation.model_dump_json(indent=2))
#print(User(**json_data))

#---
#class Address(BaseModel):
    #city: str
    #zip_code: str

#class User(BaseModel):
    #name: str
    #age: int
    #address: Address  # Вложенная модель

#data = {
    #"name": "Alex",
    #"age": 41,
    #"address": {
        #"city": "Stavropol",
        #"zip_code": "33-777"
    #}
#}

#user=User(**data)
#print(user.address.zip_code)

#---
#class UserList(BaseModel):
    #users: List[User]  # Список пользователей

#data_1 = {
    #"users": [
        #{"name": "Alex", "age": 41},
        #{"name": "Yuliana", "age": 40}
    #]
#}

#user = UserList(**data_1)
#print(user.users[1].age)

#---
class User(BaseModel):
    name: str
    age: int

adapter = TypeAdapter(list[User])

users = [
    {"name": "Alex", "age": 41},
    {"name": "Yuliana", "age": 40}
]

validated_users = adapter.validate_python(users)
print(validated_users[1].name)