from flask import Flask, request
import json
import Adafruit_CharLCD as LCD
from components.lcd import print_message

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/lcd_display', methods = ['POST'])
def displayLCD():
    data = request.get_json()
    data = data['lcd_text']
    lcd  = LCD.Adafruit_CharLCDBackpack(address=0x21)
    print("in route")
    print(data)
    print_message(lcd, data)
   
    return 'data was received successfully'

if __name__ == '__main__':
    app.run(debug=True, port=5000)