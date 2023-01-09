glossary = {
    'variable': 'Variable is a symbolic name that is a reference or pointer to an object. Once an object is assigned to a variable, you can refer to the object by that name.',
    'list': 'List is a command that stores items in one collection.',
    'comment': 'Commenting is when a person adds something like a note to explain what the code is doing or whatever they would like to comment.',
    'loop': 'Loops are a repetition of a command until a certain input is given.',
    'string': 'Strings are used for storing characters.',
    'boolean': 'Boolean is used to represent the truth value of an expression',
    'float': 'Float is a numerical value with a decimal component.',
    'arithmetic operators': 'Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication and division.',
    'tuple': 'Tuples are used to store multiple items in a single variable.',
    'arrays': 'Arrays are used to group together similar variables.',
    } #variable "glossary" is stored data including 'variable', 'list', 'comment', 'loop', 'string', 'boolean', 'float', 'arithmetic operators', 'tuple', 'arrays' and their data

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}") #prints the word names and descriptions in the dictionary