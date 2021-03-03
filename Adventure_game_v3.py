import time
import random


# Declare global variables/reset for new game
def set_variables():
    global items
    global monster1
    global monster2
    global location1
    global location2
    global weapon1
    global weapon2
    items = []
    monster1 = random.choice(["Giant Cyclops", "Magical Chimera",
                              "Dark Goblin", "Dark Wizard"])
    monster2 = random.choice(["3-Headed Cerebrus", "Dracula",
                              "Crazy Frankenstein", "Crazy Witch"])
    location1 = random.choice(["Ghostly Mansion", "Spooky Castle"])
    location2 = random.choice(["Dark Cavern", "Haunted Graveyard"])
    weapon1 = random.choice(["Golf Club", "Baseball Bat",
                             "Pair of Scizzors", "Beer Bottle"])
    weapon2 = random.choice(["Thors Hammer", "Sword of Ragnorak",
                             "Iron Mans Machine Gun"])


# Function for starting a new game and resetting variables
def new_game():
    set_variables()
    intro()
    play_game()


# Function for continuing a game, keeping existing variables
def continue_game():
    intro()
    play_game()


# Function to quit game when chosen
def quit_game():
    display("Thanks for playing! See you next time!\n")


def random_string(string):
    index = 0
    output = []
    while index < len(string):
        if string[index:index+10] == "{monster1}":
            output.append(monster1)
            index += 10
        elif string[index:index+10] == "{monster2}":
            output.append(monster2)
            index += 10
        elif string[index:index+11] == "{location1}":
            output.append(location1)
            index += 11
        elif string[index:index+11] == "{location2}":
            output.append(location2)
            index += 11
        elif string[index:index+9] == "{weapon1}":
            output.append(weapon1)
            index += 9
        elif string[index:index+9] == "{weapon2}":
            output.append(weapon2)
            index += 9
        else:
            output.append(string[index])
            index += 1
    output = "".join(output)
    return output


# Defines print and time delay function
def print_sleep(string, pause):
    print(string)
    time.sleep(pause)


# Pause passed to print_sleep and display, set default 1 second
# Can set other strings to have higher or speeds
def display(x, pause=1):
    print_sleep(random_string(x), pause)


# Valid input operator uses == instead of if..in.. want exact answer:
def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 == response:
            return response
        elif option2 == response:
            return response
        else:
            display("Sorry, I don't understand\n")


def intro():
    display("You find yourself standing in a dark forest at night"
            "filled with tall trees and scary shadows .\n", 2)
    display("Rumor has it that a monster is hiding in here,"
            " and has been terrifying the nearby village.\n", 2)


def play_again():
    response = valid_input("Would you like to play again? (y/n)\n", "y", "n")
    if response == "y":
        new_game()
    elif response == "n":
        quit_game()


# Defines inputs/responses/results when player reaches option 1 house
def house(items):
    if "Sword" in items:
        display("You approach the door of the {location1}\n")
        display("You are about to knock when the"
                "door opens and out steps a {monster2}\n")
        display("Eep! This is the {monster2}'s {location1}!\n")
        display("The {monster2} attacks you!\n")
        response = valid_input("Would you like to (1) fight "
                               "or (2) run away?\n", "1", "2")
        if response == "1":
            display("As the {monster2} moves to attack,"
                    " you reveal your new weapon\n", 2)
            display("The {weapon2} shines brightly in your"
                    " hand as you brace yourself for the attack.\n", 2)
            display("But the {monster2} takes one look at "
                    "your shiny new toy and runs aways\n", 2)
            display("You have rid the town of the {monster2}."
                    " You are victorious!\n", 2)
            play_again()
        elif response == "2":
            display("You fled\n", 2)
            continue_game()
    else:
        display("You approach the door of the {location1}\n")
        display("You are about to knock when the door "
                "opens and out steps a {monster1}\n")
        display("The {monster1} attacks you!\n")
        display("You feel a bit under-prepared for this,"
                " with only having a {weapon1}\n")
        response = valid_input("Would you like to "
                               "(1) fight or (2) run away?\n", "1", "2")
        if response == "1":
            display("You do your best...\n", 2)
            display("but your {weapon1} is no match for the {monster1}\n", 2)
            display("You have been defeated", 2)
            play_again()
        elif response == "2":
            display("You fled\n", 2)
            continue_game()


# Defines inputs/responses/results when player reaches option 2 cave
def cave(items):
    if "Sword" in items:
        display("You have returned to the {location2}\n")
        display("There is nothing else here for you to do\n")
        display("You walk back to the dark forest\n")
        continue_game()
    else:
        display("You peer cautiously into the {location2}\n", 2)
        display("It turns out to be only a very small {location2}\n", 2)
        display("Your eye catches a glint of metal behind a rock\n", 2)
        display("You found the {weapon2}\n", 2)
        display("You discard your silly old {weapon1}"
                " and take the {weapon2} with you\n", 2)
        display("You walk back to the dark forest\n", 2)
        items.append("Sword")
        continue_game()


# Defines main game playing function
def play_game():
    display("In front of you is a {location1}.\n")
    display("To your right is a {location2}.\n")
    if "Sword" in items:
        display("In your hand you hold your trusty"
                " (and effective) {weapon2}.\n")
    else:
        display("In your hand you hold your trusty"
                "(but not very effective) {weapon1}.\n")
    display("Enter 1 to knock on the door of the {location1}\n")
    display("Enter 2 to peer into the {location2}\n")
    response = valid_input("What would you like to do?\n", "1", "2")
    if response == "1":
        house(items)
    elif response == "2":
        cave(items)


# Starts game
new_game()
