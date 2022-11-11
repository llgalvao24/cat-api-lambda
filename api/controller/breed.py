from fastapi import APIRouter
import boto3
from uuid import uuid4
from service.cat_api import fetch_breeds
from ports.out.model import BreedModel

router = APIRouter()
dynamo_resource = boto3.resource('dynamodb')
breed_table = dynamo_resource.Table('breed')


@router.get("/api/fetch-breeds")
def call_fetch_breeds():
    return fetch_breeds()


@router.post("/api/breed")
def create_breed(Breed: BreedModel):
    breed = BreedModel(
        breed_id=str(uuid4()),
        name=Breed.name,
        description=Breed.description,
        life_span=Breed.life_span,
        temperament=Breed.temperament,
        origin=Breed.origin
    )

    resp = breed_table.put_item(Item=breed)

    if resp['ResponseMetadata']['HTTPStatusCode'] == 200:
        return {"message": "Breed created successfully", "ok": True}

    return {"message": "Breed creation failed", "ok": False}


@router.get("/api/breeds")
def get_breeds():
    resp = breed_table.scan()
    return resp['Items']
