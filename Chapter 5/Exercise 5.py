pets = [] #the variable "pets" is turned into a list

pet = {
    'Animal type': 'Dog',
    'Name': 'Danny',
    'Owner': 'Jonathan',
} #the variable "pet" is turned into a dictionary
pets.append(pet) #adds the dictionary to the list

pet = {
    'Animal type': 'Cat',
    'Name': 'Nyanko Big',
    'Owner': 'Tada',
} #the variable "pet" is turned into a dictionary
pets.append(pet) #adds the dictionary to the list

pet = {
    'Animal type': 'Dog',
    'Name': 'Bond',
    'Owner': 'Anya',
} #the variable "pet" is turned into a dictionary
pets.append(pet) #adds the dictionary to the list

for pet in pets:
    print(f"\nHere's what I know about {pet['Name'].title()}:") #prints the statement in this line and the name of the pet in each dictionary
    for key, value in pet.items():
        print(f"\t{key}: {value}") #prints the age and animal type the pet is