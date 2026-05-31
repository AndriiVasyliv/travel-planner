from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.dependencies import get_db
from app.schemas.place import (
    PlaceCreate,
    PlaceResponse
)
from app.services.place_service import PlaceService

router = APIRouter(
    prefix="/projects",
    tags=["Places"]
)


@router.post(
    "/{project_id}/places",
    response_model=PlaceResponse,
    status_code=201
)
async def create_place(
        project_id: int,
        place: PlaceCreate,
        db: Session = Depends(get_db)
):
    return await PlaceService.create_place(
        db=db,
        project_id=project_id,
        place_data=place
    )
