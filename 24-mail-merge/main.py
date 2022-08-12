#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("input/letters/starting_letter.txt") as data:
    form_letter = data.read()
    for n in names:
        stripped_name = n.strip()
        output_content = form_letter.replace(PLACEHOLDER, stripped_name)
        with open(f"output/readytosend/{stripped_name}.txt", mode="w") as output_letter:
            output_letter.write(output_content)


    