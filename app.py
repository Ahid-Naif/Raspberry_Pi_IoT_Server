from flask import Flask, request
import json
import Adafruit_CharLCD as LCD
from components.lcd import print_message, clear_lcd
from components.buzzer import buzzer_on, buzzer_off

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/lcd_display', methods = ['POST'])
def displayLCD():
    data = request.get_json()
    data = data['lcd_text']
    lcd  = LCD.Adafruit_CharLCDBackpack(address=0x21)
    print_message(lcd, data)
   
    return 'data was received successfully'

@app.route('/lcd_clear', methods = ['POST'])
def clearLCD():
    lcd  = LCD.Adafruit_CharLCDBackpack(address=0x21)
    clear_lcd(lcd)
   
    return 'LCD was cleared successfully'

@app.route('/buzzer_on', methods = ['POST'])
def buzzerON():
    data = request.get_json()
    data = data['buzzerStatus']
    buzzer_on(data)

    return 'buzzer is turned on'

@app.route('/buzzer_off', methods = ['POST'])
def buzzerOFF():
    data = request.get_json()
    data = data['buzzerStatus']
    buzzer_off(data)

    return "buzzer is turned off"

if __name__ == '__main__':
    app.run(debug=True, port=5000)