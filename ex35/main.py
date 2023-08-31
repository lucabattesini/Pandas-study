import pandas as pd

#Juntando data frames
#Data frames
d1 = pd.DataFrame({"carro":["Hyundai", "Renault", "Fiat"]})
d2 = pd.DataFrame({"animal":["Capivara", "Bem-te-vi"]})
#juntando o Data frame
d3 = pd.concat([d1,d2], ignore_index=True, sort=False)
print(d3)