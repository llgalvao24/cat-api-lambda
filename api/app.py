from fastapi import FastAPI
from mangum import Mangum
from adapters.router import api_routers

app = FastAPI()

app.include_router(api_routers.router)


@app.get("/")
def read_root():
    return {"ok": True}


lambda_handler = Mangum(app=app, lifespan="off")
