# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 22:49:17 2022

@author: jario
"""

import random
import matplotlib.pyplot as plt

        
def Random():
    numerus = random.randint(1, 300)
    print('Numerus ' + str(numerus))
    
def main():
    
    experimenta_matrix = []
    experimenta_nomen = []

    experimenta = int(input("Intra numerum experimentorum: "))
    for x in range(0,experimenta):
        
        globals()['experimentum%s' % x]  = 0
        globals()['matrix%s' % x] = []
        #i = len(matrix)
        folium = 0
        while folium <= 299:
            
            alef = Random()
            
            if alef not in globals()['matrix%s' % x]:
                globals()['matrix%s' % x].append(alef)
                folium = folium + 1
                globals()['experimentum%s' % x] = globals()['experimentum%s' % x] + 1
                print("Folium est ingressus")
            
            elif alef in globals()['matrix%s' % x]:
                folium = folium
                globals()['experimentum%s' % x] = globals()['experimentum%s' % x] + 1
                print("Non intravit, iam exstat")
        
        experimenta_matrix.append(globals()['experimentum%s' % x])
        experimenta_nomen.append('fact'+str(x))
        print("Experimentorum numero: " + str(x) + "Totalis numerus foliorum: " + str(globals()['experimentum%s' % x]) ) 
        print(globals()['matrix%s' % x])
        #print(experimenta_nomen)
        
        x_valorem = experimenta_nomen
        y_valorem = experimenta_matrix
        
        plt.bar(x_valorem, y_valorem) #El gráfico 
        plt.title('Experimenta - Totalis numerus foliorum implere album ') #El título 
        ax = plt.subplot() #Axis 
        ax.set_xticks(x_valorem) #Eje x 
        ax.set_xticklabels(x_valorem) #Etiquetas del eje x 
        ax.set_ylabel('Totalis numerus foliorum') #Nombre del eje y
        ax.set_xlabel('Experiementa numerus') #Nombre del eje x
       
main()

