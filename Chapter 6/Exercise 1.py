prompt = "\nWhat topping would you like on your pizza?" #variable "prompt" is given the statement in this line
prompt += "\nEnter 'quit' when you are finished: " #variable "prompt" is also given the statement in this line

while True: #while loop becomes true
    topping = input(prompt) #prints prompt variable and the user has to input their answer
    if topping != 'quit': #if the user inputs an answer that is not "quit"
        print(f"Your pizza will now have {topping} included.") #prints the statement in this list and the "topping" variable
        print("")
    else:
        break #ends the code