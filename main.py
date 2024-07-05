#TODO: Create a letter using starting_letter.txt 
# for each name in invited_names.txt
# Read name in invited_names.txt

with open("./Input/Names/invited_names.txt") as names:
    invited_names = names.readlines()

# print(invited_names)
# Replace the [name] placeholder with the actual name.
# Read Letter
with open("./Input/Letters/starting_letter.txt") as letter:
    text = letter.read()

# print(text)
for name in invited_names:
    new_name = name.strip()
    new_text = text.replace("[name]", new_name)
    # print(new_text)
    letter_name = f"letter_for_{new_name}.txt"
# Save the letters in the folder "ReadyToSend" .
    with open("./Output/ReadyToSend/" + letter_name, mode="w") as new_letter:
        new_letter.write(new_text)
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp