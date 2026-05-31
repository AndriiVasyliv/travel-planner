from fastapi import FastAPI
from app.database.database import Base, engine
from app.models.project import Project
from app.models.place import Place
from app.routers.projects import router as project_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(project_router)


@app.get("/")
def root():
    return {"message": "Travel Planner API"}