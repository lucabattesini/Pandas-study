import pandas as pd

#Grafico de barras
#Data frame
df = pd.DataFrame([30, 60, 20], index=["teatro","escola","rodoviária"])

#Criando grafico
barra = df.plot(kind="bar", legend=False)