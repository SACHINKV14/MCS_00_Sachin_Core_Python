from fastapi import FastAPI     #import fastapi
import uvicorn                  #import uvicorn


app = FastAPI()                 #app initialize

@app.get('/')                   #end point creation
def home():
    return 'Hello World!'                 #responce

if __name__ == '__main__':
    uvicorn.run(app)            #run the code
