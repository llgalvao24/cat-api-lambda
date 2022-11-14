from fastapi import APIRouter

from domain.domain_manager import DomainManager
from adapters.out.cat_api_service_imp import CatApiServiceImp
from adapters.out.breed_repository_imp import BreedRepositoryImp
from models.breed import BreedModel

router = APIRouter()
domain_mgr = DomainManager(
    cat_api_service=CatApiServiceImp.from_env(),
    breed_repository=BreedRepositoryImp.from_env()
)  # declared as global vars - for init purpose


@router.get("/cat-api/breeds")
def fetch_breeds():
    return domain_mgr.fetch_breeds()


@router.get("/api/breeds/{breed_id}")
def get_breed_by_id(breed_id: str):
    return domain_mgr.get_breed_by_id(breed_id)


@router.get("/api/breeds")
def get_all_breeds():
    return domain_mgr.get_all_breeds()


@router.get("/api/breeds/fetch/save")
def fetch_and_save_breeds():
    return domain_mgr.fetch_and_save_breeds()


@router.patch("/api/breeds/{breed_id}")
def update_breed(breed_id: str, breed: BreedModel):
    update_breed = breed.dict(exclude_unset=True)
    return domain_mgr.update_breed(breed_id, update_breed)
