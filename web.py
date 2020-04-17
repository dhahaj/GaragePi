import time
from datetime import datetime
from flask import Flask, render_template, request

RELAY1=7
RELAY2=11
RELAY3=13
RELAY4=15
CONTACT1=16
CONTACT2=18

CODE='5626'

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)  # the pin numbers refer to the board connector not the chip
GPIO.setwarnings(False)

GPIO.setup(CONTACT1, GPIO.IN, GPIO.PUD_UP) # set up pin ?? (one of the above listed pins) as an input with a pull-up resistor
GPIO.setup(CONTACT2, GPIO.IN, GPIO.PUD_UP) # set up pin ?? (one of the above listed pins) as an input with a pull-up resistor

GPIO.setup(RELAY1, GPIO.OUT)
GPIO.output(RELAY1, GPIO.HIGH)
GPIO.setup(RELAY2, GPIO.OUT)
GPIO.output(RELAY2, GPIO.HIGH)
GPIO.setup(RELAY3, GPIO.OUT)
GPIO.output(RELAY3, GPIO.HIGH)
GPIO.setup(RELAY4, GPIO.OUT)
GPIO.output(RELAY4, GPIO.HIGH)




app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
        if GPIO.input(CONTACT1) == GPIO.HIGH and GPIO.input(CONTACT2) == GPIO.HIGH:
             print("Garage is Opening/Closing")
             return app.send_static_file('Question.html')
        else:  
             if GPIO.input(CONTACT1) == GPIO.LOW:
                   print ("Garage is Closed")
                   return app.send_static_file('Closed.html')
             if GPIO.input(CONTACT2) == GPIO.LOW:
                   print ("Garage is Open")
                   return app.send_static_file('Open.html')


@app.route('/Garage', methods=['GET', 'POST'])
def Garage():
        name = request.form['garagecode']
        if name == CODE:                     # 12345678 is the Password that Opens Garage Door (Code if Password is Correct)
                GPIO.output(RELAY1, GPIO.LOW)
                time.sleep(1)
                GPIO.output(RELAY1, GPIO.HIGH)
                time.sleep(2)

                if GPIO.input(CONTACT1) == GPIO.HIGH and GPIO.input(CONTACT2) == GPIO.HIGH:
                  print("Garage is Opening/Closing")
                  return app.send_static_file('Question.html')
                else:
                  if GPIO.input(CONTACT1) == GPIO.LOW:
                        print ("Garage is Closed")
                        return app.send_static_file('Closed.html')
                  if GPIO.input(CONTACT2) == GPIO.LOW:
                        print ("Garage is Open")
                        return app.send_static_file('Open.html')

        if name != CODE:  # 12345678 is the Password that Opens Garage Door (Code if Password is Incorrect)
                if name == "":
                        name = "NULL"
                print("Garage Code Entered: " + name)
                if GPIO.input(CONTACT1) == GPIO.HIGH and GPIO.input(CONTACT2) == GPIO.HIGH:
                  print("Garage is Opening/Closing")
                  return app.send_static_file('Question.html')
                else:
                  if GPIO.input(CONTACT1) == GPIO.LOW:
                        print ("Garage is Closed")
                        return app.send_static_file('Closed.html')
                  if GPIO.input(CONTACT2) == GPIO.LOW:
                        print ("Garage is Open")
                        return app.send_static_file('Open.html')


@app.route('/stylesheet.css')
def stylesheet():
        return app.send_static_file('stylesheet.css')

@app.route('/Log')
def logfile():
        return app.send_static_file('log.txt')

@app.route('/images/<picture>')
def images(picture):
        return app.send_static_file('images/' + picture)

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)


