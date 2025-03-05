from datetime import datetime
from typing import List, Optional

from domain.models import ExerciseSet, WorkoutSession
from infrastructure.repositories.base_repository import BaseRepository
from sqlalchemy import desc
from sqlalchemy.orm import Session


class WorkoutSessionRepository(BaseRepository[WorkoutSession]):
    def get_by_user(
        self, db: Session, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[WorkoutSession]:
        return (
            db.query(WorkoutSession)
            .filter(WorkoutSession.user_id == user_id)
            .order_by(desc(WorkoutSession.start_time))
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_workout_plan(
        self, db: Session, workout_plan_id: int, skip: int = 0, limit: int = 100
    ) -> List[WorkoutSession]:
        return (
            db.query(WorkoutSession)
            .filter(WorkoutSession.workout_plan_id == workout_plan_id)
            .order_by(desc(WorkoutSession.start_time))
            .offset(skip)
            .limit(limit)
            .all()
        )

    def add_exercise_set(
        self,
        db: Session,
        workout_session_id: int,
        exercise_id: int,
        set_number: int,
        reps: int,
        weight: Optional[float] = None,
        duration: Optional[int] = None,
        distance: Optional[float] = None,
        notes: Optional[str] = None,
    ) -> ExerciseSet:
        exercise_set = ExerciseSet(
            workout_session_id=workout_session_id,
            exercise_id=exercise_id,
            set_number=set_number,
            reps=reps,
            weight=weight,
            duration=duration,
            distance=distance,
            notes=notes,
        )
        db.add(exercise_set)
        db.commit()
        db.refresh(exercise_set)
        return exercise_set

    def complete_session(
        self,
        db: Session,
        session_id: int,
        notes: Optional[str] = None,
        rating: Optional[int] = None,
    ) -> Optional[WorkoutSession]:
        session = self.get(db, id=session_id)
        if not session:
            return None

        session.end_time = datetime.utcnow()
        session.duration = int(
            (session.end_time - session.start_time).total_seconds() / 60
        )
        if notes is not None:
            session.notes = notes
        if rating is not None:
            session.rating = rating

        db.commit()
        db.refresh(session)
        return session

    def get_recent_sessions(
        self, db: Session, user_id: int, days: int = 7
    ) -> List[WorkoutSession]:
        start_date = datetime.utcnow() - datetime.timedelta(days=days)
        return (
            db.query(WorkoutSession)
            .filter(
                WorkoutSession.user_id == user_id,
                WorkoutSession.start_time >= start_date,
            )
            .order_by(desc(WorkoutSession.start_time))
            .all()
        )


workout_session_repository = WorkoutSessionRepository(WorkoutSession)
