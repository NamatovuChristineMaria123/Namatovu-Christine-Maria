# Create an account from  https://openweathermap.org/

# Use API key from https://home.openweathermap.org/users/sign_up
# Save the API key in a file named apikey.py
# API_KEY = 'your_api_key_here'

# We should be able to retrive the API key from this file in .csv format for Climatic forecast for 30 days


# Define the API endpoint
# url = f"https://pro.openweathermap.org/data/2.5/forecast/climate?lat={lat}&lon={lon}&appid={API_KEY}"


import requests
import pandas as pd  # type: ignore


# Set your API key here
API_KEY = 'aeee9d9a475d066f100fbcaf8da302c6'

# Cordinates for the location you want to get the climatic forecast  Kampala
lat = 0.347596  # Latitude for Kampala
lon = 32.582520  # Longitude for Kampala

# Define the API endpoint
url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"


#  Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Convert the data to a DataFrame
    df = pd.DataFrame(data['list'])

    # Save the DataFrame to a CSV file
    df.to_csv('climatic_forecast.csv', index=False)

    print("Data saved to climatic_forecast.csv")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
