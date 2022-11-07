from flask import Flask, render_template
import requests
import json
import tweepy
import time
from time import localtime, strftime

auth= tweepy.OAuthHandler("r8Ga8u2MtuFydRoiN0ib7wwyR","M1805AttQMpOMMHLeO7gK5hIHBMhwNtwc5kmEovPcxnPsfdtyv")
auth.set_access_token("1074029183360208896-PdzZvB6UzFUOi4rxt2NqhnvwG0axzW","yERTH1WSoI3orJ6ytImAZ1ec4R0BgLd2NAbTIvEYcpvuV")

api = tweepy.API(auth, wait_on_rate_limit=True)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_weather", methods = ["GET"])
def get_weather():
    url = "https://api.openweathermap.org/data/2.5/weather?q=Alajuela&units=metric&appid=92b759db4a8570cd8089d3d6e5be6da9"
    while True:
        response = json.loads(requests.request("GET", url).text)

        information = {}
        information["city"] = response["name"]
        information["temp"] = response["main"]["temp"]
        information["icon"] = response["weather"][0]["icon"]
        information["description"] = response["weather"][0]["description"]
        information["humidity"] = response["main"]["humidity"]
        information["speed"] = response["wind"]["speed"]

        try:
            api.update_status("Weather in {}: {}°C, Humidity: {}%, Wind speed: {}km/h #salvandoRedes2022IC {}".format(information["city"], information["temp"], information["humidity"], information["speed"], strftime("%d-%m-%Y %H:%M:%S", localtime())))
        except Exception as error:
            print(error)
        time.sleep(600)

app.run()