from typing import Optional
from pydantic import BaseModel


class BreedModel(BaseModel):
    breed_id: Optional[str]
    breed_name: Optional[str]
    description: Optional[str]
    life_span: Optional[str]
    temperament: Optional[str]
    origin: Optional[str]
