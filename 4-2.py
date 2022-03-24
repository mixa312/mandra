import RPi.GPIO as GPIO
import time 

def decimal2binary(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setwarnings(False)    
GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
try:
    Per = int(input())
    t = Per/510
    while(True):
        for i in range(255):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(t)
        for i in range(255, 0, -1):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(t)

finally: 
    GPIO.output(dac, 0)
    GPIO.cleanup

