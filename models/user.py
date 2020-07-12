#!/usr/bin/python3
''' manage class user '''
from models.base_model import BaseModel


class User(BaseModel):
    email = ''
    password = ''
    first_name = ''
    last_name = ''
