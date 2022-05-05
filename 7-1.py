import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setwarnings(False) 

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)


def decimal2binary(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    value = 0
    for i in range(len(dac)):
        GPIO.output(dac[i], 1)
        time.sleep(0.007)
        
        if (GPIO.input(comp) == 0):
            GPIO.output(dac[i], 0)

        else:
            value += (1<<(7-i))
    GPIO.output(dac, 0)
    return(value)
        

def show_voltage(value):
    GPIO.output(leds, decimal2binary(value))


try:
    voltage_results = []
    voltage_ADC = []
    start_time = time.time()
    GPIO.output(troyka, 1)
    current_voltage = adc()
    while current_voltage < 0.97*256:
        show_voltage(current_voltage)
        print(current_voltage, "{:.2f}V".format(current_voltage/256*3.3))
        voltage_ADC.append(current_voltage)
        voltage_results.append(current_voltage/256*3.3)
        current_voltage = adc()

    current_voltage = adc()
    GPIO.output(troyka, 0)
    while current_voltage > 0.02*256:
        show_voltage(current_voltage)
        print(current_voltage, "{:.2f}V".format(current_voltage/256*3.3))
        voltage_ADC.append(current_voltage)
        voltage_results.append(current_voltage/256*3.3)
        current_voltage = adc()
    end_time = time.time()

    experiment_time = end_time - start_time

    plt.plot(voltage_results)
    plt.show()


    with open("data(voltage).txt", 'w') as dataV:
        dataV.write('\n'.join([str(item) for item in voltage_results]))
    
    with open("data(ADC).txt", 'w') as dataA:
        dataA.write('\n'.join([str(item) for item in voltage_ADC]))

    with open("settings.txt", 'w') as settings:
        settings.write("{:.3f} \n".format(experiment_time/len(voltage_results)))
        settings.write("{:.3f}".format(3.3/256))

    print("Время эксперимента: ", str(experiment_time))
    print("Период одного измерения: {:.2f}".format(experiment_time/len(voltage_results)))
    print("Средняя частота дискретизации: {:.2f}".format(len(voltage_results)/experiment_time))
    print("шаг квантования АЦП: {:.2f}V".format(3.3/256))

finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
