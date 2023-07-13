import pandas as pd

#NaN no pandas

#criando series para saber se existem a cor verde
# ou azul nas bandeiras nos paises

verde = pd.Series({'BR' :1, 'FR': 0, 'IT': 1, 'UK': 0})
azul = pd.Series({'AR': 1, 'BR' :1, 'FR' :1, 'IT' :0, 'UK' :1})

#Somando as Series
soma = verde + azul
print('soma')
print(soma)
print("-------------------------------------")

#Verificando se o valor é NaN
print("a soma é nula?")
print(pd.isnull(soma))

#O valor 'AR' é nulo pois ele so existe na 
# Serie azul, e não é somado com nenhum valor na Serie verde 

#Os valores NaN no pandas representam valores nulos, ausentes
#ou desconhecidos