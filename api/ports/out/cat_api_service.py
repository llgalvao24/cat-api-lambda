from abc import ABC, abstractmethod


class CatApiService(ABC):
    @abstractmethod
    def fetch_breeds(self) -> dict:
        raise NotImplementedError("Method fetch_breeds not implemented")
