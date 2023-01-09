prompt = "How old are you?" #variable "prompt" is given the statement in this line
prompt += "\nEnter 'quit' when you are finished. " #variable "prompt" is also given the statement in this line

while True: #while loop becomes true
    age = input(prompt) #prints prompt variable and the user has to input their answer
    if age == 'quit': #if the user inputs the word 'quit'
        break #ends the code
    age = int(age)

    if age < 3: #if age is lesser than 3
        print("You get in free!") #prints the statement in this line
        print("")
    elif age <= 12: #if age is lesser than or equal to 12
        print("Your ticket is $10.") #prints the statement in this line
        print("")
    else:
        print("Your ticket is $15.") #prints the statement in this line
        print("")