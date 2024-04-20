from database_access import *
from datetime import date

DB: DatabaseAccesser = DatabaseAccesser("recipes.json")


##############################################################################
# Main
##############################################################################
def main() -> None:
    intro()
    while True:
        ask_for_command()


##############################################################################
# Processes
##############################################################################
def ask_for_command() -> str:
    command: str = remove_spaces(input("type in your command:  ")).lower()
    if command == "decide":
        command_decide()
    elif command == "add":
        command_add()
    elif command == "delete":
        command_delete()
    elif command == "showrecipes":
        command_show_recipes()
    elif command == "find":
        command_find()
    elif command == "changerecipe":
        command_change_recipe()
    elif command == "eat":
        command_eat()
    elif command == "showsettings":
        command_show_settings()
    elif command == "changesetting":
        command_change_setting()
    elif command == "quit":
        command_quit()
    else:
        print(f"\"{command}\" is not a command")

    return command


def intro() -> None:
    print(
        """
        type in any of the following commands:
        command              description
        _______________      ______________________________________________________
        decide               decide what you should eat today
        add                  adds a new recipe to the list of recipes
        delete               deletes a recipe from the list of recipes
        show recipes         shows all recipes
        find                 finds a recipe from the list of recipes
        change recipe        changes a recipe
        eat                  changes the days since last eaten for a recipe to 0
        show settings        shows settings
        change setting       changes a setting
        quit                 quits the program
        """
    )


def remove_spaces(raw_text: str) -> str:
    final_text: str = ""
    for char in range(len(raw_text)):
        if raw_text[char] == " ":
            pass
        else:
            final_text += raw_text[char]

    return final_text


##############################################################################
# Commands
##############################################################################

# decide what you should eat today
def command_decide() -> None:
    pass


# adds a new recipe to the list of recipes
def command_add() -> None:
    pass


# deletes a recipe from the list of recipes
def command_delete() -> None:
    pass


# shows all recipes
def command_show_recipes() -> None:
    DB.print_all_recipes()
    print("")


# finds a recipe from the list of recipes
def command_find() -> None:
    pass


# changes a recipe
def command_change_recipe() -> None:
    pass


# changes the days since last eaten for a recipe to 0
def command_eat() -> None:
    recipe_name: str = input("What recipe would you like to eat?:  ")
    new_recipe: dict = DB.get_recipe(recipe_name)
    todays_date: str = f"{date.today().year}-{date.today().month}-{date.today().day}"
    todays_date = make_date_standard(todays_date)

    print(todays_date)
    new_recipe["date_last_eaten"] = todays_date
    DB.set_recipe(recipe_name, new_recipe)
    DB.save()


# shows settings
def command_show_settings() -> None:
    print(f"Use taste ratings: {DB.get_setting('taste_rating_is_stored')}")
    print(f"Use health ratings: {DB.get_setting('health_rating_is_stored')}")

    print("")


# changes the settings
def command_change_setting() -> None:
    global DB
    command_show_settings()
    setting_name: str = remove_spaces(input("What setting would you like to change?:  ")).lower()
    if setting_name == "usetasteratings":
        change_to_value: str = remove_spaces(input("What would you like to change it to?:  ")).lower()
        if change_to_value == "true":
            DB.set_setting("taste_rating_is_stored", True)
        elif change_to_value == "false":
            DB.set_setting("taste_rating_is_stored", False)
        else:
            print(f"You cannot change the taste rating to \"{change_to_value}\"")
            return None
    elif setting_name == "usehealthratings":
        change_to_value: str = remove_spaces(input("What would you like to change it to?:  ")).lower()
        if change_to_value == "true":
            DB.set_setting("health_rating_is_stored", True)
        elif change_to_value == "false":
            DB.set_setting("health_rating_is_stored", False)
        else:
            print(f"You cannot change the health rating to \"{change_to_value}\"")
            return None
    else:
        print(f"\"{setting_name}\" is not a valid setting")
        return None

    DB.save()

    command_show_settings()

    print("")


# quits the program
def command_quit() -> None:
    print("Quitting program")
    quit()


##############################################################################
#
##############################################################################
if __name__ == "__main__":
    main()
    print(ask_for_command())
