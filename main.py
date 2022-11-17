from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

@app.get("/username")
async def read_main():
    return {"msg": f"firsst test"}
