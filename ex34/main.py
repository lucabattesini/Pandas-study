import pandas as pd

#concatenação de Data Frame
lojaA = pd.DataFrame({"loja":["A", "A", "A"],
 "dia": ["sex", "sab", "dom"],
 "valor": [7500, 9500, 8200]}
 )
lojaB = pd.DataFrame({"loja":["B", "B", "B"],
 "dia": ["sex", "sab", "dom"],
 "valor": [5100, 8250, 9900]}
 )
lojaC = pd.DataFrame({"loja":["C", "C"],
 "dia": ["sab", "dom"],
 "valor": [7500, 11800]}
 )

loja = pd.concat([lojaA, lojaB, lojaC], ignore_index=True)

print(loja)
