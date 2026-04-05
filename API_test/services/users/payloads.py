import faker
from faker import Faker
fake = Faker()


class Payload:

    def create_user(self,
                   id: int = fake.random_number(digits=5, fix_len=True),
                   name: str = fake.first_name(),
                   status: str = "available"):
        return {
                "id": id,
                "category": {
                    "id": id,
                    "name": name
                },
                "name": name,
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": id,
                        "name": name
                    }
                ],
                "status": status
        }