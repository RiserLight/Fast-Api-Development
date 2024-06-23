import requests

# Define the URL
url = 'http://127.0.0.1:8000/put'

# Define the data to be sent in the request body
data = {
   "title":"Abcdef",
   "content":"content",
   "id":10,
   "name":[]
}

# Define any headers you want to include
headers = {
    'Content-Type': 'application/json'
}

# Send the PUT request
response = requests.put(url, json=data, headers=headers)

# Handle the response
if response.status_code == 200:
    print('PUT request was successful.')
    print('Response:', response.json())
else:
    print('PUT request failed with status code:', response.status_code)
    print('Response:', response.text)