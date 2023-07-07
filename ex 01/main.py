import pandas as pd

#My first Exercise

notas = pd.Series([9, 2.3, 8, 9, 10])

lst_matriculas = ['m1', 'm2', 'm3', 'm4', 'm5']
lst_nomes = ['luca', 'clara', 'yannick', 'juan', 'milena']
alunos = pd.Series(lst_nomes, index=lst_matriculas)

print(notas)
print('===================')
print(alunos)