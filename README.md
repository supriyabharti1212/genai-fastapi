# GenAI FastAPI

A GenAI-based FastAPI application that uses an LLM to answer user questions.

## Features

- FastAPI REST API
- Qwen 2.5 3B model via Ollama
- PostgreSQL database
- SQLAlchemy ORM
- Alembic database migrations
- Docker and Docker Compose
- Jenkins CI pipeline
- Automated testing with Pytest

## Tech Stack

- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker
- Docker Compose
- Jenkins
- Pytest
- Ollama
- Qwen 2.5 3B

## Run the Application

Start the application using Docker Compose:

```bash
docker compose up --build
````

The API will be available at:

[http://localhost:8000](http://localhost:8000)

## API Documentation

FastAPI provides interactive API documentation using Swagger UI.

Open:

[http://localhost:8000/docs](http://localhost:8000/docs)

## Run Tests

Run the tests using:

```bash
pytest
```

## Database Migrations

This project uses Alembic for database migrations.

To apply the latest migrations:

```bash
alembic upgrade head
```

## Docker

Build the Docker image:

```bash
docker build -t genai-fastapi .
```

Run the Docker container:

```bash
docker run -p 8000:8000 genai-fastapi
```

## Jenkins CI

Jenkins is used for Continuous Integration.

The Jenkins pipeline performs the following steps:

1. Checkout the code from GitHub
2. Build the Docker image
3. Run automated tests using Pytest
4. Mark the build as SUCCESS or FAILURE

The Jenkins pipeline is defined in:

```text
Jenkinsfile
```

### CI Pipeline Flow

```text
GitHub
   ↓
Jenkins
   ↓
Checkout Code
   ↓
Build Docker Image
   ↓
Run Pytest
   ↓
SUCCESS / FAILURE
```

## Project Structure

```text
genai-fastapi/
├── app/
│   ├── db/
│   │   ├── database.py
│   │   └── models.py
│   └── ...
├── alembic/
├── tests/
│   └── test_basic.py
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── alembic.ini
├── requirements.txt
├── start.sh
└── README.md
```

## Project Status

The Jenkins CI pipeline is successfully configured.

* GitHub integration: Working
* Docker build: Working
* Pytest: Working
* Jenkins CI: Working

## Author

Supriya Bharti
