import datetime #this code imports data for date and time
now = datetime.datetime.now() #the variable "now" has the value of the current date and time
print("Current date and time: ") # this code prints the words "Current date and time: " to the terminal
print(now.strftime("%Y-%m-%d %H:%M:%S")) #this code prints the time with year, month, day, hour, minute, and seconds