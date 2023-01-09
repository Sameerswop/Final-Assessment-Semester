sandwich_orders = ['Pastrami', 'Beef', 'Egg', 'Bacon', 'Chicken', 'Pastrami', 'Pastrami'] #variable "sandwich_orders" turns into a list that has 7 items
finished_sandwiches = [] #variable "finished_sandwiches" turns into an empty list

print("It's rather unfortunate, but we have run out of pastrami today.") #prints the statement in this line
while 'Pastrami' in sandwich_orders: 
    sandwich_orders.remove('Pastrami') #removes pastrami from the list "sandwich_orders"

print("\n")
while sandwich_orders: 
    current_sandwich = sandwich_orders.pop() #"current_sandwich" is assigned the retrieved data from "sandwich_orders"
    print(f"Your {current_sandwich} sandwich is being made.") #prints the statement in this line and the data in "current_sandwich"
    finished_sandwiches.append(current_sandwich) #adds the data stored in "current_sandwich" to the list "finished_sandwiches"

print("\n")
for sandwich in finished_sandwiches:
    print(f"The {sandwich} sandwich is finished.") #prints the statement in this line and the words in the list "finished_sandwiches"