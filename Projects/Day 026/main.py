import pandas as pd

# TODO 1. Create a dictionary in this format:
data = pd.read_csv("Projects/Day 026/nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (index,row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter Your Name: ").upper()
phonetic = [data_dict[letter] for letter in list(name)]
print(phonetic)
