import pandas as pd

#Series
moedas = ['Peso', 'Real', 'Euro', 'Euro', 'Libra']
paises = [['América', 'América', 'Europa', 'Europa', 'Europa'],
['AR', 'BR', 'FR', 'IT', 'UK']]

#Juntando as Series
paises = pd.Series(moedas, index=paises)

#Imprimindo Paises
print(paises)
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

#Imprimindo especificamente
print(paises["América"])
print(paises[:, 'IT'])