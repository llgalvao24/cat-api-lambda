from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List
import logging
import boto3

from ports.out.breed_repository import BreedRepository
from models.breed import BreedModel

if TYPE_CHECKING:
    from mypy_boto3_dynamodb.service_resource import Table

dynamodb_client = boto3.client('dynamodb')
logger = logging.getLogger()
# logger.setLevel(logging.ERROR)


class BreedRepositoryImp(BreedRepository):
    def __init__(self, table: Optional[Table] = None) -> None:
        self.table = table

    @classmethod
    def from_env(cls) -> "BreedRepositoryImp":
        dynamo_resource = boto3.resource('dynamodb')
        table = dynamo_resource.Table('breed')
        return cls(table=table)

    def get_by_id(self, breed_id) -> dict:
        try:
            resp = self.table.get_item(Key={'breed_id': breed_id})
            logger.info("Breed fetched successfully")
            return {"breed": resp['Item']}
        except dynamodb_client.exceptions.ResourceNotFoundException as e:
            logger.info(e)
            return {"message": "Breed {breed_id} failed"}
        except Exception as e:
            logger.error(e)
            return {"message": "Breed fetch failed"}

    def get_all(self) -> List[dict]:
        try:
            resp = self.table.scan()
            logger.info("Breeds fetched successfully")
            print("all set, this test")
            return {"breeds": resp['Items']}
        except Exception as e:
            logger.error(e)
            return {"message": "Breeds fetch failed"}

    def save(self, breed: BreedModel) -> dict:
        try:
            resp = self.table.put_item(Item=breed)
            logger.info("Breed saved successfully")
            return {"message": "Breed saved successfully",
                    "status": resp['ResponseMetadata']['HTTPStatusCode']}
        except Exception as e:
            logger.error(e)
            return {"message": "Breed creation failed"}
