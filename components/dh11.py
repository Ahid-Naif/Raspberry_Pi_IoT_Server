import sys
import Adafruit_DHT

# set type of the sensor
sensor = 11
# set pin number
pin = 4

def measure_humidity_temperature():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        return humidity, temperature
    else:
        print("Error in reading humidity or temperature or both!")
        return 0, 0