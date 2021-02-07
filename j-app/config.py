import os
from dotenv import load_dotenv


load_dotenv(f"{os.path.dirname(os.path.realpath(__file__))}/.env")


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
        'vZ9YVje1aU'
