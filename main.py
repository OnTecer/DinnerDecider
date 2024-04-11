from database_access import *

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
    try:
        eval(f"command_{command}()")
    except:
        print(f"\"{command}\" is not a command")

    return command


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
        quit (quits the program)
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


# finds a recipe from the list of recipes
def command_find() -> None:
    pass


# changes a recipe
def command_change() -> None:
    pass


# changes the days since last eaten for a recipe to 0
def command_eat() -> None:
    pass


# shows settings
def command_show() -> None:
    print(f"Use taste ratings: {DB.get_setting('taste_rating_is_stored')}")
    print(f"Use health ratings: {DB.get_setting('health_rating_is_stored')}")

    print("")


# changes the settings
def command_modify() -> None:
    global DB
    command_show()
    setting_name: str = remove_spaces(input("What setting would you like to change?:  ")).lower()
    change_to_value: str = remove_spaces(input("What would you like to change it to?:  ")).lower()
    if setting_name == "usetasteratings":
        if change_to_value == "true":
            DB.set_setting("taste_rating_is_stored", True)
        elif change_to_value == "false":
            DB.set_setting("taste_rating_is_stored", False)
        else:
            print(f"You cannot change the taste rating to \"{change_to_value}\"")
            return None
    elif setting_name == "usehealthratings":
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

    command_show()

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
