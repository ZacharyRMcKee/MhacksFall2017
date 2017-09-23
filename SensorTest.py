#Brett and Zach
#MHacksX Fall 2017 sensor project

import RPi.GPIO as GPIO
import time
#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)

while True:
    i=GPIO.input(11) #Sets i to the input of the sensor (0 = low, 1 = high)
    if i==0:
        print("Detected Nothing")
        time.sleep(0.4)
    elif i==1:
        print("Detected Something")
        time.sleep(0.4)
