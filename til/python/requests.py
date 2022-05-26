import requests

# file upload
URL = 'http://localhost:3000/upload'
FILE = {'file': open('test.xlsx', 'rb')}
res = requests.post(URL, files=FILE)

# json send
URL = 'http://localhost:8000/json'
ITEM = {'mydata': "トークンです"}
res = requests.post(URL, json=ITEM)
