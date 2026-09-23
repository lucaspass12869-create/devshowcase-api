from fastapi import FastAPI
from .database import Base, engine
from .routers import profiles, technologies, projects

Base.metadata.create_all(bind=engine)

app = FastAPI(title="devshowcase-api - Lucas e Naiara)
