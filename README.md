# Library API

A simple Book Library API built with Python and FastAPI.

## Features

- Get all books
- Add a new book
- Get a book by ID
- Update a book
- Delete a book

## Technologies

- Python
- FastAPI
- Uvicorn

## Installation

Install the required packages:

```bash
python -m pip install -r requirements.txt
python -m pip install --upgrade fastapi "uvicorn[standard]"
```

## Run the Project

Run the following command from the project folder:

```bash
python -m uvicorn LibrariApi:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

## API Documentation

Open the following URL in your browser to test the API:

`http://127.0.0.1:8000/docs`

## Available Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/books` | Get all books |
| POST | `/books` | Add a new book |
| GET | `/books/{book_id}` | Get a book by ID |
| PATCH | `/books/{book_id}` | Update a book |
| DELETE | `/books/{book_id}` | Delete a book |

## Data Storage

Book data is stored in memory. Changes will be lost when the application restarts.

## Note

This project is a beginner-level practice project for learning REST APIs with FastAPI.