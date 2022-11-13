from abc import ABC, abstractmethod
from models.breed import BreedModel


class BreedRepository(ABC):
    @abstractmethod
    def get_all(self) -> dict:
        raise NotImplementedError("Method get_all not implemented")

    @abstractmethod
    def save(self, breed: BreedModel) -> dict:
        raise NotImplementedError("Method save not implemented")
