from flask import Flask, render_template, request
import MySQLdb
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def login():
   return render_template('login.html')

@app.route('/login1')
def login1():
   return render_template('login1.html')

 

@app.route('/browse')
def browse():
    return render_template('browse.html')




@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         name = request.form['name']
         addr = request.form['addr']
         pincode = request.form['pin']
         contact = request.form['con']
         gender = request.form['gen']
         country = request.form['country']  
         city = request.form['city']
         course= request.form['course']
         institute = request.form['institute']

         
         with MySQLdb.connect("localhost","job","admin123","loginpage") as con:
            print conncted
            cur = con.cursor()
            
            
            cur.execute("INSERT INTO login(name,addr,pincode,contact,gender,city,country,course,institute)VALUES (?,?,?,?)",(name,addr,pin,con,gen,country,city,course,institute) )

            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = MySQLdb.connect("localhost","job","admin123","loginpage")
   #con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from login")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
