from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from infrastructure.database.manager import UnitOfWork
from presentation.api.v1.api import api_router

app = FastAPI(
    title="ShapeUp API",
    description="API for the ShapeUp fitness and nutrition tracking application",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix="/api/v1")


@app.on_event("startup")
async def startup_event():
    # Create database tables
    uow = UnitOfWork()
    uow.create_tables()


@app.get("/")
async def root():
    return {
        "message": "Welcome to ShapeUp API",
        "version": "1.0.0",
        "docs_url": "/api/docs",
        "redoc_url": "/api/redoc",
    }
