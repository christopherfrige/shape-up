from typing import List

from application.use_cases.diet.create_diet_use_case import CreateDietUseCase
from application.use_cases.diet.delete_diet_use_case import DeleteDietUseCase
from application.use_cases.diet.get_diet_use_case import GetDietUseCase
from application.use_cases.diet.list_diets_use_case import ListDietsUseCase
from application.use_cases.diet.update_diet_use_case import UpdateDietUseCase
from domain.schemas import Diet, DietCreate, DietUpdate
from fastapi import APIRouter, Depends, HTTPException, Query
from infrastructure.database.manager import UnitOfWork
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=Diet)
def create_diet(
    diet: DietCreate,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = CreateDietUseCase(session)
        return use_case.execute(diet)


@router.get("/{diet_id}", response_model=Diet)
def get_diet(
    diet_id: int,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = GetDietUseCase(session)
        diet = use_case.execute(diet_id)
        if not diet:
            raise HTTPException(status_code=404, detail="Diet not found")
        return diet


@router.get("/", response_model=List[Diet])
def list_diets(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = ListDietsUseCase(session)
        return use_case.execute(skip=skip, limit=limit)


@router.put("/{diet_id}", response_model=Diet)
def update_diet(
    diet_id: int,
    diet: DietUpdate,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = UpdateDietUseCase(session)
        updated_diet = use_case.execute(diet_id, diet)
        if not updated_diet:
            raise HTTPException(status_code=404, detail="Diet not found")
        return updated_diet


@router.delete("/{diet_id}")
def delete_diet(
    diet_id: int,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = DeleteDietUseCase(session)
        if not use_case.execute(diet_id):
            raise HTTPException(status_code=404, detail="Diet not found")
        return {"message": "Diet deleted successfully"}
