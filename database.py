from flask import Flask, render_template, url_for
import sqlite3
import app
from sqlite3 import Error
from flask import request, redirect

app = Flask(__name__)

# DB CREATION AND INSTANTIATION #

conn = sqlite3.connect('webstore.db')
cursor = conn.cursor() 
cursor.execute("DROP TABLE IF EXISTS PRODUCT")

#Creating table as per requirement
sql ='''CREATE TABLE PRODUCT(
   ID INT,
   PRODUCT_NAME CHAR(20) NOT NULL,
   PRICE FLOAT,
   QUANTITY INT
)'''

cursor.execute("DROP TABLE IF EXISTS USER")

sql2 ='''CREATE TABLE USER(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   EMAIL CHAR(20),
   PASSWD CHAR(20),
   PHONE INT
)'''

cursor.execute("DROP TABLE IF EXISTS CONTACTUS_MSG")

sql3 ='''CREATE TABLE CONTACTUS_MSG(
   FULLNAME CHAR(20) NOT NULL,
   EMAIL CHAR(20) NOT NULL,
   MSG CHAR(200)
)'''

cursor.execute(sql)
cursor.execute(sql2)
cursor.execute(sql3)
print("Tables created successfully........")
conn.commit()
