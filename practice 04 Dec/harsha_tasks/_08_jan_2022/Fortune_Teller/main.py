#import request is
from flask import Flask,render_template,request

from magic8ball import Magic
#create object
app = Flask(__name__)
@app.route('/')
def welcome():
    return render_template('home.html')
#to get info from the home page(html)
@app.route('/confirm',methods=['POST'])
def insert_details():
    newClass = Magic()
    result = newClass.fortune()
    return render_template('reg_success.html',result=result)

if __name__ == '__main__':
    app.run(debug=True,port=8006)      #debug true so that no need of rerunning the code
