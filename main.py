from fastapi import FastAPI

from book.api import views


from db.db_setup import engine
from book.models import Author

Author.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(views.router)

