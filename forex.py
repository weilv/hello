

import urllib, urllib2, sys
import ssl


host = 'https://ali-waihui.showapi.com'
path = '/waihui-list'
method = 'GET'
appcode = '2cd7b7bd4b964c2aa0398209963149c8'
querys = 'code='
bodys = {}
url = host + path + '?' + querys

request = urllib2.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib2.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)
    
import MySQLdb


conn = MySQLdb.Connect(

    host = 'mooncake520.com',
    port =3306,
    user = 'root',
    passwd = '123456',
    db = 'jijian',
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
