from pydantic import BaseModel
from typing import Optional

class GetCalls(BaseModel):
    EscalationID: str
    class Config:
        orm_mode=True
	