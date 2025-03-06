from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query

from src.application.use_cases.progress.create_progress_use_case import (
    CreateProgressUseCase,
)
from src.application.use_cases.progress.delete_progress_use_case import (
    DeleteProgressUseCase,
)
from src.application.use_cases.progress.get_progress_use_case import GetProgressUseCase
from src.application.use_cases.progress.list_progress_use_case import ListProgressUseCase
from src.application.use_cases.progress.update_progress_use_case import (
    UpdateProgressUseCase,
)
from src.domain.schemas import Progress, ProgressCreate, ProgressUpdate
from src.infrastructure.database.manager import UnitOfWork

router = APIRouter()


@router.post("/", response_model=Progress)
def create_progress(
    progress: ProgressCreate,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = CreateProgressUseCase(session)
        return use_case.execute(progress)


@router.get("/{progress_id}", response_model=Progress)
def get_progress(
    progress_id: int,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = GetProgressUseCase(session)
        progress = use_case.execute(progress_id)
        if not progress:
            raise HTTPException(status_code=404, detail="Progress not found")
        return progress


@router.get("/", response_model=List[Progress])
def list_progress(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = ListProgressUseCase(session)
        return use_case.execute(skip=skip, limit=limit)


@router.put("/{progress_id}", response_model=Progress)
def update_progress(
    progress_id: int,
    progress: ProgressUpdate,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = UpdateProgressUseCase(session)
        updated_progress = use_case.execute(progress_id, progress)
        if not updated_progress:
            raise HTTPException(status_code=404, detail="Progress not found")
        return updated_progress


@router.delete("/{progress_id}")
def delete_progress(
    progress_id: int,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = DeleteProgressUseCase(session)
        if not use_case.execute(progress_id):
            raise HTTPException(status_code=404, detail="Progress not found")
        return {"message": "Progress deleted successfully"}
