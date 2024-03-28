from json_reader import JsonReaderAndWriter
from collections import UserDict
from datetime import date

JSON: JsonReaderAndWriter = JsonReaderAndWriter()

def add_recipe(recipe_name: str, ingredients: str, ) -> None:
    pass


class Recipe(UserDict):
    def __init__(self, name: str, ingredients: list[str], minutes_to_make: int, date_last_eaten: date, food_rating: int) -> None:
        super().__init__()
        self.name: str = name
        self.ingredients: list[str] = ingredients
        self.minutes_to_make: int = minutes_to_make
        self.date_last_eaten: date = date_last_eaten
        if 0 <= food_rating <= 20:
            self.food_rating: int = food_rating
        else:
            raise f"Food rating must be between 0 and 20, while the detected food rating was {food_rating}. Please tell the developer to fix this bug."


