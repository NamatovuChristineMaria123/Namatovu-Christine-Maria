
#POST means create 
import requests
# Example of a POST request to create a new resource
url = "https://jsonplaceholder.typicode.com/posts"  
data = {
    'title':'foo',
    'id': 1,
    'body':'bar',
    'userId':1
}
response = requests.post(url, json=data)
print(f"Status Code: {response.status_code}")
print('Response JSON:', response.json())