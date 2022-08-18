import mysql.connector as conn


mydb = conn.connect(host= "localhost", user = "root", passwd= "Shub@1994#") # establish connection
cursor = mydb.cursor()   # create cursor
#cursor.execute("create database sudhanshu") #create database
#cursor.execute("show databases")  # fire queries here

#s = "create table sudhanshu.ineuron(employee_id int(10) , emp_name varchar(80) , emp_mailid varchar(20) emp_salary int(6), emp_atten int(3) )"
#cursor.execute(s)
#print(cursor.fetchall()) # to print databases

#s = "create table sudhanshu.ineuron1(employe_id int(10)  , emp_name varchar(80) , emp_mailid varchar(20),emp_salary int(6) , emp_attendence int(3))"
#q1 = cursor.execute(s)

q2 = cursor.execute("select * from sudhanshu.ineuron1")
print(q2)


