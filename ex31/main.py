import pandas as pd

#Grafico de barras agrupadas
#Data Frame
df = pd.DataFrame({"mulheres": [40,10,30], 
                   "homens": [30,15,20]},
                   index=["teatro", "escultura", "pintura"])

#criando o grafico
barras = df.plot(kind="bar", legend=True, color=["yellow","blue"])