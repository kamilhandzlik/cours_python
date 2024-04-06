import requests

data = {"username":"Jan",
        "email": "jankowalski@example.com",
        "phoneNumber":123456789}

response =requests.post("http://127.0.0.1:5002", json=data)