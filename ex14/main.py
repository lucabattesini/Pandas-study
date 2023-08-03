import pandas as pd

#importar arquivos csv
paises = pd.read_csv("C:\\Users\\Win\Documents\\Estudos-Progrmção\\Estudos\\Pandas\\exemplos\\Pandas-study-main\\ex14\\bfotool-download.csv", index_col="particles")
print(paises)