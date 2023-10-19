from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    biography = Column(String(100))
    books = relationship("Book", back_populates="author")

    def __repr__(self):
        return f'{self.id}' + ' | ' + self.name


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True, unique=True)
    description = Column(String(100))
    books = relationship("Book", back_populates="category")

    def __repr__(self):
        return f'{self.id}' + ' | ' + self.title


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, unique=True)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)
    author = relationship("Author", back_populates="books")
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    category = relationship("Category", back_populates="books")
    publicationYear = Column(String(4))
    isbn = Column(String(20))
    description = Column(String(200))

    def __repr__(self):
        return str(self.id) + ' | ' + self.title


# uvicorn main:app --reload

# from book.models import Base
# target_metadata = Base.metadata




class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    posts = relationship("Post", back_populates="owner")

    def __repr__(self):
        return '{}  |  {}'.format(self.id, self.username)



class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="posts")

    def __repr__(self):
        return '{}'.format(self.id)

