import json
from collections import UserDict
from datetime import date


class Recipe(UserDict):
    def __init__(
            self, name: str, ingredients: list[str], minutes_to_make: int, date_last_eaten: date, food_rating: int
    ) -> None:
        super().__init__()
        self.name: str = name
        self.ingredients: list[str] = ingredients
        self.minutes_to_make: int = minutes_to_make
        self.date_last_eaten: date = date_last_eaten

        if 0 <= food_rating <= 20:
            self.food_rating: int = food_rating
        else:
            raise (f"Food rating must be between 0 and 20, while the detected food rating was {food_rating}. Please "
                   f"tell the developer to fix this bug.")


class DatabaseAccesser(UserDict):
    def __init__(self, filepath="recipes.json") -> None:
        super().__init__()
        self.filepath: str = filepath
        rawData: str = open(filepath, "r").read()
        self.data = json.loads(rawData)

    def save(self) -> None:
        with open(self.filepath, "w") as outfile:
            new_raw_data = json.dumps(self.data, indent=4)
            outfile.write(new_raw_data)

    def add_recipe(self, recipe: Recipe) -> None:
        self.data["recipes"].append(
            {
                "name": recipe.name,
                "ingredients": recipe.ingredients,
                "minutes_to_make": recipe.minutes_to_make,
                "date_last_eaten": recipe.date_last_eaten,
                "food_rating": recipe.food_rating
            }
        )

    def remove_recipe(self, recipe_name: str) -> None:
        for recipe_it in range(len(self.data["recipes"])):
            if self.data["recipes"][recipe_it]["name"] == recipe_name:
                del self.data["recipes"][recipe_it]


# Code for testing
if __name__ == "__main__":
    pass
