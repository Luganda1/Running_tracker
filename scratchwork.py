import requests
from datetime import datetime



pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "JK5FB!SLF37ASFhC'M?AS3DNF"
USERNAME = "tonny88"
GRAPH_ID = "id1"

#GETTING STARTED WITH PIXELA
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(f"response code: {response.text}")
# print("tonny")

#using the post() to create our graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "miles",
    "type": "float",
    "color": "ajisai",
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


#using the post() to post data into the graph

date = datetime.now()
print(date.strftime("%Y%m%d"))

# https://pixe.la/v1/users/a-know/graphs/test-graph
value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

value_params = {
    "date": date.strftime("%Y%m%d"),
    "quantity": input("How many miles did you run today? ")
}

response_values = requests.post(url=value_endpoint, json=value_params, headers=headers)
print(response_values.text)


#using the put() method to update the our pixela
date = datetime(year=2021, month=6,day=1)
pixela_date = date.strftime("%Y%m%d")
update_pixela_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{pixela_date}"

update_params = {
    "quantity": "8.5"
}

# update_response = requests.put(url=update_pixela_endpoint, json=update_params, headers=headers)
# print(update_response.text)
#

#USING THE DELETE() METHOD TO DELETE AND ENTRY IN OUR GRAPH

delete_date = date.strftime("%Y%m%d")
delete_pixela_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{delete_date}"


# delete_response = requests.delete(url=delete_pixela_endpoint, headers=headers)
# print(delete_response.text)
#










import requests
from datetime import datetime
import os

GENDER = YOUR GENDER
WEIGHT_KG = YOUR WEIGHT
HEIGHT_CM = YOUR HEIGHT
AGE = YOUR AGE

APP_ID = os.environ["YOUR_APP_ID"]
API_KEY = os.environ["YOUR_API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["YOUR_SHEET_ENDPOINT"]

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    #No Auth
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)


    #Basic Auth
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            os.environ["USERNAME"],
            os.environ["PASSWORD"],
        )
    )

    #Bearer Token
    bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.text)

