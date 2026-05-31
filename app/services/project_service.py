from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import ProjectCreate


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
