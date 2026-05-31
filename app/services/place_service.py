from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.place import Place
from app.models.project import Project
from app.schemas.place import PlaceCreate
from app.services.art_api_service import ArtApiService


class PlaceService:

    @staticmethod
    async def create_place(
            db: Session,
            project_id: int,
            place_data: PlaceCreate
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

        if len(project.places) >= 10:
            raise HTTPException(
                status_code=400,
                detail="Maximum 10 places allowed"
            )

        existing_place = (
            db.query(Place)
            .filter(
                Place.project_id == project_id,
                Place.external_id == place_data.external_id
            )
            .first()
        )

        if existing_place:
            raise HTTPException(
                status_code=400,
                detail="Place already exists in project"
            )

        artwork = await ArtApiService.get_artwork(
            place_data.external_id
        )

        if not artwork:
            raise HTTPException(
                status_code=404,
                detail="Artwork not found"
            )

        place = Place(
            project_id=project_id,
            external_id=place_data.external_id,
            title=artwork["title"]
        )

        db.add(place)
        db.commit()
        db.refresh(place)

        return place

    @staticmethod
    def get_places(
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

        return project.places

    @staticmethod
    def get_place(
            db: Session,
            project_id: int,
            place_id: int
    ):
        place = (
            db.query(Place)
            .filter(
                Place.id == place_id,
                Place.project_id == project_id
            )
            .first()
        )

        if not place:
            raise HTTPException(
                status_code=404,
                detail="Place not found"
            )

        return place
