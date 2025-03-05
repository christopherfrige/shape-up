from typing import List

from application.use_cases.workout.session.create_session_use_case import (
    CreateSessionUseCase,
)
from application.use_cases.workout.session.delete_session_use_case import (
    DeleteSessionUseCase,
)
from application.use_cases.workout.session.get_session_use_case import GetSessionUseCase
from application.use_cases.workout.session.list_sessions_use_case import (
    ListSessionsUseCase,
)
from application.use_cases.workout.session.update_session_use_case import (
    UpdateSessionUseCase,
)
from domain.schemas import WorkoutSession, WorkoutSessionCreate, WorkoutSessionUpdate
from fastapi import APIRouter, Depends, HTTPException, Query
from infrastructure.database.manager import UnitOfWork
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=WorkoutSession)
def create_session(
    session: WorkoutSessionCreate,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = CreateSessionUseCase(session)
        return use_case.execute(session)


@router.get("/{session_id}", response_model=WorkoutSession)
def get_session(
    session_id: int,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = GetSessionUseCase(session)
        workout_session = use_case.execute(session_id)
        if not workout_session:
            raise HTTPException(status_code=404, detail="Workout session not found")
        return workout_session


@router.get("/", response_model=List[WorkoutSession])
def list_sessions(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = ListSessionsUseCase(session)
        return use_case.execute(skip=skip, limit=limit)


@router.put("/{session_id}", response_model=WorkoutSession)
def update_session(
    session_id: int,
    session: WorkoutSessionUpdate,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = UpdateSessionUseCase(session)
        updated_session = use_case.execute(session_id, session)
        if not updated_session:
            raise HTTPException(status_code=404, detail="Workout session not found")
        return updated_session


@router.delete("/{session_id}")
def delete_session(
    session_id: int,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = DeleteSessionUseCase(session)
        if not use_case.execute(session_id):
            raise HTTPException(status_code=404, detail="Workout session not found")
        return {"message": "Workout session deleted successfully"}
