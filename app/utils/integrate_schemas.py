from typing import Optional
from pydantic import BaseModel, Field


class IntegrationInputs(BaseModel):
    method: str
    f: str
    a: float
    b: float
    grid_pts: int = Field(default=50)
    req_time: bool = Field(default=False)


class IntegrationOutputs(BaseModel):
    integral: float
    req_time: Optional[float] = None
