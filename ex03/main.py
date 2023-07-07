import pandas as pd

#Busca e verificação de rótulos e objetos

#Serie
alunos = pd.Series({'M1':'Luca','M2':'Clara','M3':'Yannick','M4':'Juan','M5':'Milena',})

#Teste se rotulo está na serie
try_m2 = 'M2' in alunos
try_m10 = 'M10' in alunos

#Teste se valor está na Serie
try_luca = alunos.isin(['Luca'])
try_Felipe = alunos.isin(['Felipe'])

#Imprimindo se os valores e rotulos anteriores existem ou não

#rotulo
print("Teste de rótulo :")

print("O rótulo M2 existe? :", try_m2)
print("------------------------------------------")
print("O rótulo M10 existe? :", try_m10)
print("------------------------------------------")

#valor
print("Teste de valores :")

print(try_luca)
print("------------------------------------------")
print(try_Felipe)

#isin é utilizado para verificar se um ou mais valores estão na Serie


