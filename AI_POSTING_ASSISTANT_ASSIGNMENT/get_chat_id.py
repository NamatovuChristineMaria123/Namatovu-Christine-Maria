import requests

bot_token = "7934351370:AAH5yjnens1LRfcCdxZi1ooc9MKyhomlGNM"  # Your bot token here

url = f"https://api.telegram.org/bot{bot_token}/getUpdates"

response = requests.get(url)
print(response.json())
