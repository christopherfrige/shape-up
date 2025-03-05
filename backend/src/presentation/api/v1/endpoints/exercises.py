from typing import List

from application.use_cases.exercise.create_exercise_use_case import (
    CreateExerciseUseCase,
)
from application.use_cases.exercise.delete_exercise_use_case import (
    DeleteExerciseUseCase,
)
from application.use_cases.exercise.get_exercise_use_case import (
    GetExerciseUseCase,
)
from application.use_cases.exercise.list_exercises_use_case import (
    ListExercisesUseCase,
)
from application.use_cases.exercise.update_exercise_use_case import (
    UpdateExerciseUseCase,
)
from domain.schemas import Exercise, ExerciseCreate, ExerciseUpdate
from fastapi import APIRouter, Depends, HTTPException, Query
from infrastructure.database.manager import UnitOfWork

router = APIRouter()


@router.post("/", response_model=Exercise)
def create_exercise(
    exercise: ExerciseCreate,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = CreateExerciseUseCase(session)
        return use_case.execute(exercise)


@router.get("/{exercise_id}", response_model=Exercise)
def get_exercise(
    exercise_id: int,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = GetExerciseUseCase(session)
        exercise = use_case.execute(exercise_id)
        if not exercise:
            raise HTTPException(status_code=404, detail="Exercise not found")
        return exercise


@router.get("/", response_model=List[Exercise])
def list_exercises(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = ListExercisesUseCase(session)
        return use_case.execute(skip=skip, limit=limit)


@router.put("/{exercise_id}", response_model=Exercise)
def update_exercise(
    exercise_id: int,
    exercise: ExerciseUpdate,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = UpdateExerciseUseCase(session)
        updated_exercise = use_case.execute(exercise_id, exercise)
        if not updated_exercise:
            raise HTTPException(status_code=404, detail="Exercise not found")
        return updated_exercise


@router.delete("/{exercise_id}")
def delete_exercise(
    exercise_id: int,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = DeleteExerciseUseCase(session)
        if not use_case.execute(exercise_id):
            raise HTTPException(status_code=404, detail="Exercise not found")
        return {"message": "Exercise deleted successfully"}
