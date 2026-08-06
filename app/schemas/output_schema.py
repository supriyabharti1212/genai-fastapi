
from pydantic import BaseModel
from typing import List

class AIResponse(BaseModel):
    definition : str
    example : str
    advantages : List[str]
