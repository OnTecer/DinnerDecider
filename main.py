from database_access import *


def main() -> None:
    while True:
        command: str = ask_for_command()


def ask_for_command() -> str:
    raw_command: str = input("type in your command:  ")
    final_command: str = ""
    for char in range(len(raw_command)):
        if raw_command[char] == " ":
            pass
        else:
            final_command += raw_command[char]

    return final_command


def intro() -> None:
    print(
"""
type in any of the following commands:

decide (decide what you should eat today)
add (adds a new recipe to the list of recipes)
delete (deletes a recipe from the list of recipes)
find (finds a recipe from the list of recipes)
change (changes a recipe)
eat (changes the days since last eaten for a recipe to 0)
show (shows settings)
modify (changes the settings)
"""
)


if __name__ == "__main__":
    main()
