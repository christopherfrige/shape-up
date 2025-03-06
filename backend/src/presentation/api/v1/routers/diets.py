from fastapi import APIRouter, Depends, HTTPException

from src.application.use_cases.diet.create_diet_use_case import CreateDietUseCase
from src.application.use_cases.diet.delete_diet_use_case import DeleteDietUseCase
from src.application.use_cases.diet.get_diet_use_case import GetDietUseCase
from src.application.use_cases.diet.update_diet_use_case import UpdateDietUseCase
from src.domain.schemas import Diet, DietCreate, DietUpdate
from src.infrastructure.database.manager import UnitOfWork

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
