import pandas as pd

#Tendencia central
#DataFrame
dados = {'jogador': ['Felipe', 'Carlos', 'Luca'],
         'infracao': ['Falta', 'Abuso verbal', 'Reclamação'],
         'punicao': [1, 3, 1]
}

df = pd.DataFrame(dados)

#calculando a tendência central
print("media ", df['punicao'].mean())
print("mediana ", df['punicao'].median())
print("moda ", df['punicao'].mode().values)