import requests
import json

endpoint= "http://localhost:8000/api/products/1/"

get_response= requests.get(endpoint)  #API(get api from requests called)

print(get_response.json())