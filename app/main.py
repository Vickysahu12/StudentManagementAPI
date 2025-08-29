from fastapi import FastAPI

app = FastAPI()

@app.get("/AboutVicky")
async def about_vicky():
    return{"message":"In This Backend system we will gonna make and production grade ready api system"}