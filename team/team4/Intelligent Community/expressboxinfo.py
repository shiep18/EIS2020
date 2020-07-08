import pymysql

#number：字符类型
#number：快递箱编号。输入编号即可得到返回值。
#返回值格式('2', '1-102', '0')
def express_info(number):
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()

    sql = "SELECT * FROM user WHERE bianhao = '%s'" % number
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        return row
    
#number：快递箱编号。输入编号即可改变状态值为1。
#放快递时调用
def deposit(number):
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()
    sql = "update user set state=" + '1' + " where bianhao=\'" + number + "\'"

    cursor.execute(sql)
    conn.commit()

#number：快递箱编号。输入编号即可改变状态值为0。
#取快递时调用
def take_out(number):
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()
    sql = "update user set state=" + '0' + " where bianhao=\'" + number + "\'"

    cursor.execute(sql)
    conn.commit()
