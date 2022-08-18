import mysql.connector as conn

mydb = conn.connect(host= "localhost", user = "root", passwd= "Shub@1994#") # establish connection
cursor = mydb.cursor()

s = "insert into sudhanshu.ineuron1 values(101, 'sudhanshu kumar', 'sudh@ineuron.ai', 100, 30)"
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)

mydb.commit()

cursor.execute("select * from sudhanshu.ineuron1")
for i in cursor.fetchall() :
    print(i)