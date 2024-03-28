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

    def add_recipe(self, recipe: dict) -> None:
        self.data["recipes"].append(recipe)

    def remove_recipe(self, recipe_name: str) -> None:
        for recipe_it in range(len(self.data["recipes"])):
            if self.data["recipes"][recipe_it]["name"] == recipe_name:
                del self.data["recipes"][recipe_it]


# Code for testing
if __name__ == "__main__":
    pass
