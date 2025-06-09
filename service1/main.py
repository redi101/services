from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/greeting")
def greeting(name : str):
    return {f"Привет, {name}!"}