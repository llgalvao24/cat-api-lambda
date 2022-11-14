from typing import List
from abc import ABC, abstractmethod
from models.breed import BreedModel


class BreedRepository(ABC):
    @abstractmethod
    def get_by_id(self, breed_id: str) -> dict:
        raise NotImplementedError("Method get not implemented")

    @abstractmethod
    def get_all(self) -> List[dict]:
        raise NotImplementedError("Method get_all not implemented")

    @abstractmethod
    def save(self, breed: dict) -> dict:
        raise NotImplementedError("Method save not implemented")

    @abstractmethod
    def update(self, breed_id: str, breed: dict) -> dict:
        raise NotImplementedError("Method update not implemented")
