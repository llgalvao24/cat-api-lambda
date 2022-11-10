from fastapi import FastAPI
from mangum import Mangum
from controller import breed

app = FastAPI()

app.include_router(breed.router)


@app.get("/")
def read_root():
    return {"Hello": "World", "ok": True}


@app.get("/hello")
def hello_mount():
    return {"message": "All is well", "ok": True}


lambda_handler = Mangum(app=app, lifespan="off")
