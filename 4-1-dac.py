import RPi.GPIO as GPIO
import time 

def decimal2binary(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setwarnings(False)    
GPIO.setmode(GPIO.BCM)
dac = [24, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
try:
    while(True):
        number = input("введите число ")
        if number == "q":
            break
        elif number.isdigit() == False: 
            print("вводимое значение содержит не число")
        elif float(number) % 1 != 0: 
            print("Не целое число")
            continue
        elif int(number) > 255:
            print("число превышает возможности 8-разрядного ЦАП")
            continue
        
        elif int(number) < 0: 
            print("число отрицательное")
            continue
        else:
            print("значение напряжения на выходе ЦАП " + str(int(number) * 3.3/255)) 
            number = decimal2binary(int(number))
            GPIO.output(dac, number)
        

finally: 
    GPIO.output(dac, 0)
    GPIO.cleanup

