import MySQLdb


conn = MySQLdb.Connect(

    host = ‘localhost’,
    port =3306,
    user = 'root',
    passwd = '123456’,
    db = ‘jijian’,
    charset = 'utf8'
    )
cursor = conn.cursor()

sql="select * from bitcoin where value=0 "

sql2 = "delete  from bitcoin where value=0"
cursor.execute(sql2)
print cursor.rowcount
rs= cursor.fetchone()
print rs

cursor.execute(sql)
print cursor.rowcount
rs= cursor.fetchone()
print rs

conn.commit()
