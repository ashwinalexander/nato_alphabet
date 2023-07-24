
import pandas as pd

# convert csv to dataframe
nato_data = pd.read_csv("nato_phonetic_alphabet.csv")

# Keyword comprehension + convert dataframe to dict using iterrows()
nato_dict = {row.letter: row.code for (idx,row) in nato_data.iterrows()}

user_name = input("Enter a word:")

# List comprehension with some dict lookups
nato_user_name = [nato_dict[letter.upper()] for letter in user_name]

print(nato_user_name)
