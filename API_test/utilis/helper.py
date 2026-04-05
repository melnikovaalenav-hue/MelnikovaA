import json
import allure
import requests
from pydantic import BaseModel

class Helper:

    def attach_response(self, response):
        result = json.dumps(response, indent=4)
        allure.attach(
            body=result,
            name="API Response",
            attachment_type=allure.attachment_type.JSON
        )

    def validate_response(self,
        response: requests.Response,
        model=type[BaseModel],
        status_code: int = 200,
        expected_success:bool = True
    ):
        self.attach_response(response.json())
        if expected_success:
            assert response.status_code == status_code, response.json()
            if isinstance(response.json(), dict):
                return model(**response.json())
            elif isinstance(response.json(), list):
                return [model(**item) for item in response.json()]
        else:
            assert response.status_code != 200, response.json()



