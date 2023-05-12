import numpy as np
import pandas as pd
data = np.loadtxt('minutes_n_ingredients.csv',dtype=int,delimiter=',')
print(data[:5])
print(np.mean(data[:,[1]]))#среднее значение второго столбца
print(np.mean(data[:,[2]]))#среднее значение третьего столбца
print(data.min(axis=0)[1:])#минимальные значения второго и третьего столбцов
print(data.max(axis=0)[1:])#максимальные значения второго и третьего столбцов
print(np.median(data,axis=0)[1:])#медианы второго и третьего столбцов
print("\n")
print(len(np.unique(data[:,[0]])))#сколько уникальных рецептов находится в датасете.
print(len(np.unique(data[:,[2]])),np.unique(data[:,[2]]))#Сколько и каких различных значений кол-ва ингредиентов присутвует в рецептах из датасета

#щшйвьшауцщ
