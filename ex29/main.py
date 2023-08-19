import pandas as pd

#Criando um grafico de linhas
#Data Frame
dados = {"óleo de soja": [71.15, 66.93, 67.91, 67.66],
         "melancia": [10.52, 15.68, 14.95, 26.23],
         "frango congelado": [47.17, 23.68, 38.36, 17.08]
}
df = pd.DataFrame(dados, index=[3, 6, 9, 12])

#Criando o grafico
line = df.plot(kind="line", style=[".-"],
               ylim=(0, 100), xlim=(3, 12))