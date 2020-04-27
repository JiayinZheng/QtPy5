import pymysql
db = pymysql.connect(host = 'localhost',port = 3306, user = 'root', passwd = '991128Lu',db = 'ct',charset = 'utf8')
# configure and connect
cursor = db.cursor()
cursor.execute("select uid from ct_editor")
# execute sql statements
data = cursor.fetchall().__getitem__(0)
# use the index to get specific attribute
# (3,)
print(data)
data = cursor.fetchone()
# 3
sql = "select * from ct_server"
cursor.execute(sql)
data = cursor.fetchone()
print(data)
sql2 = "select * from ct_server "