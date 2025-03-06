from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field

from .models import ActivityLevel, ExerciseCategory, FoodCategory, Gender


class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    age: int = Field(..., gt=0)
    weight: float = Field(..., gt=0)
    height: float = Field(..., gt=0)
    gender: Gender
    activity_level: ActivityLevel


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    age: Optional[int] = Field(None, gt=0)
    weight: Optional[float] = Field(None, gt=0)
    height: Optional[float] = Field(None, gt=0)
    activity_level: Optional[ActivityLevel] = None


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class FoodBase(BaseModel):
    name: str
    category: FoodCategory
    calories_per_serving: float = Field(..., ge=0)
    proteins: float = Field(..., ge=0)
    carbohydrates: float = Field(..., ge=0)
    fats: float = Field(..., ge=0)
    serving_size: float = Field(..., gt=0)
    serving_unit: str


class FoodCreate(FoodBase):
    pass


class FoodUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[FoodCategory] = None
    calories_per_serving: Optional[float] = Field(None, ge=0)
    proteins: Optional[float] = Field(None, ge=0)
    carbohydrates: Optional[float] = Field(None, ge=0)
    fats: Optional[float] = Field(None, ge=0)
    serving_size: Optional[float] = Field(None, gt=0)
    serving_unit: Optional[str] = None


class Food(FoodBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class DietBase(BaseModel):
    name: str
    description: Optional[str] = None
    daily_calories: float = Field(..., ge=0)


class DietCreate(DietBase):
    pass


class DietUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    daily_calories: Optional[float] = Field(None, ge=0)


class Diet(DietBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class DietFoodBase(BaseModel):
    food_id: int
    quantity: float = Field(..., gt=0)


class DietFoodCreate(DietFoodBase):
    pass


class DietFood(DietFoodBase):
    id: int
    diet_id: int
    created_at: datetime
    food: Food

    class Config:
        from_attributes = True


class MealPlanBase(BaseModel):
    day_of_week: int = Field(..., ge=0, le=6)
    meal_type: str


class MealPlanCreate(MealPlanBase):
    pass


class MealPlanUpdate(BaseModel):
    day_of_week: Optional[int] = Field(None, ge=0, le=6)
    meal_type: Optional[str] = None


class MealPlan(MealPlanBase):
    id: int
    diet_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class MealFoodBase(BaseModel):
    food_id: int
    quantity: float = Field(..., gt=0)


class MealFoodCreate(MealFoodBase):
    pass


class MealFood(MealFoodBase):
    id: int
    meal_plan_id: int
    created_at: datetime
    food: Food

    class Config:
        from_attributes = True


class ProgressBase(BaseModel):
    weight: float = Field(..., gt=0)
    body_fat_percentage: Optional[float] = Field(None, ge=0, le=100)
    chest_circumference: Optional[float] = Field(None, gt=0)
    waist_circumference: Optional[float] = Field(None, gt=0)
    hip_circumference: Optional[float] = Field(None, gt=0)
    bicep_circumference: Optional[float] = Field(None, gt=0)
    thigh_circumference: Optional[float] = Field(None, gt=0)
    notes: Optional[str] = None


class ProgressCreate(ProgressBase):
    pass


class ProgressUpdate(ProgressBase):
    weight: Optional[float] = Field(None, gt=0)
    date: Optional[datetime] = None


class Progress(ProgressBase):
    id: int
    user_id: int
    date: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ExerciseBase(BaseModel):
    name: str
    description: str
    category: ExerciseCategory
    muscle_groups: str
    equipment_needed: Optional[str] = None
    difficulty_level: int = Field(..., ge=1, le=5)


class ExerciseCreate(ExerciseBase):
    pass


class ExerciseUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[ExerciseCategory] = None
    muscle_groups: Optional[str] = None
    equipment_needed: Optional[str] = None
    difficulty_level: Optional[int] = Field(None, ge=1, le=5)


class Exercise(ExerciseBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class WorkoutExerciseBase(BaseModel):
    exercise_id: int
    sets: int = Field(..., gt=0)
    reps: int = Field(..., gt=0)
    weight: Optional[float] = Field(None, gt=0)
    rest_time: int = Field(..., ge=0)
    notes: Optional[str] = None
    order: int = Field(..., ge=0)


class WorkoutExerciseCreate(WorkoutExerciseBase):
    pass


class WorkoutExercise(WorkoutExerciseBase):
    id: int
    workout_plan_id: int
    exercise: Exercise

    class Config:
        from_attributes = True


class WorkoutPlanBase(BaseModel):
    name: str
    description: Optional[str] = None
    difficulty_level: int = Field(..., ge=1, le=5)
    estimated_duration: int = Field(..., gt=0)


class WorkoutPlanCreate(WorkoutPlanBase):
    exercises: List[WorkoutExerciseCreate]


class WorkoutPlanUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    difficulty_level: Optional[int] = Field(None, ge=1, le=5)
    estimated_duration: Optional[int] = Field(None, gt=0)


class WorkoutPlan(WorkoutPlanBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    workout_exercises: List[WorkoutExercise]

    class Config:
        from_attributes = True


class ExerciseSetBase(BaseModel):
    exercise_id: int
    set_number: int = Field(..., gt=0)
    reps: int = Field(..., gt=0)
    weight: Optional[float] = Field(None, gt=0)
    duration: Optional[int] = Field(None, gt=0)
    distance: Optional[float] = Field(None, gt=0)
    notes: Optional[str] = None


class ExerciseSetCreate(ExerciseSetBase):
    pass


class ExerciseSet(ExerciseSetBase):
    id: int
    workout_session_id: int
    created_at: datetime
    exercise: Exercise

    class Config:
        from_attributes = True


class WorkoutSessionBase(BaseModel):
    workout_plan_id: int
    notes: Optional[str] = None
    rating: Optional[int] = Field(None, ge=1, le=5)


class WorkoutSessionCreate(WorkoutSessionBase):
    exercise_sets: List[ExerciseSetCreate]


class WorkoutSessionUpdate(BaseModel):
    end_time: Optional[datetime] = None
    duration: Optional[int] = Field(None, gt=0)
    notes: Optional[str] = None
    rating: Optional[int] = Field(None, ge=1, le=5)


class WorkoutSession(WorkoutSessionBase):
    id: int
    user_id: int
    start_time: datetime
    end_time: Optional[datetime] = None
    duration: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    exercise_sets: List[ExerciseSet]
    workout_plan: WorkoutPlan

    class Config:
        from_attributes = True
