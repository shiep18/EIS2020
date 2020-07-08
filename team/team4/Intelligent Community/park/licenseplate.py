import pymysql

def add():
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()

    s = ["京ND8W56", "鲁Q77777", "粤BNB698"]
    s1 = ['贾帅杰', '王文政', '黎祖林']
    s2 = ['1', '0', '1']
    for i in range(3):
        res = "'" + s[i] + "'" + ',' + "'" + s1[i] + "'" + ',' + s2[i]
        sql = "INSERT INTO usercar(licenseplate,name,carbarn) VALUES (" + res + ")"
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
            conn.close()

def user_info(num):
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()

    sql = "SELECT * FROM usercar WHERE licenseplate = '%s'" % num

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            return row  # 返回值格式(车牌, 用户名, 车位序号)
    except:
        conn.rollback()
        conn.close()
        return 0  # 外来车辆

def SearchPlate(num):
    num=str(num)
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()
    sql = "SELECT * FROM licenseplate WHERE state = '%s'" % num

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results[0][0]
    except:
        conn.rollback()
        conn.close()
        return 0  # 外来车辆

def car_num():
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()

    sql = "SELECT * FROM licenseplate"
    cursor.execute(sql)
    results = cursor.fetchall()

    info = [0 for _ in range(len(results))]
    state = [0 for _ in range(len(results))]
    i = 0
    for n in results:
        info[i] = n[0]
        state[i] = n[1]
        i = i + 1
    i = 8 - i

    return info, i, state

def car_Per():
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()
    sql = "SELECT * FROM usercar"
    cursor.execute(sql)
    results = cursor.fetchall()
    info = [0 for _ in range(len(results))]
    state = [0 for _ in range(len(results))]
    i=0
    for n in results:
        info[i] = n[3]
        state[i] = n[2]
        i += 1
    return info,state

# num:车牌号。字符类型
def delate(num):
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()
    sql = "DELETE FROM licenseplate WHERE number = \'" + num + "\'"
    cursor.execute(sql)
    conn.commit()

# num:车牌号。字符类型
def car_add(num):
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()
    res="'"+num+"','0'"
    sql = "INSERT INTO licenseplate(number,state) VALUES (" + res + ")"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        conn.close()

def Park_add(num,Plate):
    num=str(num)
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()
    sql = "UPDATE licenseplate SET state = \'" + num + "\' WHERE number = \'" + Plate +"\'"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        conn.close()


def Per_update(num,Plate):
    num = str(num)
    Plate=str(Plate)
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()
    sql = "UPDATE usercar SET state = \'" + num + "\' WHERE carbarn = \'" + Plate + "\'"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        conn.close()


if __name__=="__main__":
    pass
    #print(SearchPlate(6))




























