import pandas as pd

#Estatisticas de colunas e linhas de um Data Frame
notas = pd.DataFrame({"A1":[9.8, 7.2, 8.0],
                      "A2": [5.3, 4.0, 3.5],
                      "A3": [5.5, 8.1, 7.2],
                      "A4": [7.0, 7.5, 6.5]}, 
index=["P1","P2","P3"])

#Imprimindo o Data Frame
print(notas)
print("=============================================")

print("Media dos alunos")
print(notas.mean())
print("=============================================")

print("Maior nota de cada aluno")
print(notas.max())
print("=============================================")

print("Media de cada prova")
print(notas.mean(axis=1))
print("=============================================")

print("Maior nota de cada prova")
print(notas.max(axis=1))
print("=============================================")
