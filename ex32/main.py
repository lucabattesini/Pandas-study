import pandas as pd

#Criando um hitograma
#Data Frame
df = pd.DataFrame({
                    "tempo": [4, 5, 1, 7, 7, 8, 6, 6, 5,
                    2, 5, 8, 7, 1, 6, 3, 4, 8,
                    5, 7, 4, 6, 3, 6, 2, 6, 8]})

#Criando o hitograma
hit = df.plot(kind="hist", bins=3)