#building url dynamically
#flask variable rules and url building

#redirect to redirect to the new page
#url_for is used to create redirect logically

from flask import Flask,redirect,url_for

#create object
app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to India"

@app.route('/pass/<int:score>')
def pass_score(score):
    return "person is passed scored marks is:" +str(score)

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


if __name__ == '__main__':
    app.run(debug=True,port=8001)