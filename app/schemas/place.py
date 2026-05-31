from typing import Optional
from pydantic import BaseModel, ConfigDict


class PlaceCreate(BaseModel):
    external_id: int


class PlaceUpdate(BaseModel):
    notes: Optional[str] = None
    visited: Optional[bool] = None


class PlaceResponse(BaseModel):
    id: int
    external_id: int
    title: str
    notes: Optional[str]
    visited: bool

    model_config = ConfigDict(
        from_attributes=True
    )
