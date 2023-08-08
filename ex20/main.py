import pandas as pd

#Tipos de atributos
#Data frame
dados = {"renda": [6.46, 1.50, 0.00, 2.57, 9.90, 6.22],
        "empregos": [1,1,0,1,2,3],
        "sexo": ["F","M","F","M","M","F"],
        "escolaridade": ["pós-graduação","fundamental",
        "médio","médio",
        "superior","médio"]}

pme = pd.DataFrame(dados)

#Imprime o nome dos atributos
print(pme.dtypes)