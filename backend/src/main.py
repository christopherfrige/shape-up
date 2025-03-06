import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from infrastructure.config import SETTINGS
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
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {
        "message": "Welcome to ShapeUp API",
        "version": "1.0.0",
        "docs_url": "/api/docs",
        "redoc_url": "/api/redoc",
    }


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        reload=SETTINGS.app_environment == "development",
        port=8000,
    )
