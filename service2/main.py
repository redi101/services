from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/sum")
def sum(a : int, b : int):
    return {"Result": a + b}