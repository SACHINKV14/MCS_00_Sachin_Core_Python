from fastapi import FastAPI,Request, Form    #import fastapi
import uvicorn                  #import uvicorn


app = FastAPI()


@app.get('/{item},{item1}')
def get_body(item,item1):
    sum=int(item)+int(item1)
    return {"sum of two numbers is:"f'{sum}'}


if __name__ == '__main__':
    uvicorn.run(app,debug=True,port=8002)