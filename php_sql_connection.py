import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='',db='departmentinfo')
#print(conn.connection_id)
curr = conn.cursor()
sql = 'select * from records'
curr.execute(sql)
data = curr.fetchall()
for lines in data:
    print(lines)