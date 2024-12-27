import requests

test=requests.get("http://192.168.0.115:5000/get")
print(test.text)
requests.get("http://192.168.0.115:5000/clear")