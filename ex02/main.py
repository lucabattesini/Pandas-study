import pandas as pd

#Imprimindo propriedades e nomeando vetores e rótulos

#Serie
alunos = pd.Series({'M1':'Luca','M2':'Clara','M3':'Yannick','M4':'Juan','M5':'Milena',})

#Adiciona um nome a vetores
alunos.name = "alunos"
#Adiciona nome para rotulos
alunos.index.name = "matrículas"

#Imprime a variavel alunos
print(alunos)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
#criando as variaveis com as propriedades
tamanho = alunos.size #calculando o número de elementos
dados = alunos.values #Vetor de dados(Nome dos alunos)
rotulos = alunos.index #Vetor de rotulos(Matriculas)
alunos_tipo = type(alunos)
alunos_dtype = alunos.dtype
alunos_idx_dtype = alunos.index.dtype

#Imprimindo os valores

print('Número de elementos:', tamanho)
print('Vetor de dados:', dados)
print('Vetor de rótulos:', rotulos)
print('tipo:', alunos_tipo)
print('dtype da Serie:', alunos_dtype)
print('Dtype do vetor de rótulos:', alunos_idx_dtype)


#Data types:
#values : vetor de dados;
#index : vetor de rótulos;
#name : nome do vetor de dados;
#size : tamanho da Series (número de elementos);
#index.name : nome do vetor de rótulos;
#index.dtype : dtype do vetor de rótulos.