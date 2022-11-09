from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World", "ok": True}


@app.get("/hello")
def hello_mount():
    return {"message": "All is well", "ok": True}


lambda_handler = Mangum(app=app, lifespan="off")
