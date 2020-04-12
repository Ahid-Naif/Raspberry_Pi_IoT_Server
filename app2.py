import requests
import time
from components.ultrasonic import measure_distance
from components.dh11 import measure_humidity_temperature

url = "https://thawing-crag-91038.herokuapp.com/sensors_readings"

while True:
    distance = measure_distance()
    humidity, temperature = measure_humidity_temperature()

    data = {'distance'   : distance,
            'humidity'   : humidity,
            'temperature': temperature
            }
    res = requests.post(url,data=data)