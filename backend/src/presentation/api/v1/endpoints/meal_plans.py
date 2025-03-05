from typing import List

from application.use_cases.meal_plan.create_meal_plan_use_case import (
    CreateMealPlanUseCase,
)
from application.use_cases.meal_plan.delete_meal_plan_use_case import (
    DeleteMealPlanUseCase,
)
from application.use_cases.meal_plan.get_meal_plan_use_case import GetMealPlanUseCase
from application.use_cases.meal_plan.list_meal_plans_use_case import (
    ListMealPlansUseCase,
)
from application.use_cases.meal_plan.update_meal_plan_use_case import (
    UpdateMealPlanUseCase,
)
from domain.schemas import MealPlan, MealPlanCreate, MealPlanUpdate
from fastapi import APIRouter, Depends, HTTPException, Query
from infrastructure.database.manager import UnitOfWork
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=MealPlan)
def create_meal_plan(
    meal_plan: MealPlanCreate,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = CreateMealPlanUseCase(session)
        return use_case.execute(meal_plan)


@router.get("/{meal_plan_id}", response_model=MealPlan)
def get_meal_plan(
    meal_plan_id: int,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = GetMealPlanUseCase(session)
        meal_plan = use_case.execute(meal_plan_id)
        if not meal_plan:
            raise HTTPException(status_code=404, detail="Meal plan not found")
        return meal_plan


@router.get("/", response_model=List[MealPlan])
def list_meal_plans(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = ListMealPlansUseCase(session)
        return use_case.execute(skip=skip, limit=limit)


@router.put("/{meal_plan_id}", response_model=MealPlan)
def update_meal_plan(
    meal_plan_id: int,
    meal_plan: MealPlanUpdate,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = UpdateMealPlanUseCase(session)
        updated_meal_plan = use_case.execute(meal_plan_id, meal_plan)
        if not updated_meal_plan:
            raise HTTPException(status_code=404, detail="Meal plan not found")
        return updated_meal_plan


@router.delete("/{meal_plan_id}")
def delete_meal_plan(
    meal_plan_id: int,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = DeleteMealPlanUseCase(session)
        if not use_case.execute(meal_plan_id):
            raise HTTPException(status_code=404, detail="Meal plan not found")
        return {"message": "Meal plan deleted successfully"}
