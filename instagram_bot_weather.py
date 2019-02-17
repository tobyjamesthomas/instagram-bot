from instagram_bot import InstagramBot
from weather import Weather, Unit
from os import path
import re
import json

"""
TODO:
    - Weather API not working anymore, replace with better one
"""

# Initialize InstagramBot
ig = InstagramBot()

# Get today's weather forcast
# TODO: Weather API no longer working
weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup('4118') # Toronto WOEID
forecast = location.forecast[0]
sunrise = location.astronomy['sunrise']
sunset = location.astronomy['sunset']

# Correct sunset if incorrect
# (e.g. might return "7:3 pm")
if not re.match("^[0-1]?[0-9]:[0-5][0-9] (am|pm)$", sunset):
    sunset = ":0".join(sunset.split(":"))

# Craft weather message
weather_emojis = json.load(open(path.dirname(__file__) + '/weather_emojis.json'))
report = (
        f"Weather: {forecast.text} {weather_emojis[forecast.code]}\n"
        f"🔺{forecast.high}ºC 🔻{forecast.low}ºC\n"
        f"🌅{sunrise} 🌇{sunset}"
)

# Update Instagram bio
old_bio = ig.get_bio()

try: # If old_bio has a weather report
    new_bio = old_bio.split("–")
    new_bio[1] = f"\n{report}"
    new_bio = "–".join(new_bio)
except IndexError: # If old_bio doesn't have a weather report
    new_bio = old_bio + f"\n–\n{report}"

ig.set_bio(new_bio)
ig.close()
