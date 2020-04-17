print " Control + C to exit Program"

import time

RELAY1=7
RELAY2=11
RELAY3=13
RELAY4=14

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)         # the pin numbers refer to the board connector not the chip
GPIO.setwarnings(False)
GPIO.setup(RELAY1, GPIO.OUT)     # sets the pin input/output setting to OUT
GPIO.output(RELAY1, GPIO.HIGH)   # sets the pin output to high
GPIO.setup(RELAY2, GPIO.OUT)
GPIO.output(RELAY2, GPIO.HIGH)
GPIO.setup(RELAY3, GPIO.OUT)
GPIO.output(RELAY3, GPIO.HIGH)
GPIO.setup(RELAY4, GPIO.OUT)
GPIO.output(RELAY4, GPIO.HIGH)


try:
  while 1 >=0:
    GPIO.output(RELAY1, GPIO.LOW)   # turns the first relay switch ON
    time.sleep(.5)                  # pauses system for 1/2 second
    GPIO.output(RELAY1, GPIO.HIGH)  # turns the first relay switch OFF
    GPIO.output(RELAY2, GPIO.LOW)   # turns the second relay switch ON
    time.sleep(.5)
    GPIO.output(RELAY2, GPIO.HIGH)
    GPIO.output(RELAY3, GPIO.LOW)
    time.sleep(.5)
    GPIO.output(RELAY3, GPIO.HIGH)
    GPIO.output(RELAY4, GPIO.LOW)
    time.sleep(.5)
    GPIO.output(RELAY4, GPIO.HIGH)
    time.sleep(.5)
except KeyboardInterrupt:      # Stops program when "Control + C" is entered
  GPIO.cleanup()               # Turns OFF all relay switches
