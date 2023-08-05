from typing import Optional
from pydantic import BaseModel

class Return(BaseModel):
    resultCode: str
    resultExtra: Optional[str]
    resultText: str

class Response(BaseModel):
    output: Optional[str]
    return_: Return 
    