import os
from dotenv import load_dotenv

load_dotenv()


class Credentials:

    STAGE = os.getenv("STAGE")

    if STAGE == "aqa":
        LOGIN = os.getenv("AQA_LOGIN")
        PASSWORD = os.getenv("AQA_PASSWORD")
    elif STAGE == "release":
        LOGIN = ""
        PASSWORD = ""