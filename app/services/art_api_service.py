import httpx


class ArtApiService:
    BASE_URL = "https://api.artic.edu/api/v1/artworks"

    @staticmethod
    async def get_artwork(external_id: int):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{ArtApiService.BASE_URL}/{external_id}"
            )

        if response.status_code != 200:
            return None

        data = response.json()

        return data.get("data")

    @staticmethod
    async def search_artworks(query: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{ArtApiService.BASE_URL}/search",
                params={"q": query}
            )

        if response.status_code != 200:
            return []

        data = response.json()

        return data.get("data", [])