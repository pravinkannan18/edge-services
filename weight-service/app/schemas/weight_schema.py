from pydantic import BaseModel

class WeightSchema(BaseModel):
    kg: float
