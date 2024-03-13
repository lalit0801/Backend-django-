import requests
import json

# endpoint="https://httpbin.org/status/200/"
# endpoint= "https://httpbin.org/anything"
endpoint= "http://localhost:8000/api/"



params = {"product_id": 123}
get_response= requests.post(endpoint, json={"title":" hello world!!"})  #API(get api from requests called)
# print(get_response.text) #print raw response text
# print(get_response.status_code)

#http request-> html
# REST API http request -> JSON(~python dictionary)
print(get_response.json())
