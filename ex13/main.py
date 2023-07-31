import pandas as pd

#Modificando Data Frames

#Data Frame

dados = {'nome': ['Argentina','Brasil','França','Itália',
 'Reino Unido'],
 'continente': ['América','América','Europa','Europa',
 'Europa'],
 'extensao': [2780,8511,644,301,244],
 'verde': [0,1,0,1,0]}

siglas = ['AR','BR','FR','IT','UK']

paises = pd.DataFrame(dados,index=siglas)

#inseriondo paises
paises.loc['JP'] = {'nome': 'Japão', 
                     'continente': 'Ásia',
                     'extensao': 372,
                     'verde': 0}

#Alterando a extensão
paises.at['BR', 'extensao'] = 9304

#Removendo paises
paises = paises.drop(['AR'])

#Imprimindo o Data Frame modificado
print(paises)