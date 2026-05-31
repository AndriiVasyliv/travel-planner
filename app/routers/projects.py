from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.dependencies import get_db

from app.schemas.project import (
    ProjectCreate,
    ProjectResponse, ProjectUpdate
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


@router.get(
    "/",
    response_model=list[ProjectResponse]
)
def get_projects(
        db: Session = Depends(get_db)
):
    return ProjectService.get_projects(db)


@router.get(
    "/{project_id}",
    response_model=ProjectResponse
)
def get_project(
        project_id: int,
        db: Session = Depends(get_db)
):
    return ProjectService.get_project(
        db,
        project_id
    )


@router.put(
    "/{project_id}",
    response_model=ProjectResponse
)
def update_project(
        project_id: int,
        project: ProjectUpdate,
        db: Session = Depends(get_db)
):
    return ProjectService.update_project(
        db,
        project_id,
        project
    )


@router.delete(
    "/{project_id}"
)
def delete_project(
        project_id: int,
        db: Session = Depends(get_db)
):
    return ProjectService.delete_project(
        db,
        project_id
    )
