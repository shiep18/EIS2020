#!C:\Users\cao\AppData\Local\Programs\Python\Python37\python.exe
#coding=utf-8
import cgi, cgitb 

# 创建 FieldStorage 实例化
form = cgi.FieldStorage() 

# 获取数据
mc_move = form.getvalue('mc_move')
mc_dir = form.getvalue('mc_dir')
#map=[[0.5,0.5]for x in range (10)]
#print (map)
print ("Content-type:text/html")
print ()
print ("<html>")
print ("<head>")
print ("<meta charset=\"utf-8\">")
print ("<title>moocxing</title>")
print ("</head>")
print ("<body>")
print ("<h2>%s:%s</h2>" % (mc_move,mc_dir))
print ("</body>")
print ("</html>")
with open(mc_move+'.txt', 'w') as f:
    f.write(f'{mc_dir}')

