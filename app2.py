import requests
import time
from components.ultrasonic import measure_distance

url = "https://thawing-crag-91038.herokuapp.com/distance"

while True:
    distance = measure_distance()

    data = {'distance':distance}
    res = requests.post(url,data=data)

    time.sleep(1)