#building url dynamically
#flask variable rules and url building


from flask import Flask

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
@app.route('/results/<int:score>')
def results_score(score):
    result=" "
    if score<50:
        result="fail"
    else:
        result="pass"
    return result




if __name__ == '__main__':
    app.run(debug=True,port=8000)