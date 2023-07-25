import pandas as pd

#Series Temporais

dias = ['01/02/2022', '02/02/2022', '03/02/2022', '04/02/2022', '05/02/2022', '06/02/2022']
temp = [31, 35, 34, 28, 27, 27]
Serie_temporal = pd.Series(temp, index=dias)

#imprimindo
Serie_temporal.index = pd.to_datetime(Serie_temporal.index, format='%d/%m/%Y')
print(Serie_temporal)