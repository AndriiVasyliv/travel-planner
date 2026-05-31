from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate


class ProjectService:

    @staticmethod
    def create_project(
            db: Session,
            project_data: ProjectCreate
    ):
        project = Project(
            name=project_data.name,
            description=project_data.description,
            start_date=project_data.start_date
        )

        db.add(project)
        db.commit()
        db.refresh(project)

        return project

    @staticmethod
    def get_projects(db: Session):
        return db.query(Project).all()

    @staticmethod
    def get_project(
            db: Session,
            project_id: int
    ):
        project = (
            db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

        if not project:
            raise HTTPException(
                status_code=404,
                detail="Project not found"
            )

        return project

    @staticmethod
    def update_project(
            db: Session,
            project_id: int,
            project_data: ProjectUpdate
    ):
        project = ProjectService.get_project(
            db,
            project_id
        )

        update_data = project_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(project, key, value)

        db.commit()
        db.refresh(project)

        return project

    @staticmethod
    def delete_project(
            db: Session,
            project_id: int
    ):
        project = ProjectService.get_project(
            db,
            project_id
        )

        if any(place.visited for place in project.places):
            raise HTTPException(
                status_code=400,
                detail="Cannot delete project with visited places"
            )

        db.delete(project)
        db.commit()

        return {"message": "Project deleted"}
