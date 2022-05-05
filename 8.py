import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data(ADC).txt", dtype=int)
settings = np.loadtxt('settings.txt', dtype=float)
voltage = data/256*3.3
t = []
for i in range(len(voltage)):
    t.append(settings[0]*(i+1))
print(voltage)
box = {'facecolor':'blue'}
fig, ax = plt.subplots()
time1 = t[np.argmax(voltage)]
time2 = max(t) - time1
print(time1)
ax.plot(t, voltage, 'o', ls = '-', markevery = 100, color = 'indigo', linewidth = 1)
ax.set(xlim=(0, 1.05*max(t)), ylim = (0, 1.05*max(voltage)))
ax.text(0.5, 0.5, 'время зарядки = '+ str(time1) +', время разрядки '+ str(time2) + '', bbox = box, color = 'white')
ax.set_xlabel('время, с')
ax.set_ylabel('Напряжение, В')
ax.minorticks_on()#включаем второстепенные деленя осей
ax.grid(which = 'minor', linestyle = ':', color = 'black')
ax.grid(which = 'major', linestyle = ':', color = 'black')
ax.set_title('Процесс заряда и разряда в RC-цепочке', loc = 'left', wrap = True)
plt.show()
fig.savefig('fig.png')