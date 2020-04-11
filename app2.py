import time
from components.ultrasonic import measure_distance

while True:
    distance = measure_distance()