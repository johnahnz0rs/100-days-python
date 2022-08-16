import pandas
nato = pandas.read_csv("nato.csv") #nato is a DataFrame object now


#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter:row.code for (_, row) in nato.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
u_input = input("enter a short word (letters only plz): ").upper()
coded_input = [nato_dict[u] for u in u_input if u in nato_dict]
print(coded_input)
