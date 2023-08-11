import pandas as pd

#Usando "unique()" e "value)counts()"
#Data Frame
dados = {"sexo": ["F","M","F","F","F","M"],
         "bairro": ["Belverde",
         "Belverde",
         "Savassi",
         "Anchieta",
          None,
         "Savassi"],
         "valor": [150.00,
         35.00,
         80.00,
         250.00,
         9.90,
         25.00], 
         "cartao": ["Master",
         "Visa",
         "Visa",
         "Amex",
         "Elo",
         "Master"]}

id = [1, 2, 3, 4, 5, 6]
vendas = pd.DataFrame(dados, index = id)

#Calculando o domínio dos produtos
print("Domínio dos atributos")
print("sexo", vendas["sexo"].unique())
print("bairro", vendas["bairro"].unique())
print("cartao", vendas["cartao"].unique())
print("-" * 50)

#Calcula a frequência dos valores por coluna
print("Tabela de frequência")
print("\n1-sexo")
print(vendas["sexo"].value_counts())
print("\n2-bairro")
print(vendas["bairro"].value_counts())

#unique- Retorna o domínio dos atributos categoricos
#value_counts- Retorna a frequência dos valores de cada coluna