import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "https://127.0.0.1:8000/"


get_response = requests.get(endpoint) #HTTP requests
print(get_response.text) #print our response on text format
print(get_response.status_code)
# print(get_response.json())