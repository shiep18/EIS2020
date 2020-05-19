#!C:\Users\DELL\AppData\Local\Programs\Python\Python37\python377.exe
#coding=utf-8

import cgi,cgitb,time,csv
from pykeyboard import PyKeyboard
k=PyKeyboard()
# 创建 FieldStorage 实例化
form = cgi.FieldStorage() 

# 获取数据
#mc_build = form.getvalue('mc_build')
#mc_dir = form.getvalue('mc_dir')
x = form.getvalue('x')
y = form.getvalue('y')
z = form.getvalue('z')
#map=[[0.5,0.5]for x in range (10)]
#print (map)
print ("Content-type:text/html")
print ()
print ("<html>")
print ("<head>")
print ("<meta charset=\"utf-8\">")
print ("<title>moocxing</title>")
print ("</head>")
#print ("<body>")
#print ("<h2>%s:%s</h2>" % (mc_move,mc_dir))
print('<h2>x:',x,'y:',y,'z:',z,' </h2>')
#print ("</body>")
print ("</html>")
#with open(mc_build+'.csv', 'w') as f:
#    f.write(f'{mc_dir}')

with open('build.csv', "r+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()   #清空文件
with open('build.csv','w',newline='') as f:
    csvwriter = csv.writer(f,dialect = ("excel"))
    csvwriter.writerow(x)
    csvwriter.writerow(y)
    csvwriter.writerow(z)
