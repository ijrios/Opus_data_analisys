# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 ‏‎10:27:59 2022

@author: jario
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Librería de scikit_learn para regresion lineal
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RANSACRegressor
from random import seed

np.random.seed(158)
#Generamos datos aleatorios
x1 = np.random.randint(50, 100, 85)
#Le ingresamos ruido
ruido = np.random.normal(0, 20, 85)
y1 = 2 + 3 * x1 + ruido
#x = np.append(x1,1)
#y = np.append(y1,1)

lw = 2
plt.scatter(x1, y1, color='yellowgreen', marker='.',
            label='Tendencia principal')
plt.legend(loc='upper left', fontsize='x-small')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Se requiere que el arreglo este en forma de columna
x1 = x.reshape(-1,1)
y1 = y.reshape(-1,1)
lr = LinearRegression()
lr.fit(x1, y1)
# Muestre el intercepto y el coeficiente
lr.intercept_, lr.coef_
ransac = RANSACRegressor(LinearRegression())
ransac.fit(x1, y1)
# El objeto guarda los inliers
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)
# Variables que se pueden usar luego si se desea
outliers_x = x1[outlier_mask]
outliers_y = y1[outlier_mask]
line_x = np.arange(x1.min(), x1.max())[:, np.newaxis]
line_y = lr.predict(line_x)
line_y_ransac = ransac.predict(line_x)
# Muestre el intercepto y el coeficiente
ransac.estimator_.intercept_, ransac.estimator_.coef_
lw = 2
plt.scatter(x1[inlier_mask], y1[inlier_mask], color='yellowgreen', marker='.',
            label='Tendencia principal')
plt.plot(line_x, line_y, color='navy', linewidth=lw, label='Regresor lineal')
plt.plot(line_x, line_y_ransac, color='cornflowerblue', linewidth=lw,
         label='Regresor Ransac')
plt.legend(loc='upper left', fontsize='xx-small')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()