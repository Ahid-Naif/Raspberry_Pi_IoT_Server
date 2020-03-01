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

def clear_lcd(lcd):
    lcd.clear()
    # Turn backlight off
    lcd.set_backlight(1)