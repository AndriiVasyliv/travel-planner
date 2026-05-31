# Travel Planner API

## Features

- Project CRUD
- Place CRUD
- Art Institute API integration
- Artwork validation
- Maximum 10 places per project
- Duplicate place prevention
- Automatic project completion
- Project deletion restrictions

## Installation

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload

## Available Endpoints

### Projects
- POST /projects
- GET /projects
- GET /projects/{id}
- PUT /projects/{id}
- DELETE /projects/{id}

### Places
- POST /projects/{id}/places
- GET /projects/{id}/places
- GET /projects/{id}/places/{place_id}
- PATCH /projects/{id}/places/{place_id}

### Artworks
- GET /artworks/search

## API Documentation

http://localhost:8000/docs