
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()
class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str | None = None

books = [
    {"id": 1, "title": "Python tricks", "author": "Fatemeh"},
    {"id": 2, "title": "grok", "author": "Faezeh"}
]

@app.get("/books")
def get_books():
    return books

@app.post("/books")
def add_book(book: BookCreate):
    book_data = book.model_dump()
    book_data["id"] = len(books) + 1
    books.append(book_data)
    return book_data

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    return {"message": "Book not found"}


@app.patch("/books/{book_id}")
def update_book(book_id: int, new_data: dict):
    for book in books:
        if book["id"] == book_id:
            book.update(new_data)
            return book

    return {"message": "Book not found"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted"}

    return {"message": "Book not found"}