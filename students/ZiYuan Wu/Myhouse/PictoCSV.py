
import pandas as pd
list=[[1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1],
      [1,1,0,1,1,1,1,0,1,1],
      [1,1,0,0,1,1,1,0,1,1],
      [1,1,0,1,0,1,1,0,1,1],
      [1,1,0,1,1,0,1,0,1,1],
      [1,1,0,1,1,1,0,0,1,1],
      [1,1,0,1,1,1,1,0,1,1],
      [1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1]]
# 下面这行代码运行报错
# list.to_csv('e:/testcsv.csv',encoding='utf-8')
test=pd.DataFrame(columns = None,data=list)#数据有三列，列名分别为one,two,three
print(test)
test.to_csv('e:/2020class/QianRuShi/minecraft_m3_all/myhouse/N.csv',encoding='gbk',header=0,index=0)

