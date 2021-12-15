#instance of the app
from fastapi import FastAPI
import uvicorn

from pydantic import BaseModel
app = FastAPI()


#to connect to database

@app.get('/home')
def get():
    return 'Hello Harsha'

@app.get('/home/{name}')
def get(name):
    return f'Hello {name}'

class Item(BaseModel):
    name : str
    number : int

@app.post('home/post')
def post(game : Item):
   #item ---->Item-->item={'name':'name','number':12}
    new_name = game.name
    new_number = game.number
    return f'Hello{new_name} you are in {new_number}'

if __name__ == '__main__':
    uvicorn.run(app,port = 5000)



