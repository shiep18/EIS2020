import pandas as pd
df = pd.read_excel('./获取关键表.xlsx')
df[['Unnamed: 3','Unnamed: 4']].to_excel('测量桩号.xlsx')


##print(df.loc['测量桩号'])
##df.loc['测量桩号'].to_excel('测量桩号.xlsx')
