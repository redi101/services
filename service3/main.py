from fastapi import FastAPI, Request
import httpx

app = FastAPI()

@app.get("/greeting")
async def proxy_greeting(name : str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"http://localhost:8001/greeting?name={name}")
        return resp.json()

@app.get("/sum")
async def proxy_sum(a : int, b : int):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"http://localhost:8002/sum?a={a}&b={b}")
        return resp.json()