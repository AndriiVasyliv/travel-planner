from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.dependencies import get_db

from app.schemas.project import (
    ProjectCreate,
    ProjectResponse
)

from app.services.project_service import ProjectService

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post(
    "/",
    response_model=ProjectResponse,
    status_code=201
)
def create_project(
        project: ProjectCreate,
        db: Session = Depends(get_db)
):
    return ProjectService.create_project(
        db=db,
        project_data=project
    )
