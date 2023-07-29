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

#imprimindo as propriedades

print('---------------------')
num_linhas = paises.shape[0]
num_colunas = paises.shape[1]
indices = paises.index
colunas = paises.columns
paises_tipo = type(paises)
paises_dtype = paises.dtypes
paises_idx_dtype = paises.index.dtype

print('número de linhas: ', num_linhas)
print('número de colunas: ', num_colunas)
print('rótulos das linhas: ', indices)
print('rótulos das colunas: ', colunas)
print('tipo (type): ', paises_tipo)
print('dtypes das colunas:\n', paises_dtype)
print('dtype dos rótulos das linhas:', paises_idx_dtype)
print("=-=-=-=-=-=-=-=-=-=-=-=")