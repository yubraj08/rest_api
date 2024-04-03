from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Yube is testing"}