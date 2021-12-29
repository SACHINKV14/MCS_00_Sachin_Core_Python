#import request is
from flask import Flask,render_template,redirect,url_for,request
#to use sqlite
import sqlite3
#os module
import os
#to check where the py file present
currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
#homepage
@app.route('/')
def welcome():
    return render_template('home.html')
#to get info from the home page(html)
@app.route('/confirm',methods=['POST'])
def insert_details():
    firstname=request.form['firstname']
    lastname=request.form['Lastname']
    mailid=request.form['Mailid']
    phonenum=request.form['Phonenumber']
    location=request.form['Location']
    username=request.form['username']
    password=request.form['password']
    # connection sqlite3
    connection = sqlite3.connect(currentdirectory + "\studentregister.db")
    cursor = connection.cursor()
    #inseert data into db
    query1="""INSERT INTO studentregister 
    VALUES('{fn}','{ln}','{mid}',{pn},'{l}','{un}','{p}') 
    """.format(fn=firstname,ln=lastname,mid=mailid,pn=phonenum,l=location,un=username,p=password)
    cursor.execute(query1)
    connection.commit()
    cursor.close()
    return render_template('reg_success.html')

if __name__ == '__main__':
    app.run(debug=True,port=8005)      #debug true so that no need of rerunning the code
