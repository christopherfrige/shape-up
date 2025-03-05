from fastapi import APIRouter
from presentation.api.v1.endpoints import (
    auth,
    diets,
    exercises,
    foods,
    meal_plans,
    progress,
    workout_plans,
    workout_sessions,
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(exercises.router, prefix="/exercises", tags=["exercises"])
api_router.include_router(foods.router, prefix="/foods", tags=["foods"])
api_router.include_router(diets.router, prefix="/diets", tags=["diets"])
api_router.include_router(meal_plans.router, prefix="/meal-plans", tags=["meal-plans"])
api_router.include_router(progress.router, prefix="/progress", tags=["progress"])
api_router.include_router(
    workout_plans.router, prefix="/workout-plans", tags=["workout-plans"]
)
api_router.include_router(
    workout_sessions.router, prefix="/workout-sessions", tags=["workout-sessions"]
)
