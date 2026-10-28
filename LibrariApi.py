
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, Field

app = FastAPI()
class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str | None = None

books = {
  1:  {"id": 1, "title": "Python tricks", "author": "Fatemeh"},
  2:  {"id": 2, "title": "grok", "author": "Faezeh"},
}

@app.get("/books")
def get_books():
    return books

@app.post("/books")
def add_book(book: BookCreate):
    book_data = book.model_dump()
    new_id = max(books.keys(), default=0) + 1
    book_data["id"] = new_id
    books[new_id] = book_data
    return book_data

@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id in books:
        return books[book_id]

    raise HTTPException(status_code=404, detail="Book not found")


@app.patch("/books/{book_id}")
def update_book(book_id: int, new_data: dict):
    if book_id in books:
            books[book_id].update(new_data)
            return books[book_id]

    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id in books:
            del books[book_id]
            return {"message": "Book deleted"}

    raise HTTPException(status_code=404, detail="Book not found")