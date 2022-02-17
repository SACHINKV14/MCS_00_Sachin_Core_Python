from flask import Flask, render_template, request, redirect
import sqlite3
#os module
import os
#to check where the py file present
currentdirectory = os.path.dirname(os.path.abspath(__file__))
print(currentdirectory)



app = Flask(__name__)



@app.route('/', methods=['POST','GET'])
def hello_world():
    if request.method == 'POST':
        id = request.form['id']
        tasknames = request.form['tasktodo']
        id1=request.form['id1']

        if id1=="add":
            connection = sqlite3.connect(str(currentdirectory) + "/yourdailytask.db")
            cursor = connection.cursor()
            queryadd = """INSERT INTO yourdailytask VALUES('{taskname}')""".format(taskname=tasknames)
            cursor.execute(queryadd)
            connection.commit()
            cursor.close()
            return render_template('home.html')

        if id1=="retrieve":
            conn = sqlite3.connect("yourdailytask.db")
            c = conn.cursor()

            c.execute("SELECT * FROM yourdailytask ")

            all_data=c.fetchall()
            print(all_data)

            return render_template('alldata.html',all_data=all_data)



        if id1=="delete":
            return "deleting task"


    return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True)