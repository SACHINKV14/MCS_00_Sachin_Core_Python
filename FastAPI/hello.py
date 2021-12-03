from fastapi import FastAPI
app=FastAPI

@app.get("/hello")
async def hellow():
    return "welcome"