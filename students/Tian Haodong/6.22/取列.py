import pandas as pd

df = pd.read_excel("全表.xlsx", usecols=[3, 4],names=None)
df_li = df.values.tolist()
#print(df_li)
#df_li[].to_excel('45列.xlsx')

df = pd.DataFrame(df_li, columns=['4列', '5列'])

df.to_excel("45列.xlsx", index=False)




