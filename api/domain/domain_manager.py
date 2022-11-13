from typing import Optional
from uuid import uuid4
import logging

from models.breed import BreedModel
from ports.out.cat_api_service import CatApiService
from ports.out.breed_repository import BreedRepository

logger = logging.getLogger()


class DomainManager:
    def __init__(
        self,
        cat_api_service: Optional[CatApiService] = None,
        breed_repository: Optional[BreedRepository] = None
    ) -> None:
        self.breed_repository = breed_repository
        self.cat_api_service = cat_api_service

    def fetch_breeds(self) -> dict:
        return self.cat_api_service.fetch_breeds()

    def get_all_breeds(self) -> dict:
        return self.breed_repository.get_all()

    def fetch_and_save_breeds(self) -> dict:
        try:
            breeds = self.cat_api_service.fetch_breeds()
            for breed in breeds:
                breedModel = BreedModel(
                    breed_id=str(uuid4()),
                    name=breed["name"],
                    description=breed["description"],
                    life_span=breed["life_span"],
                    temperament=breed["temperament"],
                    origin=breed["origin"]
                )
                self.breed_repository.save(breedModel.dict())
            return {"message": "Breeds fetched and saved successfully"}
        except Exception as e:
            logger.error(e)
            return {"message": "Breeds fetch and save failed"}
