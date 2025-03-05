from typing import List, Optional

from domain.models import WorkoutExercise, WorkoutPlan
from infrastructure.repositories.base_repository import BaseRepository
from sqlalchemy.orm import Session


class WorkoutPlanRepository(BaseRepository[WorkoutPlan]):
    def get_by_user(
        self, db: Session, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[WorkoutPlan]:
        return (
            db.query(WorkoutPlan)
            .filter(WorkoutPlan.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def add_exercise(
        self,
        db: Session,
        workout_plan_id: int,
        exercise_id: int,
        sets: int,
        reps: int,
        weight: Optional[float] = None,
        rest_time: int = 60,
        notes: Optional[str] = None,
        order: Optional[int] = None,
    ) -> WorkoutExercise:
        if order is None:
            # Get the highest order number and increment it
            last_exercise = (
                db.query(WorkoutExercise)
                .filter(WorkoutExercise.workout_plan_id == workout_plan_id)
                .order_by(WorkoutExercise.order.desc())
                .first()
            )
            order = (last_exercise.order + 1) if last_exercise else 0

        workout_exercise = WorkoutExercise(
            workout_plan_id=workout_plan_id,
            exercise_id=exercise_id,
            sets=sets,
            reps=reps,
            weight=weight,
            rest_time=rest_time,
            notes=notes,
            order=order,
        )
        db.add(workout_exercise)
        db.commit()
        db.refresh(workout_exercise)
        return workout_exercise

    def remove_exercise(
        self, db: Session, workout_plan_id: int, exercise_id: int
    ) -> bool:
        workout_exercise = (
            db.query(WorkoutExercise)
            .filter(
                WorkoutExercise.workout_plan_id == workout_plan_id,
                WorkoutExercise.exercise_id == exercise_id,
            )
            .first()
        )
        if not workout_exercise:
            return False
        db.delete(workout_exercise)
        db.commit()
        return True

    def reorder_exercises(
        self, db: Session, workout_plan_id: int, exercise_orders: List[dict]
    ) -> bool:
        for order in exercise_orders:
            workout_exercise = (
                db.query(WorkoutExercise)
                .filter(
                    WorkoutExercise.workout_plan_id == workout_plan_id,
                    WorkoutExercise.id == order["id"],
                )
                .first()
            )
            if not workout_exercise:
                return False
            workout_exercise.order = order["order"]
        db.commit()
        return True


workout_plan_repository = WorkoutPlanRepository(WorkoutPlan)
