from database_access import *


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
    raw_command: str = input("type in your command:  ")
    final_command: str = ""
    for char in range(len(raw_command)):
        if raw_command[char] == " ":
            pass
        else:
            final_command += raw_command[char]

    try:
        eval(f"command_{final_command}()")
    except SyntaxError:
        print(f"{final_command} is not a command")

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
        quit (quits the program)
        """
    )


##############################################################################
# Commands
##############################################################################
def command_decide() -> None:
    pass


def command_add() -> None:
    pass


def command_delete() -> None:
    pass


def command_find() -> None:
    pass


def command_change() -> None:
    pass


def command_eat() -> None:
    pass


def command_show() -> None:
    pass


def command_modify() -> None:
    pass


def command_quit() -> None:
    print("Quitting program")
    quit()


##############################################################################
#
##############################################################################
if __name__ == "__main__":
    main()
    print(ask_for_command())
