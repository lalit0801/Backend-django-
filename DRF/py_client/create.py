import requests

endpoint= "http://localhost:8000/api/products/"

data={
    "title":"this field is done",
}

get_response= requests.post(endpoint, json=data)  #API(get api from requests called)
print(get_response.json())