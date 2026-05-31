from fastapi import APIRouter
from app.services.art_api_service import ArtApiService

router = APIRouter(
    prefix="/artworks",
    tags=["Artworks"]
)


@router.get("/search")
async def search_artworks(q: str):
    return await ArtApiService.search_artworks(q)