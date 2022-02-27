import mysql.connector as mqt
import random


psdw = (input("Give your MySQL password: "))


mydb = mqt.connect(host='localhost',user='root',password=psdw)

name_lst = ["Nike",'Adidas','New Balance','ASICS','Puma','Skechers','Fila','Bata','Burberry','VF Corporation']
price_lst = [random.randrange(1000,20000,200) for i in range(len(name_lst))]

cursor = mydb.cursor()

#creating stufs
cursor.execute("create database shoe_database")
cursor.execute("use shoe_database")
cursor.execute("create table data(code int unique primary key, name varchar(20), price int)")

for i in range(len(name_lst)):
    sql = f"INSERT INTO data (code, name, price) VALUES ('{101+i}','{name_lst[i]}', '{price_lst[i]}')"
    cursor.execute(sql)
    mydb.commit()

cursor.execute("select * from data")
result = cursor.fetchall()
for i in result:
    print(i)