from typing import List
from abc import ABC, abstractmethod
from models.breed import BreedModel


class BreedRepository(ABC):
    @abstractmethod
    def get_by_id(self) -> dict:
        raise NotImplementedError("Method get not implemented")

    @abstractmethod
    def get_all(self) -> List[dict]:
        raise NotImplementedError("Method get_all not implemented")

    @abstractmethod
    def save(self, breed: BreedModel) -> dict:
        raise NotImplementedError("Method save not implemented")
