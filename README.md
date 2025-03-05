# ShapeUp

A comprehensive fitness and wellness application with backend, web frontend, and mobile components.

## Project Structure

```
shape-up/
├── backend/           # FastAPI backend application
│   ├── src/          # Source code
│   │   ├── domain/   # Domain layer (entities, value objects)
│   │   ├── application/ # Application layer (use cases, interfaces)
│   │   ├── infrastructure/ # Infrastructure layer (implementations)
│   │   └── presentation/  # Presentation layer (controllers, DTOs)
│   └── pyproject.toml # Poetry configuration
├── frontend/         # Web frontend (to be implemented)
└── mobile/          # Mobile application (to be implemented)
```

## Backend Setup

The backend is built with FastAPI and follows clean architecture principles.

### Prerequisites

- Python 3.11+
- Poetry (Python dependency manager)

### Installation

1. Install Poetry if you haven't already:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Navigate to the backend directory and install dependencies:
```bash
cd backend
poetry install
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Run the development server:
```bash
poetry run uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`

### Development

- Code formatting: `poetry run ruff format .`
- Linting: `poetry run ruff check .`
- Testing: `poetry run pytest`

## Architecture

The backend follows clean architecture principles with the following layers:
- Domain (entities, value objects)
- Application (use cases, interfaces)
- Infrastructure (implementations, external services)
- Presentation (controllers, DTOs) 