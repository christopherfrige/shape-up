from src.domain.models import ActivityLevel, Gender


class CaloriesService:
    @staticmethod
    def calculate_bmr(weight: float, height: float, age: int, gender: Gender) -> float:
        """
        Calculate Basal Metabolic Rate using the Mifflin-St Jeor equation
        """
        if gender == Gender.MALE:
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        else:
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
        return round(bmr, 2)

    @staticmethod
    def calculate_tdee(bmr: float, activity_level: ActivityLevel) -> float:
        """
        Calculate Total Daily Energy Expenditure based on activity level
        """
        activity_multipliers = {
            ActivityLevel.SEDENTARY: 1.2,
            ActivityLevel.LIGHTLY_ACTIVE: 1.375,
            ActivityLevel.MODERATELY_ACTIVE: 1.55,
            ActivityLevel.VERY_ACTIVE: 1.725,
            ActivityLevel.EXTRA_ACTIVE: 1.9,
        }
        tdee = bmr * activity_multipliers[activity_level]
        return round(tdee, 2)

    @staticmethod
    def calculate_calorie_goal(tdee: float, goal: str) -> float:
        """
        Calculate daily calorie goal based on weight goal
        """
        goal_adjustments = {
            "weight_loss": -500,  # 500 calorie deficit
            "maintenance": 0,
            "muscle_gain": 500,  # 500 calorie surplus
        }
        if goal not in goal_adjustments:
            raise ValueError("Invalid goal. Must be one of: weight_loss, maintenance, muscle_gain")

        calories = tdee + goal_adjustments[goal]
        return round(calories, 2)
