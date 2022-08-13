import pandas
nato = pandas.read_csv("nato.csv") #nato is a DataFrame object now


#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {}
for (_, s) in nato.iterrows():
    l = s["letter"]
    c = s["code"]
    nato_dict[l] = c
# print(nato_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
u_input = input("enter a short word (letters only plz): ").upper()
# # new_var = [new_item for x in thing if]
# coded_input = [nato_dict[u] for u in u_input]
# new_var = [new_item for x in thing if]
coded_input = [nato_dict[u] for u in u_input if u in nato_dict]
print(coded_input)
