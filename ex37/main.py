import pandas as pd

#Fazendo junção interna
#Data Frame
dic_depto = {"id":["D1","D2","D3","D4"], 
 "nomDepto": ["Compras","RH","TI","Vendas"],
 "local":["SP","RJ","RJ","SP"]
 }
dic_emp = {"num":[3199,3269,3555,3788,3844],
 "nome": ["Ana","David","José","Marina","Luís"],
 "salario":[1600,2975,1500,5000,3000],
 "idDepto": ["D2","D3",None,"D2","D4"]
 }
depto = pd.DataFrame(dic_depto)
emp = pd.DataFrame(dic_emp)

#Operação de junção
juncao_interna = pd.merge(emp, depto, left_on="idDepto",
right_on="id")
print('------------------------------')
print("depto:")
print(depto)
print('------------------------------')
print("emp:")
print(emp)
print('------------------------------')
print("junção interna:")
print(juncao_interna)