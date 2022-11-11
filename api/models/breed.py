from pydantic import BaseModel


class BreedModel(BaseModel):
    breed_id: str
    name: str
    description: str
    life_span: str
    temperament: str
    origin: str

    def __init__(self, breed_id, name, description, life_span, temperament, origin):
        self.breed_id = breed_id
        self.name = name
        self.description = description
        self.life_span = life_span
        self.temperament = temperament
        self.origin = origin

    def __repr__(self):
        return f"BreedModel(breed_id={self.breed_id}, \
          name={self.name}, description={self.description}, \
          life_span={self.life_span}, temperament={self.temperament}, \
          origin={self.origin})"
