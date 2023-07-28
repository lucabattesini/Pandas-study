import pandas as pd

#DataFrame
dados = {'nome' : ['Argentina', 'Brasil', 'França', 'Itália', 'Reino Unido'], 
         'continente': ['América', 'América', 'Europa', 'Europa', 'Europa'], 
         'extenção': [299, 477, 354, 143, 768], 
         'verde': [0, 1, 0, 1, 0]
         }

siglas = ['AR', 'BR', 'Fr', 'IT', 'UK']
paises = pd.DataFrame(dados, index=siglas)

#imprimindo
print(paises)