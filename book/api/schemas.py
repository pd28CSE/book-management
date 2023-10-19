from pydantic import BaseModel, Field
from book import models

class BaseAuthor(BaseModel):
    name: str
    biography: str
    
    class Config:
        __tablename__ = models.Author
        orm_mode = True

class Author(BaseAuthor):
    id: int


class BaseCategory(BaseModel):
    title: str
    description:str

    class Config:
        __tablename__ = models.Category
        orm_mode = True

class Category(BaseCategory):
    id: int



class BaseBook(BaseModel):
    title: str
    author: Author
    category: Category
    publicationYear: str
    isbn: str 
    description: str

    class Config:
        __tablename__ = models.Book
        orm_mode = True



class Book(BaseBook):
    id: int



class CreateBook(BaseModel):
    title: str 
    author_id: int
    category_id: int
    publicationYear: str
    isbn: str
    description: str 

    class Config:
        __tablename__ = models.Book
        orm_mode = True




class BaseUser(BaseModel):
    username: str

    class Config:
        __tablename__ = models.User
        orm_mode = True

class User(BaseUser):
    id: int



class CreatePost(BaseModel):
    title: str
    owner_id: int

    class Config:
        __tablename__ = models.Post
        orm_mode = True



class BasePost(BaseModel):
    title: str
    owner: User


class Post(BasePost):
    id: int

