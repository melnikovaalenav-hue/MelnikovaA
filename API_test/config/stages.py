import os

stages = {
    "dev": "https://petstore.swagger.io/"
}

def get_stage():
    stage_key = os.getenv("STAGE")
    return stages[stage_key]

