from fastapi import FastAPI
abb=FastAPI()

@abb.get("/hello")
def hellow():
    return "welcome"
