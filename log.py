import os, time
import RPi.GPIO as GPIO
from datetime import datetime

RELAY1=7
RELAY2=11
RELAY3=13
RELAY4=15
CONTACT1=16
CONTACT2=18


logfile = open("/home/daniel/git/GarageWeb/static/log.txt", "a")
logfile.write(datetime.now().strftime("     Program Starting -- %m-%d-%Y -- %H:%M  -- Hello! \n"))
logfile.close()
print(datetime.now().strftime("     Program Starting -- %m-%d-%Y -- %H:%M  -- Hello! \n"))

print " Control + C to exit Program"


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(CONTACT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(CONTACT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
time.sleep(1)

TimeDoorOpened = datetime.strptime(datetime.strftime(datetime.now(), '%m-%d-%Y %H:%M:%S'),'%Y-%m-%d %H:%M:%S')  #Default Time
DoorOpenTimer = 0              #Default start status turns timer off
DoorOpenTimerMessageSent = 1   #Turn off messages until timer is started

try:
  while 1 >= 0:
    time.sleep(1)
    if DoorOpenTimer == 1:  #Door Open Timer has Started
      currentTimeDate = datetime.strptime(datetime.strftime(datetime.now(), '%m-%d-%Y %H:%M:%S'), '%m-%d-%Y %H:%M:%S')
      if (currentTimeDate - TimeDoorOpened).seconds > 900 and DoorOpenTimerMessageSent == 0:
        print "Your Garage Door has been Open for 15 minutes"
        DoorOpenTimerMessageSent = 1

    if GPIO.input(CONTACT1) == GPIO.HIGH and GPIO.input(CONTACT2) == GPIO.HIGH:  #Door Status is Unknown
      logfile = open("/home/pi/GarageWeb/static/log.txt", "a")
      logfile.write(datetime.now().strftime("%m-%d-%Y -- %H:%M:%S  -- Door Opening/Closing \n"))
      logfile.close()
      print(datetime.now().strftime("%m-%d-%Y -- %H:%M:%S  -- Door Opening/Closing \n"))
      while GPIO.input(CONTACT1) == GPIO.HIGH and GPIO.input(CONTACT2) == GPIO.HIGH:
        time.sleep(.5)
    else:
      if GPIO.input(CONTACT1) == GPIO.LOW:  #Door is Closed
      logfile = open("/home/pi/GarageWeb/static/log.txt", "a")
      logfile.write(datetime.now().strftime("%m-%d-%Y -- %H:%M:%S  -- Door Closed \n"))
      logfile.close()
      print(datetime.now().strftime("%m-%d-%Y -- %H:%M:%S  -- Door Closed"))
      DoorOpenTimer = 0

    if GPIO.input(CONTACT2) == GPIO.LOW:  #Door is Open
       logfile = open("/home/pi/GarageWeb/static/log.txt", "a")
       logfile.write(datetime.now().strftime("%m-%d-%Y -- %H:%M:%S  -- Door Open \n"))
       logfile.close()
       print(datetime.now().strftime("%m-%d-%Y -- %H:%M:%S  -- Door Open"))
       #Start Door Open Timer
       TimeDoorOpened = datetime.strptime(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
       DoorOpenTimer = 1
       DoorOpenTimerMessageSent = 0


except KeyboardInterrupt:
        logfile = open("/home/pi/GarageWeb/static/log.txt","a")
        logfile.write(datetime.now().strftime("     Log Program Shutdown -- %m-%d-%Y -- %H:%M  -- Goodbye! \n"))
        logfile.close()
        print(datetime.now().strftime("     Log Program Shutdown -- %m-%d-%Y -- %H:%M  -- Goodbye! \n"))
        GPIO.cleanup()


