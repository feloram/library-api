# Library API

A simple Library API built with Python and FastAPI.

This project contains two implementations:

## 1. Dictionary Version
- File: `LibrariApi.py`
- Stores book data in a Python dictionary.
- Data is stored temporarily in memory.

## 2. PostgreSQL Version
- File: `LibraryApi.py`
- Uses PostgreSQL as the database.
- Uses SQLModel and SQLAlchemy for database operations.
- Stores book data persistently in the database.

## Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

## Environment Variables

For the PostgreSQL version, create a `.env` file based on `.env.example` and configure your database credentials.

Do not upload your `.env` file or real database credentials to GitHub.

## Run the Dictionary Version

```bash
python -m uvicorn LibrariApi:app --reload
```

## Run the PostgreSQL Version

```bash
python -m uvicorn LibraryApi:app --reload
```

## API Documentation

After starting the application, open:

http://127.0.0.1:8000/docs
