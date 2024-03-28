import json
from collections import UserDict


class JsonReaderAndWriter(UserDict):
    def __init__(self, filepath="recipes.json") -> None:
        super().__init__()
        self.filepath: str = filepath
        rawData: str = open(filepath, "r").read()
        self.data = json.loads(rawData)

    def save(self) -> None:
        with open(self.filepath, "w") as outfile:
            new_raw_data = json.dumps(self.data, indent=4)
            outfile.write(new_raw_data)


# Code added when testing the class
if __name__ == "__main__":
    JSON_RW: JsonReaderAndWriter = JsonReaderAndWriter("recipes.json")
    print(JSON_RW)
    print(JSON_RW["recipe2"]["sickos"])
    JSON_RW["recipe2"]["sickos"] = False
    print(JSON_RW)
    JSON_RW.save()
    NEW_JSON_RW: JsonReaderAndWriter = JsonReaderAndWriter("recipes.json")
