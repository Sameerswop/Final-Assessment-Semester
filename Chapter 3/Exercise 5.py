guests = ['Rhodge', 'Raze', 'Joseph'] #variable "guests" becomes a list with 3 names

name = guests[0].title() #variable "name" is assigned the first name from the list
print(f"{name}, would you like to go to the party later?") #prints the data stored in the variable "name" and the statement in the same line

name = guests[1].title() #variable "name" is assigned the second name from the list
print(f"{name}, would you like to go to the party later?") #prints the data stored in the variable "name" and the statement in the same line

name = guests[2].title() #variable "name" is assigned the third name from the list
print(f"{name}, would you like to go to the party later?") #prints the data stored in the variable "name" and the statement in the same line

name = guests[1].title() #variable "name" is assigned the second name from the list
print(f"\nThat's unfortunate, {name} said they can't come.") #prints the data stored in the variable "name" and the statement in the same line

del(guests[1]) #deletes the second name in the list
guests.insert(1, 'Kaizer') #inserts a new name to replace the deleted name

name = guests[0].title() #variable "name" is assigned the first name from the list
print(f"\n{name}, would you like to go to the party later?") #prints the data stored in the variable "name" and the statement in the same line

name = guests[1].title() #variable "name" is assigned the new second name from the list
print(f"{name}, would you like to go to the party later?") #prints the data stored in the variable "name" and the statement in the same line

name = guests[2].title() #variable "name" is assigned the third name from the list
print(f"{name}, would you like to go to the party later?") #prints the data stored in the variable "name" and the statement in the same line