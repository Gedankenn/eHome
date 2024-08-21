'''
This is the main file for the LCD display.

Author: Fabio Slika Stella
date: 2024-08-06

'''

# Importing the necessary libraries
import time
import sys
import Adafruit_CharLCD as Disp

class LCD:
    '''
    This class is used to control the LCD display.

    '''

    # Parameters
    CLEAR_DISPLAY = 0x01
    RETURN_HOME = 0x02
    ENTRY_MODE_SET = 0x04
    DISPLAY_CONTROL = 0x08
    CURSOR_SHIFT = 0x10
    FUNCTION_SET = 0x20
    SET_CGRAM_ADDRESS = 0x40
    SET_DDRAM_ADDRESS = 0x80

    # Entry mode set
    ENTRY_RIGHT = 0x00
    ENTRY_LEFT = 0x02
    ENTRY_SHIFT_INCREMENT = 0x01
    ENTRY_SHIFT_DECREMENT = 0x00

    # Display control
    DISPLAY_ON = 0x04
    DISPLAY_OFF = 0x00
    CURSOR_ON = 0x02
    CURSOR_OFF = 0x00
    BLINK_ON = 0x01
    BLINK_OFF = 0x00

    # Cursor shift
    DISPLAY_MOVE = 0x08
    CURSOR_MOVE = 0x00
    MOVE_RIGHT = 0x04
    MOVE_LEFT = 0x00

    # Function set
    DATA_LENGTH_8 = 0x10
    DATA_LENGTH_4 = 0x00
    DISPLAY_LINES_2 = 0x08
    DISPLAY_LINES_1 = 0x00
    FONT_5X10 = 0x04
    FONT_5X8 = 0x00


    # Initialization
    def __init__(self, pin_rs='P8_8', pin_e='P8_10', pins_db=['P8_18', 'P8_16', 'P8_14', 'P8_12']):
        self.pin_rs = pin_rs
        self.pin_e = pin_e
        self.pins_db = pins_db

        # Setting up the GPIO pins
        try:
            self.lcd = Disp.Adafruit_CharLCD(pin_rs, pin_e, pins_db[0], pins_db[1], pins_db[2], pins_db[3], 16, 2)
        except Exception as e:
            print("Error setting up the GPIO pins.")
            print(e)
            sys.exit(1)
       
    def message(self, data):
        '''
        This method writes data to the display.

        '''
        
        # Writing the data
        self.lcd.message(data)

    def write(self, data):
        '''
        This method writes data to the display.

        '''

        # Writing the data
        self.lcd.message(str(data))

    def clear(self):
        '''
        This method clears the display.

        '''

        self.lcd.clear()

    def home(self):
        '''
        This method returns the cursor to the home position.

        '''

        self.lcd.home()

    def set_cursor(self, row, col):
        '''
        This method sets the cursor position.

        '''

        # Setting the cursor position
        if row == 0:
            address = col
        else:
            address = 0x40 + col

        self.write(self.SET_DDRAM_ADDRESS | address)
