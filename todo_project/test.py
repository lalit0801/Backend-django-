
import requests
import json

reqUrl = "http://localhost:8000/update/"

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "Content-Type": "application/json" 
}

payload = json.dumps({"id":1,"title":"abc","description":"this is updated description","status":True})

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

print(response.text)
