import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from math import gamma

# ЭТО ФУНКЦИЯ НЕПРИЯТНОГО ВИДА ДЛЯ РАСЧЕТА ФАКТОРИАЛА БЕЗ СПЕЦИАЛЬНЫХ БИБЛИОТЕК
def factorial(array):
    return np.array([gamma(val+1) for val in array])

# НАС ИНТЕРЕСУЕТ ТОЛЬКО ФУНКЦИЯ С РАСПРЕДЕЛЕНИЕМ ПУАССОНА
def poisson(n, expected): # Expected -- это аргумент, задающий мат.ожидания распределения
    return expected ** n / factorial(n) * np.exp(-expected)

rez = pd.read_excel(r"C:\Users\ksp-t\Documents\Лабы общефиз\Чудесная 1.1.4\Результаты 1.1.4 с чудом.xlsx")
np_data = np.array(rez['rezi'])
npdata = np.array(rez['rezi'])
npdatar = np.array(rez['rezi'])
reshaped_data = np.reshape(np_data, (-1, 10))
sum_data = np.sum(reshaped_data, 1)
resdata = np.reshape(npdata, (-1, 20))
sdata = np.sum(resdata, 1)
resdatar = np.reshape(npdatar, (-1, 40))
sdatar = np.sum(resdatar, 1)

x_1 = np.arange(0, 100, 0.1) # Создадим массив значений от 0 до 50 с шагом в 0.1
expected_value = np.mean(rez['rezi'])

y_1 = poisson(x_1, expected_value)

x_10 = np.arange(0, 100, 0.1) # Создадим массив значений от 0 до 50 с шагом в 0.1
expected_value = np.mean(sum_data)

y_10 = poisson(x_10, expected_value)

x_20 = np.arange(0, 100, 0.1) # Создадим массив значений от 0 до 50 с шагом в 0.1
expected_value = np.mean(sdata)

y_20 = poisson(x_20, expected_value)

x_80 = np.arange(0, 130, 0.1) # Создадим массив значений от 0 до 50 с шагом в 0.1
expected_value = np.mean(sdatar)

y_80 = poisson(x_80, expected_value)



plt.hist(rez['rezi'], bins=range(0, 130, 1), label='Geiger data, 1 sec', density=True)
plt.hist(sum_data, bins=range(0, 130, 1), label='Geiger data, 10 sec', density=True)
plt.hist(sdata, bins=range(0, 130, 1), label='Geiger data, 20 sec', density=True)
plt.hist(sdatar, bins=range(0, 130, 1), label='Geiger data, 40 sec', density=True)
plt.plot(x_1, y_1, label='Poisson distribution for 1 sec')
plt.plot(x_10, y_10, label='Poisson distribution for 10 sec')
plt.plot(x_20, y_20, label='Poisson distribution for 20 sec')
plt.plot(x_80, y_80, label='Poisson distribution for 40 sec')

plt.xlabel('Число отсчетов')
plt.ylabel('Доля случаев')

plt.legend()

plt.show()


plt.hist(rez['rezi'], bins=range(0, 130, 1), label='Geiger data, 1 sec', density=True)
plt.hist(sum_data, bins=range(0, 130, 1), label='Geiger data, 10 sec', density=True)
plt.hist(sdata, bins=range(0, 130, 1), label='Geiger data, 20 sec', density=True)
plt.hist(sdatar, bins=range(0, 130, 1), label='Geiger data, 40 sec', density=True)
plt.xlabel('Число отсчетов')
plt.ylabel('Доля случаев')

plt.legend()

plt.show()