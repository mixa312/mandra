import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setwarnings(False)    
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def decimal2binary(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]
def adc():
    for i in range(256):
        GPIO.output(dac, decimal2binary(i))
        time.sleep(0.007)
        
        if (GPIO.input(comp) == 0):
            return(i)
            break
        return(0)
        


try: 
    while True:
        v = adc()
        volt = 3.3*v/256
        print(v, " ", volt)
finally: 
    GPIO.output(dac, 0)
    GPIO.cleanup








