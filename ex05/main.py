import pandas as pd
import numpy as np

#computação vetorizada

#Percorrendo elementos de Series

#Series
alunos = pd.Series({'M1':'Luca','M2':'Clara','M3':'Yannick','M4':'Juan','M5':'Milena',})

#Percorre os dados
for aluno in alunos: print (aluno)
#Percorre os rotulos
for indice in alunos.index: print(indice)

