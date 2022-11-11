from typing import Optional
import logging
import requests

from ports.out.cat_api_service import CatApiService

logger = logging.getLogger()


class CatApiServiceImp(CatApiService):
    def __init__(self, session: Optional[requests.Session] = None) -> None:
        self.session = session

    @classmethod
    def from_env(cls) -> "CatApiServiceImp":
        session = requests.Session()
        return cls(session=session)

    def fetch_breeds(self) -> dict:
        url = "https://api.thecatapi.com/v1/breeds?limit=10&page=0"
        headers = {
            "x-api-key": "live_X3z9DesKKCqSdk6nKCIt0pjNT5ScwJlAXZwC9Tpr4VOBODxLutVa4RKWy0XfbYZC"
        }

        try:
            response = self.session.get(url, headers=headers)
            logger.info("Fetch CatApi successfully")
            return response.json()
        except Exception as e:
            logger.error(e)
