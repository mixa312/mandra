import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
A = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.setwarnings(False)    
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def decimal2binary(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]
def adc():
    GPIO.output(dac, 0)
    for i in range(8):
        GPIO.output(dac[i], 1)
        A[i] = 1
        time.sleep(0.01)
        if (GPIO.input(comp) == 0):
            GPIO.output(dac[i], 0)
            A[i] = 0
    A.reverse()
    v = 0
    for i in range(8):
        v += A[i]*(2**i)
    return v
        


try: 
    while True:
        v = adc()
        print(v, " ", v*3.3/256)
finally: 
    GPIO.output(dac, 0)
    GPIO.cleanup
