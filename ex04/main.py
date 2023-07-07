import pandas as pd

#Adicionando, excluindo e modificando elementos de Series

#Serie
alunos = pd.Series({'M1':'Luca','M2':'Clara','M3':'Yannick','M4':'Juan','M5':'Milena',})

#Imprimindo a Serie original
print("Original:")
print(alunos)
print('---------------------------------')

#Insere um valor e rótulo
alunos['M6'] = 'Carlos'

#Modificação de valores
alunos['M1'] = 'Luca Battesini'
alunos[['M2', 'M3']] = ['Clara Verena','Yannick Pepe']

#Removendo valores
alunos = alunos.drop('M4')

#Imprimindo a nova Serie
print("Serie após alterações")
print(alunos)

