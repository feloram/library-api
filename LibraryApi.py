
from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Field, Session, create_engine, select


# مدل جدول books
class Book(SQLModel, table=True):
    __tablename__ = "books"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=200)
    author: Optional[str] = Field(default=None, max_length=100)


from sqlalchemy import URL

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="xxxx",
    host="localhost",
    port=5432,
    database="library_db",
)

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/books", response_model=list[Book])
def get_books(session: Session = Depends(get_session)):
    return session.exec(select(Book)).all()


@app.post("/books", response_model=Book)
def create_book(book: Book, session: Session = Depends(get_session)):
    book.id = None
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int, session: Session = Depends(get_session)):
    book = session.get(Book, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.patch("/books/{book_id}", response_model=Book)
def update_book(
    book_id: int,
    updated_book: Book,
    session: Session = Depends(get_session),
):
    book = session.get(Book, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    book.title = updated_book.title
    book.author = updated_book.author
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


@app.delete("/books/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    book = session.get(Book, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    session.delete(book)
    session.commit()
    return {"message": "Book deleted successfully"}
