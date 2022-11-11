from abc import ABC, abstractmethod
from model.breed import BreedModel


class BreedRepository(ABC):
    @abstractmethod
    def save(self, breed: BreedModel) -> None:
        raise NotImplementedError("Method save not implemented")
