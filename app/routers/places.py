from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.dependencies import get_db
from app.schemas.place import (
    PlaceCreate,
    PlaceResponse, PlaceUpdate
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


@router.get(
    "/{project_id}/places",
    response_model=list[PlaceResponse]
)
def get_places(
        project_id: int,
        db: Session = Depends(get_db)
):
    return PlaceService.get_places(
        db,
        project_id
    )


@router.get(
    "/{project_id}/places/{place_id}",
    response_model=PlaceResponse
)
def get_place(
        project_id: int,
        place_id: int,
        db: Session = Depends(get_db)
):
    return PlaceService.get_place(
        db,
        project_id,
        place_id
    )


@router.patch(
    "/{project_id}/places/{place_id}",
    response_model=PlaceResponse
)
def update_place(
        project_id: int,
        place_id: int,
        place: PlaceUpdate,
        db: Session = Depends(get_db)
):
    return PlaceService.update_place(
        db,
        project_id,
        place_id,
        place
    )
