from fastapi import FastAPI
from app.database.database import Base, engine
from app.routers.places import router as place_router
from app.routers.artworks import router as artwork_router
from app.routers.projects import router as project_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(project_router)
app.include_router(artwork_router)
app.include_router(place_router)


@app.get("/")
def root():
    return {"message": "Travel Planner API"}
