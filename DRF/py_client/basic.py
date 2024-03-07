import requests

# endpoint="https://httpbin.org/status/200/"
# endpoint= "https://httpbin.org/anything"
endpoint= "http://localhost:8000/api/home"

get_response= requests.get(endpoint,json={"product_id":123})  #API(get api from requests called)
# print(get_response.text) #print raw response text
# print(get_response.status_code)

#http request-> html
# REST API http request -> JSON(~python dictionary)
print(get_response.json())
