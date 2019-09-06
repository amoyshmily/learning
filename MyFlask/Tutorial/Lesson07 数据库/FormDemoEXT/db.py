import pymysql


def getConn():
    """
    建立连接
    :return:
    """
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='flask')
    return conn


def doQuery(sql: str) -> tuple:
    """
    查询
    :param sql:
    :return:
    """
    conn = getConn()
    cursor = conn.cursor()

    cursor.execute(sql)
    record = cursor.fetchall()

    conn.close()
    return record


def doCUD(sql: str) -> int:
    conn = getConn()
    cursor = conn.cursor()
    affected_rows = 0
    try:
        affected_rows = cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    return affected_rows


def addUser(username: str, password: str):
    """
    新增用户
    :param username:
    :param password:
    :return:
    """
    s = 'INSERT INTO user (username, password) VALUES ("{}", "{}")'.format(username, password)
    i = doCUD(sql=s)

    if i:
        print('用户新增成功！')


def isExisted(username: str, password: str) -> bool:
    sql = 'SELECT * FROM user WHERE username="{}" AND password="{}";'.format(username, password)
    record_tup = doQuery(sql=sql)
    if record_tup:
        print('该用户已存在！')
        return True
    else:
        print('该用户不存在！')
        return False


if __name__ == '__main__':
    isExisted('amoy', '12')
