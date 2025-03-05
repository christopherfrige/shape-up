from typing import List

from application.use_cases.food.create_food_use_case import CreateFoodUseCase
from application.use_cases.food.delete_food_use_case import DeleteFoodUseCase
from application.use_cases.food.get_food_use_case import GetFoodUseCase
from application.use_cases.food.list_foods_use_case import ListFoodsUseCase
from application.use_cases.food.update_food_use_case import UpdateFoodUseCase
from domain.schemas import Food, FoodCreate, FoodUpdate
from fastapi import APIRouter, Depends, HTTPException, Query
from infrastructure.database.manager import UnitOfWork
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=Food)
def create_food(
    food: FoodCreate,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = CreateFoodUseCase(session)
        return use_case.execute(food)


@router.get("/{food_id}", response_model=Food)
def get_food(
    food_id: int,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = GetFoodUseCase(session)
        food = use_case.execute(food_id)
        if not food:
            raise HTTPException(status_code=404, detail="Food not found")
        return food


@router.get("/", response_model=List[Food])
def list_foods(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = ListFoodsUseCase(session)
        return use_case.execute(skip=skip, limit=limit)


@router.put("/{food_id}", response_model=Food)
def update_food(
    food_id: int,
    food: FoodUpdate,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = UpdateFoodUseCase(session)
        updated_food = use_case.execute(food_id, food)
        if not updated_food:
            raise HTTPException(status_code=404, detail="Food not found")
        return updated_food


@router.delete("/{food_id}")
def delete_food(
    food_id: int,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = DeleteFoodUseCase(session)
        if not use_case.execute(food_id):
            raise HTTPException(status_code=404, detail="Food not found")
        return {"message": "Food deleted successfully"}
