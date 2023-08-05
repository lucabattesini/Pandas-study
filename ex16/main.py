import pandas as pd

#transformando um Data Frame em uma Serie
serie = pd.read_csv("C:\\Users\\Win\Documents\\Estudos-Progrmção\\Estudos\\Pandas\\exemplos\\Pandas-study-main\\ex16\\bfotool-download.csv", sep=" ",
                    index_col=0)

#convertendo
serie = serie.squeeze("columns")

print(serie)