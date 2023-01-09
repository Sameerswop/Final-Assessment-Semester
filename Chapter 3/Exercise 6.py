guests = ['Rhodge', 'Raze', 'Kaizer', 'Miguel', 'Joseph'] #variable "guests" becomes a list with 5 names

name = guests[0].title() #variable "name" is assigned the first name from the list
print(f"{name}, would you like to go to the party later?") #prints the data stored in the variable "name" and the statement in the same line

name = guests[1].title() #variable "name" is assigned the second name from the list
print(f"{name}, would you like to go to the party later?") #prints the data stored in the variable "name" and the statement in the same line

name = guests[2].title() #variable "name" is assigned the third name from the list
print(f"{name}, would you like to go to the party later?") #prints the data stored in the variable "name" and the statement in the same line

name = guests[1].title() #variable "name" is assigned the second name from the list
print(f"\nThat's unfortunate, {name} said they can't come.") #prints the data stored in the variable "name" and the statement in the same line

del(guests[1]) #deletes the second name in the list
guests.insert(1, 'Wade') #inserts a new name to replace the deleted name

name = guests[0].title() #variable "name" is assigned the first name from the list
print(f"\n{name}, would you like to go to the party later?") #prints the data stored in the variable "name" and the statement in the same line

name = guests[1].title() #variable "name" is assigned the second name from the list
print(f"{name}, would you like to go to the party later?") #prints the data stored in the variable "name" and the statement in the same line

name = guests[2].title() #variable "name" is assigned the third name from the list
print(f"{name}, would you like to go to the party later?") #prints the data stored in the variable "name" and the statement in the same line

print("\nI can only invite two people.")

name = guests.pop() #retrieves the final name from the list and assigns it to the variable "name" then deletes it
print(f"I'm sorry, {name.title()} there's no space at the party anymore.") #prints the data stored in the variable "name" and the statement in the same line

name = guests.pop() #retrieves the final name from the list and assigns it to the variable "name" then deletes it
print(f"I'm sorry, {name.title()} there's no space at the party anymore.") #prints the data stored in the variable "name" and the statement in the same line

name = guests.pop() #retrieves the final name from the list and assigns it to the variable "name" then deletes it
print(f"I'm sorry, {name.title()} there's no space at the party anymore.") #prints the data stored in the variable "name" and the statement in the same line

name = guests[0].title() #variable "name" is assigned the first name from the list
print(f"{name}, would you still like to go to the party?") #prints the data stored in the variable "name" and the statement in the same line

name = guests[1].title() #variable "name" is assigned the second name from the list
print(f"{name}, would you still like to go to the party?") #prints the data stored in the variable "name" and the statement in the same line

del(guests[0]) #deletes the first name in the list
del(guests[0]) #deletes the first name in the list

print(guests) #prints the list