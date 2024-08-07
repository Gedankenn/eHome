'''
This is the main file for the ehome project. It will be the file that is run to start the program.

Author: Fabio Slika Stella
date: 2024-08-06

'''

# Importing the necessary libraries
import sys
import os
import time
import lcd as LCD


def main():
    '''
    This is the main function of the program.
    '''
    # Creating the LCD object
    lcd = LCD.LCD()
    
    # Clearing the display
    lcd.clear()

    # Displaying the welcome message
    lcd.write_message("Welcome to ehome!")
    time.sleep(2)

