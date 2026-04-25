from pydantic import BaseModel, Field
from typing import Optional, Any

class User(BaseModel):
    first_name:str = Field(examples=["Mansih"])
    last_name:str = Field(examples=["Kumar"])
    wage: Optional[int] = Field(default=300, examples = [700])
    role: Optional[str] = Field(default='mistri',examples = ["mistri"])

class Attendance(BaseModel):
    labour_id : Optional[int] = Field(default=None,examples=[1])
    first_name:str = Field(default=None,examples=["Mansih"])
    last_name:str = Field(default=None, examples=["Kumar"])


class UIResponse(BaseModel):
    status: str
    status_code:int
    data: Any
    message: str

