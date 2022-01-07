#integrate html with flask
#http verb GET and POST

#render_template is used to renderhtml page

#request is to read the the posted value
from flask import Flask,redirect,url_for,render_template,request

#create object
app = Flask(__name__)

@app.route('/')
def welcome():
    #should reeturnthe render template
    return render_template('index.html')

@app.route('/pass/<int:score>')
def pass_score(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('results.html',result=res)

@app.route('/fail/<int:score>')
def fail_score(score):
    return "person is failed scored marks is:" +str(score)


#result checker
@app.route('/results/<int:marks>')
def results_score(marks):
    result=" "
    if marks<50:
        #it redirect to fail score func
        result="fail_score"
    else:
        result="pass_score"

    #to redirect to new url page
    return redirect(url_for(result,score=marks))

###result checker html page
@app.route("/submit",methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        maths=float(request.form["maths"])
        biology=float(request.form['biology'])
        chemistry=float(request.form['chemistry'])
        total_score=(maths+biology+chemistry)/3
    res1=""
    if total_score>=50:
        res1="pass_score"
    else:
        res1="fail_score"
    return redirect(url_for(res1,score=total_score ))



if __name__ == '__main__':
    app.run(debug=True,port=8002)