

import urllib, urllib2, sys,json,time
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
content = json.loads(content)
# if (content):
#     print content
res = []
data = content["showapi_res_body"]['list']

for i in range(27):
    res.append(data[i]['zhesuan'])
    # print data[i]['code']


time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
res.append(time)

# print res

import MySQLdb


conn = MySQLdb.Connect(

    host='mooncake520.com',
    port=3306,
    user='root',
    passwd='123456',
    db='jijian',
    charset='utf8'
    )
cursor = conn.cursor()
# sql1 = "INSERT INTO forex(AED,AUD) VALUES (%s,%s)" %(41,42)
sql="INSERT INTO forex(AED,AUD,BRL,CAD,CHF,DKK,EUR,GBP,HKD,IDR,INR,JPY,KRW,MOP,MYR,NOK,NZD,PHP,RUB,SAR,SEG,SGD,THB,TRY,TWD,USD,ZAR) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8],res[9],res[10],res[11],res[12],res[13],res[14],res[15],res[16],res[17],res[18],res[19],res[20],res[21],res[22],res[23],res[24],res[25],res[26])

#% (res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8],res[9],res[10],res[11],res[12],res[13],res[14],res[15],res[16],res[17],res[18],res[19],res[20],res[21],res[22],res[23],res[24],res[25],res[26],res[27],res[28])

cursor.execute(sql)
print cursor.rowcount
rs= cursor.fetchone()
print rs


conn.commit()