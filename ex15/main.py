import pandas as pd

#Importando csv sem cabeçalho separado por virgulas
notas = pd.read_csv("C:\\Users\\Win\Documents\\Estudos-Progrmção\\Estudos\\Pandas\\exemplos\\Pandas-study-main\\ex15\\bfotool-download.csv", sep=";")
print(notas)