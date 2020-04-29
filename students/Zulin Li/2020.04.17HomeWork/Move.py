#!D:\Python\python.exe
#coding=utf-8
import cgi,cgitb,time,csv
from pykeyboard import PyKeyboard

k=PyKeyboard()
form=cgi.FieldStorage()

mc_move = form.getvalue('mc_move')
mc_dir = form.getvalue('mc_dir')

print('Content-type:text/html\n')
print('<html>')
print('<head>')
print('<meta charset=\'utf-8\'>')
print('<title>moocxing</title>')
print('</head>')
print('<h2>Move:',mc_move,mc_dir,' </h2>')
print('</html>')

with open('move.csv', "r+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()   #清空文件

with open('move.csv','w',newline='') as f:
    csvwriter = csv.writer(f,dialect = ("excel"))
    for i in range(0,len(mc_move)):
        csvwriter.writerow([mc_move[i],mc_dir[i]])
