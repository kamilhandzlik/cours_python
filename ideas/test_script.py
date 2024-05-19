import  requests
import time

response = requests.post("http://127.0.0.1:5000/token", json={"username":"admin", "password":"1234"})
response_json = response.json()

access_token = response_json["access_token"]
refresh_token = response_json["refresh_token"]

items_response= requests.get("http://127.0.0.1:5000", headers={"Authorization": f"Bearer {access_token}"})

print(items_response.json())