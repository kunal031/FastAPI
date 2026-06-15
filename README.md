# FastAPI Learning

A small FastAPI project for learning API development with FastAPI, Pydantic, SQLAlchemy, and a relational database.

The app exposes basic product CRUD endpoints and initializes the database with sample product data when the table is empty.

## Features

- FastAPI application with automatic Swagger docs
- Pydantic models for request validation
- SQLAlchemy database models and sessions
- Product listing, creation, update, and deletion endpoints
- Sample product data inserted on first startup

## Project Structure

```text
.
├── main.py
├── models.py
├── database_models.py
├── database_config.py
└── requirements.txt
```

## Requirements

- Python 3.11+
- PostgreSQL or another SQLAlchemy-supported database

## Setup

Create and activate a virtual environment:

```bash
python -m venv myenv
source myenv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
DB_URL=postgresql://username:password@localhost:5432/database_name
```

Replace the username, password, host, port, and database name with your local database details.

## Run the App

```bash
uvicorn main:app --reload
```

Open the API docs:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Welcome message |
| `GET` | `/products` | Get all products |
| `GET` | `/product/{id}` | Get a product by ID |
| `POST` | `/product` | Add a new product |
| `PUT` | `/product?id={id}` | Update an existing product |
| `DELETE` | `/product?id={id}` | Delete a product |

## Example Product JSON

```json
{
  "id": 1,
  "name": "Phone",
  "description": "Budget phone",
  "price": 99.0,
  "quantity": 10
}
```

## Notes Before Pushing to GitHub

Do not commit local-only files such as:

```text
myenv/
__pycache__/
.DS_Store
.env
```

Add those entries to `.gitignore` before pushing the project.
