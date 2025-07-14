import mysql.connector as ms
msdb=ms.connect(host="localhost",user="root",passwd="sanjay@2005")
msc=msdb.cursor()

db="create database bakery"
msc.execute(db)
msdb.commit()
print("database success")

dbu="use bakery"
msc.execute(dbu)
msdb.commit()
print("database used")

utbl="create table uinfo(name varchar(20) not null,pinno integer(4) not null primary key)"
msc.execute(utbl)
msdb.commit()
print("user table success")

otbl="create table oinfo(icode integer , iname varchar(20)primary key,qty integer ,iprice integer,owner varchar(20))"
msc.execute(otbl)
msdb.commit()
print("order table success")

ptbl="create table product (icode integer(3) primary key,iname varchar(20),iqty integer ,iprice integer(4))"
msc.execute(ptbl)
msdb.commit()
print("product table success")









