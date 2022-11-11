from fastapi import APIRouter

from domain.domain_manager import DomainManager
from adapters.out.cat_api_service_imp import CatApiServiceImp

router = APIRouter()
domain_mgr = None  # declared as global vars - for init purpose


@router.get("/api/fetch-breeds")
def fetch_breeds():
    global domain_mgr
    if domain_mgr is None:
        domain_mgr = DomainManager(cat_api_service=CatApiServiceImp.from_env())
    return domain_mgr.fetch_breeds()
