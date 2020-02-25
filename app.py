from flask import Flask, request
import json
import Adafruit_CharLCD as LCD
from components.lcd import print_message, clear_lcd

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)