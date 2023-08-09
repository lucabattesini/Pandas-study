import pandas as pd

df = pd.DataFrame({
    'homens': [1, 2, 3, 4, 5],
    'mulheres': [3, 5, 6, 7, 1]
})

box = df.boxplot(column=['homens', 'mulheres'])
