import random
import requests
import schedule
import time
from datetime import datetime
from openai import OpenAI

#  OpenAI API Key 
openai_client = OpenAI(api_key="My_OPENAI_API_KEY")  #I removed OpenAPI key before commiting to security purposes

#  Telegram Bot Config 
telegram_token = "7934351370:AAH5yjnens1LRfcCdxZi1ooc9MKyhomlGNM"  
chat_id = "6853531795"           

#  Prompts for AI to use 
prompts = [
    "Write a short, punchy tweet about the future of artificial intelligence.",
    "Post a fun tech fact suitable for Telegram.",
    "Write a tech tip that inspires developers.",
    "Write a futuristic thought on robotics and automation.",
    "Create a creative short message about the rise of quantum computing.",
    "Say something insightful about digital privacy in 2025.",
    "Write a tweet-style line on the power of software engineering."
]

def generate_ai_message():
    try:
        prompt = random.choice(prompts)
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a tech-savvy assistant who writes short, engaging tech insights."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=60,
            temperature=0.8,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[ERROR] AI generation failed: {e}")
        return "🤖 AI is offline. Here's a manual tech tip: Stay curious, stay building! #Tech"

def send_to_telegram(message, image_url=None):
    try:
        if image_url:
            url = f"https://api.telegram.org/bot{telegram_token}/sendPhoto"
            payload = {
                "chat_id": chat_id,
                "caption": message,
                "photo": image_url
            }
        else:
            url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
            payload = {
                "chat_id": chat_id,
                "text": message
            }

        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print(f"[{datetime.now()}] ✅ Message sent to Telegram!")
        else:
            print(f"[ERROR] Telegram error: {response.text}")
    except Exception as e:
        print(f"[ERROR] Failed to send message: {e}")

def main():
    print("🔁 Running AI Auto Poster Bot...")

    message = generate_ai_message()
    print("📝 Generated Message:", message)

    # Optional image: Replace with any image URL or set to None
    image_url = "https://picsum.photos/512"

    send_to_telegram(message, image_url=image_url)

# Runs once immediately and schedule every 24 hours
main()
schedule.every(24).hours.do(main)

print("🚀 AI Auto Poster Bot is scheduled to post daily...")

while True:
    schedule.run_pending()
    time.sleep(10)



                        # Code OutPut 
                        
# 📝 Generated Message: 🤖 AI is offline. Here's a manual tech tip: Stay curious, stay building! #Tech
# [2025-07-02 11:31:55.164832] ✅ Message sent to Telegram!
# 🚀 AI Auto Poster Bot is scheduled to post daily... 