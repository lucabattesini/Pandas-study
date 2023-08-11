import pandas as pd

#Usando o metodo 'group_by'
#DataFrame
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

id = [1,2,3,4,5,6]

vendas = pd.DataFrame(dados, index=id)

#Gerando um variavel chamada grouped
valor = vendas['valor'].groupby(vendas['bairro'])

#computando agregados
print('- quantidade de clientes, por bairro:\n', valor.count())
print('--------------------------------------')
print('- valor total das vendas, por bairro:\n', valor.sum())
print('--------------------------------------')
print('- valor médio das vendas, por bairro:\n', valor.mean())