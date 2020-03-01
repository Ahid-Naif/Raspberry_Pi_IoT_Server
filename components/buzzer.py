import RPi.GPIO as GPIO

buzzer_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

def buzzer_on(status):
    # Make buzzer sound
    GPIO.output(buzzer_pin, GPIO.HIGH)

def buzzer_off(status):
    # Stop buzzer sound
    GPIO.output(buzzer_pin, GPIO.LOW)