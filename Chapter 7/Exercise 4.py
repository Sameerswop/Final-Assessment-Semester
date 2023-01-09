def make_shirt(size='large', message='Hello World!'): #defines the variable "make_shirt(size='large', message='Hello World!'):"
    print(f"\nI'm going to make a {size} t-shirt.") #prints the statement in this line and the variable "size"
    print(f'It will say, "{message}".') #prints the statement in this line and the variable "message"

make_shirt() 
make_shirt(size='medium') #stores the size in this line to "make_shirt"
make_shirt('small', 'Nova') #stores the data in this line to "make_shirt"