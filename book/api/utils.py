from sqlalchemy.orm import Session
from book import models


def bookConvertToDict(book: models.Book, db: Session):
    author = db.query(models.Author).filter(models.Author.id==book.author_id).first()
    if author is None:
        raise Exception('Author Not Found')
    category = db.query(models.Category).filter(models.Category.id==book.category_id).first()
    if category is None:
        raise Exception('Category Not Found')
    
    bookData = {
        "title": book.title,
        "author": {
            "name":author.name,
            "biography": author.biography,
            "id": author.id
        },
        "category": {
            "title": category.title,
            "description": category.description,
            "id": category.id
        },
        "publicationYear": book.publicationYear,
        "isbn": book.isbn,
        "description": book.description,
        "id": book.id
    }
    return bookData

