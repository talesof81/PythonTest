import pandas as pd

df = pd.read_excel('angel.xlsx')

print(df[1:3])

## x[startAt:endBefore:skip]
#df[::2].to_excel('even.xlsx')
