# Env file - (dotenv)
# how to store your password and username in the framework
# pip install python-dotenv

from dotenv import load_dotenv
import os
def test_login():
    load_dotenv()
    username = os.getenv("username")
    password = os.getenv("password")
    print(username,password)