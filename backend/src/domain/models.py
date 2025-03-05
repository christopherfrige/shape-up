from datetime import datetime
from enum import Enum
from typing import List, Optional

from infrastructure.database.base import Base
from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy import (
    Enum as SQLEnum,
)
from sqlalchemy.orm import relationship


class ActivityLevel(str, Enum):
    SEDENTARY = "sedentary"
    LIGHTLY_ACTIVE = "lightly_active"
    MODERATELY_ACTIVE = "moderately_active"
    VERY_ACTIVE = "very_active"
    EXTRA_ACTIVE = "extra_active"


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class FoodCategory(str, Enum):
    FRUITS = "fruits"
    VEGETABLES = "vegetables"
    MEATS = "meats"
    DAIRY = "dairy"
    GRAINS = "grains"
    SNACKS = "snacks"
    BEVERAGES = "beverages"
    OTHER = "other"


class ExerciseCategory(str, Enum):
    STRENGTH = "strength"
    CARDIO = "cardio"
    FLEXIBILITY = "flexibility"
    BALANCE = "balance"
    CORE = "core"
    OTHER = "other"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    age = Column(Integer)
    weight = Column(Float)
    height = Column(Float)
    gender = Column(SQLEnum(Gender))
    activity_level = Column(SQLEnum(ActivityLevel))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    diets = relationship("Diet", back_populates="user")
    progress = relationship("Progress", back_populates="user")
    workout_plans = relationship("WorkoutPlan", back_populates="user")
    workout_sessions = relationship("WorkoutSession", back_populates="user")


class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    category = Column(SQLEnum(FoodCategory))
    calories_per_serving = Column(Float)
    proteins = Column(Float)
    carbohydrates = Column(Float)
    fats = Column(Float)
    serving_size = Column(Float)
    serving_unit = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    diet_foods = relationship("DietFood", back_populates="food")


class Diet(Base):
    __tablename__ = "diets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    description = Column(String)
    daily_calories = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="diets")
    diet_foods = relationship("DietFood", back_populates="diet")
    meal_plans = relationship("MealPlan", back_populates="diet")


class DietFood(Base):
    __tablename__ = "diet_foods"

    id = Column(Integer, primary_key=True, index=True)
    diet_id = Column(Integer, ForeignKey("diets.id"))
    food_id = Column(Integer, ForeignKey("foods.id"))
    quantity = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    diet = relationship("Diet", back_populates="diet_foods")
    food = relationship("Food", back_populates="diet_foods")


class MealPlan(Base):
    __tablename__ = "meal_plans"

    id = Column(Integer, primary_key=True, index=True)
    diet_id = Column(Integer, ForeignKey("diets.id"))
    day_of_week = Column(Integer)  # 0-6 for Monday-Sunday
    meal_type = Column(String)  # breakfast, lunch, dinner, snack
    created_at = Column(DateTime, default=datetime.utcnow)

    diet = relationship("Diet", back_populates="meal_plans")
    meal_foods = relationship("MealFood", back_populates="meal_plan")


class MealFood(Base):
    __tablename__ = "meal_foods"

    id = Column(Integer, primary_key=True, index=True)
    meal_plan_id = Column(Integer, ForeignKey("meal_plans.id"))
    food_id = Column(Integer, ForeignKey("foods.id"))
    quantity = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    meal_plan = relationship("MealPlan", back_populates="meal_foods")
    food = relationship("Food")


class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime, default=datetime.utcnow)
    weight = Column(Float)
    body_fat_percentage = Column(Float, nullable=True)
    chest_circumference = Column(Float, nullable=True)
    waist_circumference = Column(Float, nullable=True)
    hip_circumference = Column(Float, nullable=True)
    bicep_circumference = Column(Float, nullable=True)
    thigh_circumference = Column(Float, nullable=True)
    notes = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="progress")


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    category = Column(SQLEnum(ExerciseCategory))
    muscle_groups = Column(JSON)  # List of muscle groups targeted
    equipment_needed = Column(JSON)  # List of required equipment
    difficulty_level = Column(Integer)  # 1-5 scale
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    workout_exercises = relationship("WorkoutExercise", back_populates="exercise")
    exercise_sets = relationship("ExerciseSet", back_populates="exercise")


class WorkoutPlan(Base):
    __tablename__ = "workout_plans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    description = Column(Text)
    difficulty_level = Column(Integer)  # 1-5 scale
    estimated_duration = Column(Integer)  # in minutes
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="workout_plans")
    workout_exercises = relationship("WorkoutExercise", back_populates="workout_plan")
    workout_sessions = relationship("WorkoutSession", back_populates="workout_plan")


class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    id = Column(Integer, primary_key=True, index=True)
    workout_plan_id = Column(Integer, ForeignKey("workout_plans.id"))
    exercise_id = Column(Integer, ForeignKey("exercises.id"))
    sets = Column(Integer)
    reps = Column(Integer)
    weight = Column(Float, nullable=True)
    rest_time = Column(Integer)  # in seconds
    notes = Column(Text, nullable=True)
    order = Column(Integer)  # For maintaining exercise order in the plan
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    workout_plan = relationship("WorkoutPlan", back_populates="workout_exercises")
    exercise = relationship("Exercise", back_populates="workout_exercises")


class WorkoutSession(Base):
    __tablename__ = "workout_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    workout_plan_id = Column(Integer, ForeignKey("workout_plans.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime, nullable=True)
    duration = Column(Integer, nullable=True)  # in minutes
    notes = Column(Text, nullable=True)
    rating = Column(Integer, nullable=True)  # 1-5 scale
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="workout_sessions")
    workout_plan = relationship("WorkoutPlan", back_populates="workout_sessions")
    exercise_sets = relationship("ExerciseSet", back_populates="workout_session")


class ExerciseSet(Base):
    __tablename__ = "exercise_sets"

    id = Column(Integer, primary_key=True, index=True)
    workout_session_id = Column(Integer, ForeignKey("workout_sessions.id"))
    exercise_id = Column(Integer, ForeignKey("exercises.id"))
    set_number = Column(Integer)
    reps = Column(Integer)
    weight = Column(Float, nullable=True)
    duration = Column(Integer, nullable=True)  # in seconds
    distance = Column(Float, nullable=True)  # in meters
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    workout_session = relationship("WorkoutSession", back_populates="exercise_sets")
    exercise = relationship("Exercise", back_populates="exercise_sets")
