from flask import Flask

app = Flask(__name__)

@app.route('/')
#if we go to home page this should execute this
def welcome():
    return "welcome to India "

#if add name to the url it exectute this
@app.route('/<name>')
#if we go to home page this should execute
def welcome_name(name):
    return "welcome to India %s" % name

#creating another url
@app.route('/state/<name1>')
def welcome_state(name1):
    return "welcome to Karantaka %s" % name1



if __name__ == '__main__':
    app.run(debug=True)
