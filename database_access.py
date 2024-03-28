import json
from collections import UserDict
from datetime import date


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

    # These are required:
    # "name": str, "ingredients": list[str], "minutes_to_make": int, "date_last_eaten": date
    # These are only required if they are turned on in settings, and are on a scale of 0 to 20
    # "food_rating": int, "health_rating": int
    def recipe_is_valid(self, recipe: dict) -> bool:
        if "name" not in recipe:
            return False
        elif recipe["name"] is not str:
            return False

        elif "ingredients" not in recipe:
            return False
        elif recipe["ingredients"] is not list[str]:
            return False

        elif "minutes_to_make" not in recipe:
            return False
        elif recipe["minutes_to_make"] is not int:
            return False

        elif "date_last_eaten" not in recipe:
            return False
        elif recipe["date_last_eaten"] is not date:
            return False

        elif self["settings"]["food_rating_is_stored"] == True:
            if "food_rating" not in recipe:
                return False
            elif recipe["food_rating"] is not int:
                return False
            elif not 0 <= recipe["food_rating"] <= 20:
                return False

        elif self["settings"]["health_rating_is_stored"] == True:
            if "health_rating" not in recipe:
                return False
            elif recipe["health_rating"] is not int:
                return False
            elif not 0 <= recipe["health_rating"] <= 20:
                return False

        else:
            return True

    def add_recipe(self, recipe: dict) -> None:
        self.data["recipes"].append(recipe)

    def remove_recipe(self, recipe_name: str) -> None:
        for recipe_it in range(len(self.data["recipes"])):
            if self.data["recipes"][recipe_it]["name"] == recipe_name:
                del self.data["recipes"][recipe_it]


# Code for testing
if __name__ == "__main__":
    pass
