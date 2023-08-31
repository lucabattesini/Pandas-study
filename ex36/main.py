import pandas as pd
#Verificando se data frames são iguais
#Criando Data frames
filmes1 = pd.DataFrame({"titulo":["O Filho da Noiva",
 "La La Land"],
 "ano":[2001,
 2017]})
filmes2 = pd.DataFrame({"titulo":["Noel, Poeta da Vila",
 "La La Land"],
 "ano":[2007,
 2017]})
filmes3 = pd.DataFrame({"titulo":["O Filho da Noiva",
 "La La Land"],
 "ano":[2001,
 2017]})

print('filmes é igual à filmes -> ', filmes1.equals(filmes2))
print('filmes é igual à filmes -> ', filmes1.equals(filmes3))