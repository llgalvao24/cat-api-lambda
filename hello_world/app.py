from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World", "ok": True}


lambda_handler = Mangum(app=app, lifespan="off")
