from fastapi import FastAPI
from app.database.database import Base, engine
from app.models.project import Project
from app.models.place import Place

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Travel Planner API"}