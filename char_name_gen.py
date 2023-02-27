# Welcome on the Character name generator.
# Info : This is a generator who will create and give you a random character name.
import random

def generate_char_name(race,char_type):
    race_name = []
    type_name = []
    if race == "Human":
        race_name = ['Alice', 'Alexandra', 'John', 'Jane', 'Bob', 'Michael', 'Robert', 'Sara', 'Mike']
    elif race == "Elves":
        race_name = ["Legolas", "Arwen", "Glorfindel", "Elrond", "Galadriel", "Haldir"]
    elif race == "Undead":
        race_name = ["Necro", "Lich", "Revenant", "Shade", "Phantasm", "Siren"]
    elif race == "Dwarf":
        race_name = ['Gimli', 'Thorin', 'Balin', 'Fili', 'Kili', "Gloin", "Dwalin"]
    elif race == "Dragon":
        race_name = ['Smaug', 'Vermithraxn', 'Spyro', 'Toothless', 'Shimmer', 'Erevan', 'Glaurung']
    elif race == "Druid":
        race_name = ["Merlin", "Gaius", "Mordred", "Morgana", "Gwaine", "Percival", "Alia", "Eira", "Kian"]

    if char_type == "Apocalypse":
        type_name = ["Asher","Blaze","Cade","Dax","Ember","Fawkes","Gage","Haze","Jagger","Koda","Lark","Maxen","Nero","Phoenix","Raze","Steele","Talon","Vesper","Wolf","Zephyr"]
    elif char_type == "Futuristic":
        type_name = ["Axl","Blade","Cygnus","Dax","Electra","Finn","Galen","Huxley","Jaxson","Kaida","Lumen","Maverick","Nova","Orion","Phoenix","Quasar","Raine","Solaris","Titan","Vega"]

        # Combine the two lists into a single list
    name_list = race_name + type_name

    # Generate a random name from the list
    name = random.choice(name_list)
    return name
# Let the user choose either a race or a type of character
option = input("Please choose between race or type: ")
# Let the user see the list of choice from race or type
if option.lower() == "race":
    print("Race available: Human, Elves, Undead, Dwarf, Dragon, Druid")
    race = input("Race: ")
    name = generate_char_name(race, "")
    print("Generated name:", name)

elif option.lower() == "type":
    print("Type available: Apocalypse, Futuristic")
    char_type = input("Type: ")
    name = generate_char_name("", char_type)
    print("Generated name:", name)
# Info pour update future:
# Allow the user to specify the type of name they want (e.g., fantasy, modern, historical).
# Allow the user to choose whether they want a first name, last name, or both.
# Allow the user to specify the origin of the name (e.g., European, Asian, African).
# Add a feature that generates a random name based on the user's input.
# Consider adding options for generating names for different fictional races or species (e.g., elves, dwarves, dragons).
# Add a feature that allows the user to generate a list of names based on their input.
# to be continue with open ai.
