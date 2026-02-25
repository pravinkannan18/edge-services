from pydantic import BaseModel

class RFIDSchema(BaseModel):
    tag: str
