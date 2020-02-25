# class lcd_I2C():
#     def __init__(self):
#         # Define LCD column and row size for 16x2 LCD.
#         self.lcd_columns = 16
#         self.lcd_rows    = 2

#         # Initialize the LCD using the pins
#         self.lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)

def print_message(lcd, message):
    try:
        lcd.clear()
        # Turn backlight on
        lcd.set_backlight(0)

        lcd.message(message)

    except KeyboardInterrupt:
        # Turn the screen off
        lcd.clear()
        lcd.set_backlight(1)

def clear_lcd():
    try:
        lcd.clear()
        # Turn backlight off
        lcd.set_backlight(1)