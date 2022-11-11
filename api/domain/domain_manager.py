from typing import Optional
from uuid import uuid4

from models.breed import BreedModel
from ports.out.cat_api_service import CatApiService
from ports.out.breed_repository import BreedRepository


class DomainManager:
    def __init__(
        self, breed_repository: Optional[BreedRepository] = None,
        cat_api_service: Optional[CatApiService] = None
    ) -> None:
        self.breed_repository = breed_repository
        self.cat_api_service = cat_api_service

    def fetch_breeds(self) -> dict:
        return self.cat_api_service.fetch_breeds()

    def fetch_and_save_breeds(self) -> dict:
        breeds = self.cat_api_service.fetch_breeds()
        for breed in breeds:
            breedModel = BreedModel(
                breed_id=str(uuid4()),
                name=breed.name,
                description=breed.description,
                life_span=breed.life_span,
                temperament=breed.temperament,
                origin=breed.origin
            )
            self.breed_repository.save(breedModel)
        return breeds
