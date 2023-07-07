import pandas as pd

notas = pd.Series([9, 2.3, 8, 9, 10])

lst_matriculas = ['m1', 'm2', 'm3', 'm4', 'm5']
lst_nomes = ['luca', 'clara', 'yannick', 'juan', 'milena']
alunos = pd.Series(lst_nomes, index=lst_matriculas)

print(notas)
print('===================')
print(alunos)

#Data types:
#values : vetor de dados;
#index : vetor de rótulos;
#name : nome do vetor de dados;
#size : tamanho da Series (número de elementos);
#index.name : nome do vetor de rótulos;
#index.dtype : dtype do vetor de rótulos.