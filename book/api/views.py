import fastapi
from sqlalchemy.orm import Session
from db.db_setup import get_db

from . import schemas
from book import models
# from .utils import bookConvertToDict

router = fastapi.APIRouter()



@router.get('/authors', response_model=list[schemas.Author])
async def getAuthorList(db: Session = fastapi.Depends(get_db)):
    return db.query(models.Author).all()


@router.post('/authors', response_model=schemas.Author)
async def createAuthor(author: schemas.BaseAuthor, db: Session = fastapi.Depends(get_db)):
    author = models.Author(**author.model_dump())
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


@router.get('/authors/{authors_id}', response_model=schemas.Author | None)
async def getAuthor(authors_id: int, db: Session = fastapi.Depends(get_db)):
    return db.query(models.Author).filter(models.Author.id == authors_id).first()


@router.put('/authors/{author_id}', response_model=schemas.Author)
async def updateAuthor(author_id: int, newData: schemas.BaseAuthor,  db: Session = fastapi.Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    author.name = newData.name
    author.biography = newData.biography
    db.commit()
    db.refresh(author)
    return author


@router.delete('/authors/{author_id}')
async def deleteAuthor(author_id: int, db: Session = fastapi.Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    db.delete(author)
    db.commit()
    return {'author': 'Author deleted.'}




@router.get('/categories', response_model=list[schemas.Category])
async def getCategoryList(db: Session=fastapi.Depends(get_db)):
    return db.query(models.Category).all()


@router.get('/categories/{category_id}', response_model=schemas.Category | None)
async def getCategory(category_id: int, response: fastapi.Response, db: Session = fastapi.Depends(get_db)):
    try:
        category = db.query(models.Category).filter(models.Category.id == category_id).first()
        if category is None:
            raise fastapi.HTTPException(status_code=404, detail="Item not found.")
    except Exception as error:
        response.status_code = fastapi.status.HTTP_404_NOT_FOUND
    return category


@router.post('/categories', response_model=schemas.Category)
async def createCategory(newCategory: schemas.BaseCategory, db: Session = fastapi.Depends(get_db)):
    category = models.Category(**newCategory.model_dump())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


@router.put('/categories/{category_id}', response_model=schemas.Category)
async def updateCategory(category_id: int,  updateCategory: schemas.BaseCategory, db: Session = fastapi.Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    category.title = updateCategory.title
    category.description = updateCategory.description
    db.commit()
    db.refresh(category)
    return category


@router.delete('/categories/{category_id}')
def deleteCategory(category_id: int, db: Session = fastapi.Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    db.delete(category)
    db.commit()
    return {'category': 'Category deleted.'}






@router.get("/books", response_model=list[schemas.Book])
async def getBooks(db: Session = fastapi.Depends(get_db)):

    books = db.query(models.Book).all()
    bookList = []
    # for book in books:
    #     try:
    #         covertedBook = bookConvertToDict(book, db)
    #         bookList.append(covertedBook)
    #     except Exception as error:
    #         pass
    return books


@router.get("/books/{book_id}", response_model=schemas.Book| None)
async def getBook(book_id: int, response: fastapi.Response, db: Session = fastapi.Depends(get_db)):
    try:
        book = db.query(models.Book).filter(models.Book.id == book_id).first()
        # book = bookConvertToDict(book, db)
        
        if book is None:
            raise fastapi.HTTPException(status_code=404, detail="Book not found.")
    except Exception as error:
        response.status_code = fastapi.status.HTTP_404_NOT_FOUND
    return book


@router.post('/books', response_model=schemas.Book|None)
async def createBook(newBook: schemas.CreateBook, db: Session=fastapi.Depends(get_db)):
    # newBook = newBook.model_dump()
    # author_id = newBook.pop('author_id')
    # category_id = newBook.pop('category_id')
    book = models.Book(**newBook.model_dump())
    db.add(book)
    db.commit()
    db.refresh(book)
    # return bookConvertToDict(book, db)
    return book


@router.put('/books/{book_id}', response_model=schemas.Book)
async def updatebook(book_id: int, updateBook: schemas.CreateBook, db: Session = fastapi.Depends(get_db)):
    # updateBook = updateBook.model_dump()
    # author_id = updateBook.pop('author_id')
    # category_id = updateBook.pop('category_id')
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    book.title = updateBook.title
    book.description = updateBook.description
    book.author_id = updateBook.author_id
    book.category_id = updateBook.category_id
    book.isbn = updateBook.isbn
    book.publicationYear = updateBook.publicationYear
    db.commit()
    db.refresh(book)
    # return bookConvertToDict(book, db)
    return book


@router.delete('/books/{book_id}')
async def deletebook(book_id: int, db: Session = fastapi.Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    db.delete(book)
    db.commit()
    return {'book': 'Book deleted.'}




@router.get('/users', response_model=list[schemas.User])
async def getUserList(db: Session = fastapi.Depends(get_db)):
    return db.query(models.User).all()


@router.post('/users', response_model=schemas.User)
async def createAuthor(author: schemas.BaseUser, db: Session = fastapi.Depends(get_db)):
    user = models.User(**author.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user





# @router.get('/posts', response_model=list[schemas.Post])
# async def getUserList(db: Session = fastapi.Depends(get_db)):
#     return db.query(models.Post).all()



# @router.post('/posts', response_model=schemas.Post)
# async def createAuthor(post: schemas.CreatePost, db: Session = fastapi.Depends(get_db)):
#     print(post)
#     post = models.Post(**post.model_dump())
#     db.add(post)
#     db.commit()
#     db.refresh(post)
#     return post

