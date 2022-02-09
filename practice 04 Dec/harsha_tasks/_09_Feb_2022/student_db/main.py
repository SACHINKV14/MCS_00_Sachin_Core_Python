
from fastapi import FastAPI,Request

import uvicorn


app = FastAPI()


  # emp = Employee()
@app.post('/stu')
def student(stu : Student):
    # if emp.id == int:
    name = stu.sname
    sid = stu.sid
    sloc = stu.sloc
    s_data = get_even_stu(sid)
    s_name = s_data[1]
    return {'emp_data' : s_data, 'name' : s_name}

@app.get('/')
def some_fun():
    return 'hello'



if __name__ == '__main__':
    uvicorn.run(app,debug=True)
