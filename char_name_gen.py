# Welcome on the Character name generator.
# Info : This is a generator who will create and give you a random character name.
import random

def generate_char_name(race):
    if race == "Human":
        race_name = ['Alice', 'Alexandra', 'John', 'Jane', 'Bob', 'Michael', 'Robert', 'Sara', 'Mike']
    elif race == "Elves":
        race_name = ["Legolas", "Arwen", "Glorfindel", "Elrond", "Galadriel", "Haldir"]
    elif race == "Mage":
        race_name = ['Aria', 'Elora', 'Galen', 'Saruman', 'Isadora', 'Lysander']
    elif race == "dwarf":
        race_name = ['Gimli', 'Thorin', 'Balin', 'Fili', 'Kili', "Gloin", "Dwalin"]
    elif race == "Dragon":
        race_name = ['Smaug', 'Vermithraxn', 'Spyro', 'Toothless', 'Shimmer', 'Erevan', 'Glaurung']
    elif race == "Druid":
        race_name = ["Merlin", "Gaius", "Mordred", "Morgana", "Gwaine", "Percival", "Alia", "Eira", "Kian"]

    # Generate a random name from the list
    name = random.choice(race_name)
    return name

race = input("Enter the race (Human, Elves, Mage, Dwarf, Dragon, Druid): ")
name = generate_char_name(race)
print("Generated name:", name)
# Info pour update future:
# Allow the user to specify the type of name they want (e.g., fantasy, modern, historical).
# Allow the user to choose whether they want a first name, last name, or both.
# Allow the user to specify the origin of the name (e.g., European, Asian, African).
# Add a feature that generates a random name based on the user's input.
# Consider adding options for generating names for different fictional races or species (e.g., elves, dwarves, dragons).
# Add a feature that allows the user to generate a list of names based on their input.
# to be continue with open ai.