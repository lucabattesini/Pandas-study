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
