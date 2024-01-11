#Exercise exercise app with google sheets



#From nutritionix API

import datetime
import requests
import json
from dotenv import load_dotenv
import os

#Environmental variables
load_dotenv(".env")
api_key: str =os.getenv("API_KEY")
app_id:str =os.getenv("APP_ID")
app_user: str =os.getenv("APP_USER")


input = input("What exercise you did today?: ")

#Nutrinionix API
Url = "https://trackapi.nutritionix.com/v2/natural/exercise"

params = {
    "query": input
}

headers={
    "x-app-id": app_id,
    "x-app-key": api_key,
}

res=requests.post(Url, json=params, headers=headers)
data = json.loads(res.text)


#Sheety API

sheety_api =f"https://api.sheety.co/{app_user}/workoutTracking/workouts"

#extract from exercise
exercise= data["exercises"][0]["user_input"]
duration=data["exercises"][0]["duration_min"]
calories=data["exercises"][0]["nf_calories"]

#Date and Time
today =datetime.datetime.now()
date= today.strftime("%d/%m/%Y")
time= today.strftime("%H:%M:%S")


body= {
    "workout" : {
    "date": date,
    "time":time,
    "exercise": exercise.title(),
    "duration": duration,
    "calories": calories,
}}
print(body["workout"])

sheet_response = requests.post(url=sheety_api, json=body)
print(sheet_response.text)

