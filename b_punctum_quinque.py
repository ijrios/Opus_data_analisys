# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 22:49:17 2022

@author: jario
"""
import random
import pandas as pd
import matplotlib.pyplot as plt

experimenta = int(input("Intra numerum experimentorum: "))
experimenta_matrix = []
experimenta_nomen = []

for x in range(0,experimenta):
    
    globals()['experimentum%s' % x]  = 0
    globals()['matrix%s' % x] = []
    #i = len(matrix)
    folium = 0
    while folium <= 299:
        numerus = random.randint(1, 300)
        print('Numerus ' + str(numerus))
        
        if numerus not in globals()['matrix%s' % x]:
            globals()['matrix%s' % x].append(numerus)
            folium = folium + 1
            globals()['experimentum%s' % x] = globals()['experimentum%s' % x] + 1
            print("Folium est ingressus")
        
        elif numerus in globals()['matrix%s' % x]:
            folium = folium
            globals()['experimentum%s' % x] = globals()['experimentum%s' % x] + 1
            print("Non intravit, iam exstat")
    
    experimenta_matrix.append(globals()['experimentum%s' % x])
    experimenta_nomen.append('fact'+str(x))
    print("Experimentorum numero: " + str(x) + "Totalis numerus foliorum: " + str(globals()['experimentum%s' % x]) ) 
    print(globals()['matrix%s' % x])
    #print(experimenta_nomen)

#------------- Graphics ---------------------------------
x_valorem = experimenta_nomen
y_valorem = experimenta_matrix
    
plt.bar(x_valorem, y_valorem) #Graphic
plt.title('Experimenta - Totalis numerus foliorum implere album ') #Titulus 
ax = plt.subplot() #Axis 
ax.set_xticks(x_valorem) #Axis x 
ax.set_xticklabels(x_valorem) #Label axis x
ax.set_ylabel('Totalis numerus foliorum') #Nomen axis Y
ax.set_xlabel('Experiementa numerus') #Nomen axis X 

# ---------- Statistics Data ---------------------------
experimenta_h = pd.DataFrame()
experimenta_h['Experimenta'] = experimenta_nomen
experimenta_h['Totalis numerus foliorum'] = experimenta_matrix
experimentae = experimenta_h['Totalis numerus foliorum']
experimenta_h.set_index('Experimenta', inplace=True)

nomen = [i for i in range(len(experimenta_nomen))]

# ------------- Creating histogram ---------------------
#plt.bar(experimentae, height=nomen)
#plt.xticks(experimentae, experimenta_nomen);
#experiementa_h.hist()

experimentus = pd.DataFrame()
experimentus['Nomen'] = experimenta_nomen
experimentus['Totalis'] = experimenta_matrix
#experimentus.set_index(experimentus['Nomen'],inplace=True)
experimentus.head(33)

experimentus.hist()
experimenta_h.describe()

