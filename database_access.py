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
    def convert_date_string_to_datetime(date_text: str) -> date:
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
        for ingredient in range(len(ingredients) - 2):
            ingredient_list += ingredients[ingredient] + ", "
        ingredient_list += ingredients[len(ingredients) - 1]

        return ingredient_list

    def print_recipe(self, recipe: dict[str]) -> None:
        name: str = self.data["recipes"][recipe]["name"]
        print(name + ":")

        ingredients_raw: list[str] = self.data["recipes"][recipe]["ingredients"]
        ingredients_listed_out: str = self.__list_ingredients(ingredients_raw)
        print("\t" + "ingredients: " + ingredients_listed_out)

        minutes_to_make: str = str(self.data["recipes"]["minutes_to_make"])
        print("\t" + "time to make: " + minutes_to_make + " minutes")

        todays_date: date = date.today()

        print("\t" + "days since last eaten: " + str(self.data["recipes"][""]))

    def print_all_recipes(self) -> None:
        for recipe in self.data["recipes"]:
            self.print_recipe(recipe)


# Code for testing
if __name__ == "__main__":
    DB: DatabaseAccesser = DatabaseAccesser()
    todayss_date = date.today()
    print(todayss_date, type(todayss_date))
    print(abs(todayss_date - date(2023, 2, 27)))
    print(type(abs(todayss_date - date(2023, 2, 27))))

    print(DB.convert_date_string_to_datetime("21-02-27").month)
