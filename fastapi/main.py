from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/hello/{name}")
async def read_name(name: str):
    return PlainTextResponse(f"Hello, {name}.")
