#!D:\Python\python.exe
#coding=utf-8
import cgi,cgitb,time,csv
from pykeyboard import PyKeyboard

k=PyKeyboard()
form=cgi.FieldStorage()

x = form.getvalue('x')
y = form.getvalue('y')
z = form.getvalue('z')
l = form.getvalue('l')
w = form.getvalue('w')
h = form.getvalue('h')

print('Content-type:text/html\n')
print('<html>')
print('<head>')
print('<meta charset=\'utf-8\'>')
print('<title>moocxing</title>')
print('</head>')
print('<h2>x:',x,'y:',y,'z:',z,'l:',l,'w:',w,'h:',h,' </h2>')
print('</html>')

with open('set.csv', "r+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()   #清空文件

with open('set.csv','w',newline='') as f:
    csvwriter = csv.writer(f,dialect = ("excel"))
    csvwriter.writerow(x)
    csvwriter.writerow(y)
    csvwriter.writerow(z)
    csvwriter.writerow(l)
    csvwriter.writerow(w)
    csvwriter.writerow(h)
    
    
