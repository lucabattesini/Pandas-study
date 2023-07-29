import pandas as pd

#DataFrame
dados = {'nome' : ['Argentina', 'Brasil', 'França', 'Itália', 'Reino Unido'], 
         'continente': ['América', 'América', 'Europa', 'Europa', 'Europa'], 
         'extenção': [299, 477, 354, 143, 768], 
         'verde': [0, 1, 0, 1, 0]
         }

siglas = ['AR', 'BR', 'Fr', 'IT', 'UK']
paises = pd.DataFrame(dados, index=siglas)
print(paises)

#Testando o rotulo de linha
Br = 'BR' in paises.index
Us = 'US' in paises.index
print("Existe o rotulo BR? ", Br)
print("Existe o rotulo US? ", Us)
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")

#Testando o rotulo de uma coluna
verde = 'verde' in paises.columns
azul = 'azul' in paises.columns
print('Existe o rotulo verde? ', verde)
print('Existe o rotulo azul? ', azul)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')

#Testando valor de coluna
Brasil = paises['nome'].isin(['Brasil'])
print("Existe o valor Brasil? ", Brasil)