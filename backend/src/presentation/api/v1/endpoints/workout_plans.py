from typing import List

from application.use_cases.workout.plan.create_plan_use_case import CreatePlanUseCase
from application.use_cases.workout.plan.delete_plan_use_case import DeletePlanUseCase
from application.use_cases.workout.plan.get_plan_use_case import GetPlanUseCase
from application.use_cases.workout.plan.list_plans_use_case import ListPlansUseCase
from application.use_cases.workout.plan.update_plan_use_case import UpdatePlanUseCase
from domain.schemas import WorkoutPlan, WorkoutPlanCreate, WorkoutPlanUpdate
from fastapi import APIRouter, Depends, HTTPException, Query
from infrastructure.database.manager import UnitOfWork
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=WorkoutPlan)
def create_plan(
    plan: WorkoutPlanCreate,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = CreatePlanUseCase(session)
        return use_case.execute(plan)


@router.get("/{plan_id}", response_model=WorkoutPlan)
def get_plan(
    plan_id: int,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = GetPlanUseCase(session)
        plan = use_case.execute(plan_id)
        if not plan:
            raise HTTPException(status_code=404, detail="Workout plan not found")
        return plan


@router.get("/", response_model=List[WorkoutPlan])
def list_plans(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = ListPlansUseCase(session)
        return use_case.execute(skip=skip, limit=limit)


@router.put("/{plan_id}", response_model=WorkoutPlan)
def update_plan(
    plan_id: int,
    plan: WorkoutPlanUpdate,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = UpdatePlanUseCase(session)
        updated_plan = use_case.execute(plan_id, plan)
        if not updated_plan:
            raise HTTPException(status_code=404, detail="Workout plan not found")
        return updated_plan


@router.delete("/{plan_id}")
def delete_plan(
    plan_id: int,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = DeletePlanUseCase(session)
        if not use_case.execute(plan_id):
            raise HTTPException(status_code=404, detail="Workout plan not found")
        return {"message": "Workout plan deleted successfully"}
