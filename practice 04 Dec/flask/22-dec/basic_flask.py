from flask import flask

app = Flask(__name__)

@app.route('/')
def welcome():
    #should reeturnthe render template
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True,port=8002)