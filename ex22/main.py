import pandas as pd

#Medidas de variabilidade
#DataFrame
dados = {'jogador': ['Luca', 'Felipe', 'Diogo', 'Carlos'],
         'infração': ['Falta', 'falta violenta', 'comportamento agrssivo', 'falta'],
         'juiz1': [1, 5, 6, 3],
         'juiz2': [3, 1, 4, 9]
}

df = pd.DataFrame(dados)

#Calculando a variabilidade
print('juiz 1')
print("amplitude:", df['juiz1'].max() - df['juiz1'].min())
print("variância:", df['juiz1'].var())
print("desvio padrão:", df['juiz1'].std())

print('juiz 2')
print("amplitude:", df['juiz2'].max() - df['juiz2'].min())
print("variância:", df['juiz2'].var())
print("desvio padrão:", df['juiz2'].std())