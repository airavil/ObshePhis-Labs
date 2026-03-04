import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from math import gamma, sqrt

# ЭТО ФУНКЦИЯ НЕПРИЯТНОГО ВИДА ДЛЯ РАСЧЕТА ФАКТОРИАЛА БЕЗ СПЕЦИАЛЬНЫХ БИБЛИОТЕК
def factorial(array):
    return np.array([gamma(val+1) for val in array])

# НАС ИНТЕРЕСУЕТ ТОЛЬКО ФУНКЦИЯ С РАСПРЕДЕЛЕНИЕМ ПУАССОНА
def poisson(n, expected): # Expected -- это аргумент, задающий мат.ожидания распределения
    return expected ** n / factorial(n) * np.exp(-expected)

def sigma (b):
    a=b**2
    return(sqrt(np.mean(a)-(np.mean(b))**2))

rez = pd.read_excel(r"C:\Users\ksp-t\Documents\Лабы общефиз\без чуда 1.1.4\Результаты 1.1.4 без чуда.xlsx")
np_data = np.array(rez['rezi'])
npdata = np.array(rez['rezi'])
npdatar = np.array(rez['rezi'])
reshaped_data = np.reshape(np_data, (-1, 10))
sum_data = np.sum(reshaped_data, 1)
resdata = np.reshape(npdata, (-1, 20))
sdata = np.sum(resdata, 1)
resdatar = np.reshape(npdatar, (-1, 80))
sdatar = np.sum(resdatar, 1)

a=np.sort(pd.unique(sdatar))
print(a)
print(f'колличество {len(a)}')
print(f'srednee {np.mean(sdatar)}')
for i in a:
    arr = (sdatar == i)
    print(f'n = {i}, N = {np.count_nonzero(arr)}')

print(sigma(np_data))
print(sigma(sum_data))
print(sigma(sdata))
print(sigma(sdatar))