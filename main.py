import requests
import os
from _datetime import datetime

API_KEY = os.environ.get("API_KEY_NUTRX")
API_ID = os.environ.get("API_ID_NUTRX")
SHEETY_TOKEN = os.environ.get("auth_token_sheety")

# requests to nutrituinix api
headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

body = {
    "query": input("Type which exercises you did? "),
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30

}
#Getting todays date and time
day = datetime.now()
date = day.strftime("%d/%m/%Y")
time = day.strftime("%H:%M:%S")

# destructuring data to ge the actual calories, duration in minutes and type of exercise
nutrix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=nutrix_endpoint, json=body, headers=headers)
data = response.json()["exercises"]
for item in data:
    # print(item)
    calories = item["nf_calories"]
    duration = item["duration_min"]
    exercise = item["name"].title()

# Requests to google sheet api
sheety_url = "https://api.sheety.co/645f34fd9f7a047c84c0dea0a3da19f6/myWorkouts/workouts"
body = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

sheety_payload = {
    "workout": {
        "date": "01/01/2020",
        "time": "15:00:00",
        "exercise": "Running",
        "duration": "10",
        "calories": "100",
    }
}

bearer_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

sheety_response = requests.post(url=sheety_url, json=sheety_payload, headers=bearer_headers)
print(sheety_response.text)