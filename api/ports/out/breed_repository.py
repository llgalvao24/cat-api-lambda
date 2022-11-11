from abc import ABC, abstractmethod


class BreedRepository(ABC):
    @abstractmethod
    def save(self) -> None:
        raise NotImplementedError("Method save not implemented")
