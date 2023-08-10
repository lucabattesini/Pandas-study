import pandas as pd

#Usando os comandos "sort_values" e "rank"
#Criando o Data frame
dados = {"nadador": ["Simonas Bilis",
         "Benjamin Proud",
         "Anthony Ervin",
         "Florent Manaudou",
         "Andriy Hovorov",
         "Nathan Adrian",
         "Bruno Fratus",
         "Brad Tandy"],
         "nacionalidade": ["Lituânia",
         "Grã-Bretanha",
         "Estados Unidos",
         "França",
         "Ucrânia",
         "Estados Unidos",
         "Brasil",
         "África do Sul"],
         "tempo": [22.08,
         21.68,
         21.40,
         21.41,
         21.74,
         21.49,
         21.79,
         21.79]}

raia = list(range(1, 9))
prova = pd.DataFrame(dados, index=raia)
prova.index.name = 'raia'

#Ordenando pelo tempo de forma crescente
prova = prova.sort_values(by="tempo")
print("Ordenado por tempo de forma crescente: ")
print(prova)

#Usando rankings
raia_result = prova["tempo"].rank(method="min")
print("Posição por narrador")
print(raia_result)

#sort_value:
#Ordena os objetos selecionados

#Rank:
#Classifica os Objetos