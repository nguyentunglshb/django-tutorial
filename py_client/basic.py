import requests

# endpoint = "https://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/test"

get_response = requests.get(endpoint, params={
    "abc": 123
}, json={
    "query": "hello world"
})
print(get_response.json())
