import pandas


#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabets = {row.letter: row.code for _, row in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
print("Welcome to the NATO Alphabets converter!")

def nato_alphabets():
    try:
        name = input("Enter a word: ").upper().replace(" ","")
        result = [alphabets[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_alphabets()
    else:
        print(result)
nato_alphabets()
