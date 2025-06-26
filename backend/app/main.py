from fastapi import FastAPI
from app.routers import student
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth
from app.db import Base, engine
from app.models import user


app = FastAPI()
app.include_router(auth.router)

app.include_router(student.router, prefix="/api")
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Welcome to School ERP Backend 🚀"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)