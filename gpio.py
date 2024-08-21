#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This is the GPIO class for beaglebone.

Author: Fabio Slika Stella
date: 2024-08-14

'''

# Importing the necessary libraries
from periphery import GPIO as gpio
import subprocess as sp
import sys

class GPIO:
    '''
    This class is used to control the GPIO pins.

    '''

    # Parameters
    IN = 0
    OUT = 1
    LOW = 0
    HIGH = 1

    # Initialization
    def __init__(self, pin, direction):
        self.pin = pin
        self.direction = direction
        self.devchip = get_gpiochip_from_pin(self.pin)
        self.gpio = gpio(self.devchip, self.pin, self.direction)



    def read(self):
        '''
        This function reads the pin.

        :return: The pin value.
        '''
        return self.gpio.read()

def get_gpiochip_from_pin(pin):
    '''
    This function returns the GPIO chip from the pin.

    :param pin: The pin.
    :return: The GPIO chip.
    '''
    gpiochip_infos_list = gpiochip_infos()
    for gpiochip_info in gpiochip_infos_list:
        if pin in gpiochip_info:
            index = gpiochip_infos_list.index(gpiochip_info)
            return f'gpiochip{index}'

    return None  # Return None if pin is not found

def gpiochip_infos():
    '''
    This function returns the GPIO chip infos.

    :return: The GPIO chip infos.
    '''
    gpio_list = []
    for i in range(4):  # Assuming there are 4 GPIO chips
        try:
            result = sp.run(["gpioinfo", f'gpiochip{i}'], capture_output=True, text=True, check=True)
            gpio_list.append(result.stdout)
        except sp.CalledProcessError as e:
            print(f"Error fetching gpiochip{i} info: {e}")

    return gpio_list


def main():
    '''
    This is the main function.

    '''
    if len(sys.argv) < 2:
        print('Options: ')
        print('-h get the help')
        print('-v get the version')
        print('-i <pin> get the pin info')
        print('-r <pin> read the pin')
        print('-w <pin> <value> write the pin')
        print('Usage: ./gpio.py <option> <params>')
        sys.exit(1)

    if sys.argv[1] == '-h':
        print('This is the help.')
        sys.exit(0)

    if sys.argv[1] == '-v':
        print('This is the version.')
        sys.exit(0)

    if sys.argv[1] == '-i':
        pin = sys.argv[2]
        info = get_gpiochip_from_pin(pin)
        print(info)
        sys.exit(0)

    if sys.argv[1] == '-r':
        pin = sys.argv[2]
        direction = GPIO.IN
        gpio = GPIO(pin, direction)
        print(gpio.read())
        sys.exit(0)

if __name__ == '__main__':
    main()
