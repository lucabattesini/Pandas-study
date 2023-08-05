import pandas as pd

dados = {'codigo': [1001,1002,1003,1004,1005],
        'nome': ['Linguiça','Quijo','Café','Presunto',
        'Pão']
 }

produtos = pd.DataFrame(dados)

produtos.to_csv("C:\\Users\\Win\Documents\\Estudos-Progrmção\\Estudos\\Pandas\\exemplos\\Pandas-study-main\\ex18\\bfotool-download.csv", sep="\t", index=False)

print(produtos)