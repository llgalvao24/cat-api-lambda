from fastapi import FastAPI
from mangum import Mangum
import boto3
from boto3.dynamodb.conditions import Key, Attr
from model.breed import BreedModel
from uuid import uuid4

app = FastAPI()

dynamo_resource = boto3.resource('dynamodb')

print(list(dynamo_resource.tables.all()))

breed_table = dynamo_resource.Table('breed')


@app.get("/")
def read_root():
    return {"Hello": "World", "ok": True}


@app.get("/hello")
def hello_mount():
    return {"message": "All is well", "ok": True}


@app.post("/api/breed")
def create_breed(Breed: BreedModel):
    breed = dict(
        breed_id=str(uuid4()),
        name=Breed.name,
        description=Breed.description,
        life_span=Breed.life_span,
        temperament=Breed.temperament,
        origin=Breed.origin,
    )

    resp = breed_table.put_item(Item=breed)

    if resp['ResponseMetadata']['HTTPStatusCode'] == 200:
        return {"message": "Breed created successfully", "ok": True}

    return {"message": "Breed creation failed", "ok": False}


@app.get("/api/breeds")
def get_breeds():
    resp = breed_table.scan()
    return resp['Items']


lambda_handler = Mangum(app=app, lifespan="off")
