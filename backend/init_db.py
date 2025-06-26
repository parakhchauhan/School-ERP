from app.db import engine
from app.models.student import Base  # this should import all models

Base.metadata.create_all(bind=engine)