# Basic get request using the requests library
import requests

response = requests.get('https://api.github.com')

# Print the status code and the JSON response
print(f"Status Code: {response.status_code}")
print('response.json();', response.json()) # Print the JSON response