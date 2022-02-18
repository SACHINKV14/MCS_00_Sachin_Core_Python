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
            conn = sqlite3.connect(str(currentdirectory) + "/yourdailytask.db")
            c = conn.cursor()
            queryadd = """INSERT INTO yourdailytask VALUES('{taskname}')""".format(taskname=tasknames)
            c.execute(queryadd)
            conn.commit()
            c.execute("SELECT * FROM yourdailytask ")
            all_data = c.fetchall()
            conn.close()
            return render_template('alldata.html', all_data=all_data)

        if id1=="retrieve":
            conn = sqlite3.connect("yourdailytask.db")
            c = conn.cursor()
            c.execute("SELECT * FROM yourdailytask ")
            conn.commit()
            all_data=c.fetchall()
            conn.close()
            return render_template('alldata.html',all_data=all_data)

        if id1=="delete":
            conn = sqlite3.connect("yourdailytask.db")
            c = conn.cursor()
            c.execute(f"DELETE FROM yourdailytask WHERE rowid={id} ")
            conn.commit()
            conn.commit()
            c.execute("SELECT * FROM yourdailytask ")
            all_data = c.fetchall()
            conn.close()
            return render_template('alldata.html', all_data=all_data)

        if id1=="update":
            conn = sqlite3.connect("yourdailytask.db")
            c = conn.cursor()
            c.execute(f'UPDATE yourdailytask SET taskname={tasknames} where rowid={id}')
            conn.commit()
            c.execute(f"DELETE FROM yourdailytask WHERE rowid={id} ")
            conn.commit()
            c.execute("SELECT * FROM yourdailytask ")
            all_data = c.fetchall()
            conn.close()

            return render_template('alldata.html', all_data=all_data)


    return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True)