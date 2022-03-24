import RPi.GPIO as GPIO
import time 

def decimal2binary(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setwarnings(False)    
GPIO.setmode(GPIO.BCM)
dac = [3]
GPIO.setup(dac, GPIO.OUT)
p = GPIO.PWM(3, 1000)
p.start(0)
try:
    
    while(True):
        s = float((input("коэффициент ")))
        p.ChangeDutyCycle(s)
        print(3.3*s/100)
        
finally: 
    GPIO.output(dac, 0)
    GPIO.cleanup

