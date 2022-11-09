from pydantic import BaseModel


class BreedModel(BaseModel):
    breed_id: str
    name: str
    description: str
    life_span: str
    temperament: str
    origin: str
