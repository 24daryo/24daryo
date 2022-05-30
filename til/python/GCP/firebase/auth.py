# -*- coding: utf-8 -*-
import os

import requests
from dotenv import load_dotenv

load_dotenv()

FIREBASE_DOMAIN = 'https://identitytoolkit.googleapis.com/v1'
API_KEY = os.getenv('FIREBASE_API_KEY')  # See here: https://console.firebase.google.com/u/2/project/aihubble/settings/general?hl=ja


class FirebaseAuth:

    @classmethod
    def verifyPassword(cls, email: str, password: str):
        URI = f"{FIREBASE_DOMAIN}/accounts:signInWithPassword?key={API_KEY}"
        data = {"email": email, "password": password, "returnSecureToken": True}
        result = requests.post(url=URI, data=data)
        if result.status_code != 200:
            return result.json()
        else:
            return result.json()


EMAIL = 'test001@example.com'
PASSWORD = 'password'
item = FirebaseAuth.verifyPassword(EMAIL, PASSWORD)
print(item)
