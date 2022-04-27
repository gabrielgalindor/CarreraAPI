from pydantic import BaseModel
from typing import Collection, Optional

class drawM(BaseModel):
    collection: str
    part: str
    variation: int
    class Config:
        orm_mode=True