import pandas as pd
import json

with open("C:\\Users\\Win\Documents\\Estudos-Progrmção\\Estudos\\Pandas\\exemplos\\Pandas-study-main\\ex17\\bfotool-download.csv") as f:
    j_serie = json.load(f)

serie = pd.DataFrame(j_serie, columns=['comida', 'compra'])

print(serie)