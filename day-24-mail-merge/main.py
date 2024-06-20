#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"
destinations = []

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    for name in names:
        name = name.strip()
        destinations.append(name)

#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read().replace("Angela","Ihsan")
    for name in destinations:
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter:
            new_letter = letter_contents.replace(PLACEHOLDER, name)
            letter.write(new_letter)

    