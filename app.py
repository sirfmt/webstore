from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine
from sqlalchemy import MetaData
import sqlite3
from sqlite3 import Error
from flask import request, redirect
from sqlalchemy import Table, Column, Integer, String, Float
from pymongo import MongoClient

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True;
#db = SQLAlchemy(app)

# DB CREATION AND INSTANTIATION #
#DB -- OPTION 1
engine = create_engine('sqlite:///test.db', echo = True)
meta = MetaData()

# Database Schema for Item and User #
Items = Table(
   'Items', meta, 
   Column('id', Integer, primary_key = True), 
   Column('product_name', String), 
   Column('price', Float), 
   Column('quantity', Integer)
)
Users = Table(
    'Users', meta,
    Column('firstname', String),
    Column('lastname', String),
    Column('email', String),
    Column('passwd', String),
    Column('phone', Integer)
)
meta.create_all(engine)

# DB CREATION AND INSTANTIATION #
# DB -- OPTION 2

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
# Commit your changes in the database
conn.commit()

#class Item(db.Model):
#    id = db.Column(db.Integer, primary_key = True)
#    product = db.Column(db.String(200))
#    price = db.Column(db.Integer)

# Site Routing Endpoints #
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mens/formalwear/shirts')
def formalShirts():
    return render_template('formalwear.html')


@app.route('/mens/formalwear')
def formalPants():
    return render_template('formalwear.html')

@app.route('/mens/casualwear')
def casualTshirts():
    return render_template('casualwear.html')

@app.route('/mens/accessories')
def accessories():
    return render_template('accessories.html')

@app.route('/checkout')
def checkoutBag(items):
    return

@app.route('/contactus')
def contactus():
    return render_template('contact.html')


@app.route('/signup', methods=['GET','POST'])
def register():
    if request.method =='POST':
        firstname = request.form.get('materialRegisterFormFirstName')
        lastname = request.form.get('materialRegisterFormLastName')
        email = request.form.get('defaultForm-email2')
        password = request.form.get('defaultForm-pass2')
        phone = request.form.get('materialRegisterFormPhone')
        return  render_template('accessories.html')          
       
    return render_template('signup.html')

# SIGNUP FORM SUBMISSION ENDPOINTS # 
@app.route('/signup_process', methods = ['GET','POST'])    
def signup_process():
            firstname = request.form.get('materialRegisterFormFirstName')
            lastname = request.form.get('materialRegisterFormLastName')
            email = request.form.get('defaultForm-email2')
            pwd = request.form.get('defaultForm-pass2')
            phone = request.form.get('materialRegisterFormPhone')
            try:
                sql_stat = '''INSERT INTO USER (FIRST_NAME, LAST_NAME, EMAIL, PASSWD, PHONE) 
                                VALUES (firstname, lastname, email, pwd, phone)'''
                cursor.execute(sql_stat)
                conn.commit()
                
            except Error as e:
                   print(e)
            return redirect("/")
            #return render_template('index.html')


@app.route('/contactus_submit', methods = ['POST'])
def contactSubmit():
            fullname = request.form.get('fname')
            email = request.form.get('email')
            msg = request.form.get('comments')

            try:
                sql_stat = '''INSERT INTO CONTACTUS_MSG (FULLNAME, EMAIL, MSG) 
                                VALUES (fname, email, comments)'''
                cursor.execute(sql_stat)
                conn.commit()
                
            except Error as e:
                   print(e)
        
            return render_template('registration_ack.html')

# PROFILE LOGIN ENDPOINTS #
@app.route('/login', methods =['GET'])
def youraccount() :
     return render_template('login.html') 


@app.route('/login_submission', methods = ['GET','POST'])
def loginSubmission():
        usrId = request.form.get('userId')
        passwd = request.form.get('passw')
        return passCheck(usrId,passwd) 

def passCheck(usrId, passwd):
        id = 'admin'
        pwd='admin'
        if  (id == usrId and pwd == passwd ):
            return 'Successful Login!'
        else:
            return 'Login Unsuccessful!'

# PRODUCT CART OPERATIONS
@app.route('/addtocart', methods = ['GET','POST'])
def add_to_cart(usrId, itemId):
    return

#Main Method Instantiation #
if __name__ == "__main__":
    app.run(debug = True)
