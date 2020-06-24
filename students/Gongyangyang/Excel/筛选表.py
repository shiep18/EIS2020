import pandas as pd
df = pd.read_excel('./全表.xlsx')
df  = df.set_index('a')

#print(df.loc['铁塔地层物理力学指标推荐值'])

#df.loc['铁塔地层物理力学指标推荐值'].to_excel('获取关键表.xlsx')

print(df.loc['测量桩号'])

df.loc['测量桩号'].to_excel('测量桩号.xlsx')
