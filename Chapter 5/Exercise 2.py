glossary = {
    'variable': 'Variable is a symbolic name that is a reference or pointer to an object. Once an object is assigned to a variable, you can refer to the object by that name.',
    'list': 'List is a command that stores items in one collection.',
    'comment': 'Commenting is when a person adds something like a note to explain what the code is doing or whatever they would like to comment.',
    'loop': 'Loops are a repetition of a command until a certain input is given.',
    'string': 'Strings are used for storing characters.',
    } #variable "glossary" is stored data including 'variable', 'list', 'comment', 'loop', 'string' and their data
word = 'variable' #word is assigned 'variable
print(f"\n{word.title()}: {glossary[word]}") #prints the title and its description

word = 'list' #word is assigned 'list'
print(f"\n{word.title()}: {glossary[word]}") #prints the title and its description

word = 'comment' #word is assigned 'comment'
print(f"\n{word.title()}: {glossary[word]}") #prints the title and its description

word = 'loop' #word is assigned 'loop'
print(f"\n{word.title()}: {glossary[word]}") #prints the title and its description

word = 'string' #word is assigned 'string
print(f"\n{word.title()}: {glossary[word]}") #prints the title and its description