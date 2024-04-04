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
        with open(self.filepath, "w") as out_file:
            new_raw_data = json.dumps(self.data, indent=4)
            out_file.write(new_raw_data)

    def get_setting(self, setting_name: str) -> bool:
        return self.data["settings"][setting_name]

    def set_setting(self, setting_name: str, set_as: bool) -> None:
        self.data["settings"][setting_name] = set_as

    def get_recipe(self, recipe_name: str) -> dict:
        return self.data["recipes"][recipe_name]

    def set_recipe(self, recipe_name: str, set_as: dict) -> None:
        self.data["recipes"][recipe_name] = set_as

    # These are required:
    # "name": str, "ingredients": list[str], "minutes_to_make": int, "date_last_eaten": str (str format "yy-mm-dd")
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
        elif recipe["date_last_eaten"] is not str:
            return False
        elif not (
            recipe["date_last_eaten"][0].isdigit() and recipe["date_last_eaten"][1].isdigit()
            and recipe["date_last_eaten"][3].isdigit() and recipe["date_last_eaten"][4].isdigit()
            and recipe["date_last_eaten"][6].isdigit() and recipe["date_last_eaten"][7].isdigit()
        ):
            return False

        elif self.data["settings"]["food_rating_is_stored"]:
            if "food_rating" not in recipe:
                return False
            elif recipe["food_rating"] is not int:
                return False
            elif not 0 <= recipe["food_rating"] <= 20:
                return False

        elif self.data["settings"]["health_rating_is_stored"]:
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
                return None

    @staticmethod
    def convert_date_string_to_date(date_text: str) -> date:
        date_text = "20" + date_text
        return date(int(date_text[0:4]), int(date_text[5:7]), int(date_text[8:10]))

    @staticmethod
    def __remove_time_of_day_from_date(self, raw_date: str) -> str:
        comma_index: int = raw_date.index(",")
        deconstucted_raw_date: list[str] = list(raw_date)
        for char in range(comma_index, len(raw_date)):
            del deconstucted_raw_date[char]

        final_date: str = ""
        for char in deconstucted_raw_date:
            final_date += char

        return final_date

    @staticmethod
    def __list_ingredients(ingredients: list[str]) -> str:
        ingredient_list: str = ""
        for ingredient in range(len(ingredients) - 1):
            ingredient_list += ingredients[ingredient] + ", "
        ingredient_list += ingredients[len(ingredients) - 1]

        return ingredient_list

    def print_recipe(self, recipe: dict) -> None:
        print(f"{recipe['name']}:")

        ingredients_raw: list[str] = recipe["ingredients"]
        ingredients_listed_out: str = self.__list_ingredients(ingredients_raw)
        print(f"\tingredients: {ingredients_listed_out}")

        print(f"\ttime to make: {recipe['minutes_to_make']} minutes")

        todays_date: date = date.today()
        date_last_eaten: date = self.convert_date_string_to_date(recipe["date_last_eaten"])
        days_since_last_eaten: str = str(abs(date_last_eaten - todays_date))
        print(f"\tdays since last eaten: {days_since_last_eaten}")

        # Check if we have the setting turned on for food rating
        if self.get_setting("food_rating_is_stored"):
            # Check if food rating exists, if so then print it, otherwise, notify the user
            if "food_rating" in recipe:
                print(f"\tfood rating: {recipe['food_rating']}")
            else:
                print(f"\tfood rating: FOOD RATING DOES NOT EXIST FOR THIS RECIPE, OR IS NOT VALID, PLEASE GIVE IT A VALID RATING")

        # Check if we have the setting turned on for health rating
        if self.get_setting("health_rating_is_stored"):
            # Check if food rating exists, if so then print it, otherwise, notify the user
            if "health_rating" in recipe:
                print(f"\thealth rating: {recipe['health_rating']}")
            else:
                print(f"\thealth rating: HEALTH RATING DOES NOT EXIST FOR THIS RECIPE, OR IS NOT VALID, PLEASE GIVE IT A VALID RATING")

    def print_all_recipes(self) -> None:
        for recipe in self.data["recipes"]:
            self.print_recipe(recipe)
            print("\n\n")


# Code for testing
if __name__ == "__main__":
    DB: DatabaseAccesser = DatabaseAccesser()
    DB.print_recipe(
        {
            "name": "Testing Testing",
            "ingredients": ["code", "files", "etc"],
            "minutes_to_make": 3,
            "date_last_eaten": "24-04-03",
            "food_rating": 4,
            "health_rating": 9
        }
    )
