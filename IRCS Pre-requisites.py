#This program can be used to create the required database and tables using MySQL Connector

import mysql.connector

con=mysql.connector.connect(user='root',host='localhost',passwd='<Enter MySQL Password Here>')#Enter MySQL Password
c=con.cursor()

c.execute("create database school")
c.execute("use school")
c.execute("create table marks(admission_number int primary key,name varchar(50),DOB date,English int,Computer int,Mathematics int,Physics int,Chemistry int)")
c.execute("create table passwd(admission_number int primary key,password varchar(50))")
c.execute("create table maspass(password varchar(150))")
c.execute("insert into maspass values(<Enter Master Password Here>)") #Enter Master Password for teacher to log in

con.commit()

