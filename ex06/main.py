import pandas as pd
import numpy as np

#Operações aritmédicas com Series

#Series
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
print("Series originais:")
print("s1: ");print(s1)
print("s2 :");print(s2)

#Operações
#Multiplicação ou divisão
print(":):):):):):):):):):):):):):):):):):):):):):)")
print("multiplicação:")
print(s1 * s2) #Troque o sinal "*" por "/" para divisão

#Soma ou subtração
print(":):):):):):):):):):):):):):):):):):):):):):)")
print("Soma:")
print(s1 + s2) #Troque o sinal de "+" por "-" para subtração

#Raiz quadrada (Utilizando a biblioteca "Numpy")
print(":):):):):):):):):):):):):):):):):):):):):):)")
print("Raiz quadrada:")
print(np.sqrt(s1))

#As operações entre Series são sempre executadas por pares de elementos
# que ocupam a mesma posição. 