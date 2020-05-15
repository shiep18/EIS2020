import cgi, cgitb
from controlend import controlend

form = cgi.FieldStorage()

mc_move = form.getvalue('mc_move')
mc_dir = form.getvalue('mc_dir')
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
try:
    controlend()
except Exception as e:
    print(repr(e))


