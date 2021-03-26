from flask import Flask, render_template, url_for
import sqlite3
import server
import database
from sqlite3 import Error
from flask import request, redirect

app = Flask(__name__)
app.secret_key = "L8yAgO7NvqHi8a_j_gpUyB3gJSmKRT2mqc4K26b3am2wBERSGjU3yksi4yDcg35n"

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
      #return render_template('login.html')
      print("endpoint hit")
      return server.login()

# PRODUCT CART OPERATIONS
@app.route('/addtocart', methods = ['GET','POST'])
def add_to_cart(usrId, itemId):
    return

#Main Method Instantiation #
if __name__ == "__main__":
    app.run(debug = True)
