from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import StreamingResponse
import time
import asyncio


app = FastAPI() 

@app.post("/")
async def read_root():
    return {"Hello": "Wafa"}

@app.get("/stream")
async def stream_numbers(request: Request):
    async def number_generator():
        for i in range(1, 10):
            yield f"data: {i}\n\n"
            await asyncio.sleep(1)
    return StreamingResponse(number_generator(), media_type="text/event-stream")