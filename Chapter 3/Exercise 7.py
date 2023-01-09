world = ['Chad', 'Japan', 'United Arab Emirates', 'United States of America', 'Philippines'] #variable "world" becomes a list with 5 countries

print("Original order:")
print(world) #prints the list its original order

print("\nAlphabetical:")
print(sorted(world)) #prints the list in alphabetical order

print("\nOriginal order:")
print(world) #prints the list in its original order

print("\nReverse alphabetical:")
print(sorted(world, reverse=True)) #prints the list in alphabetical order but in reverse

print("\nOriginal order:")
print(world) #prints the list in its original order

print("\nReversed:")
world.reverse() #makes the list order reversed
print(world) #prints the list in its original order but in reverse

print("\nOriginal order:")
world.reverse() #makes the list order reversed
print(world) #prints the list in its original order

print("\nAlphabetical")
world.sort() #sorts the list order alphabetically
print(world) #prints the list in alphabetical order

print("\nReverse Alphabetical")
world.sort(reverse=True) #reverses the list order
print(world) #prints the list in its original order but in reverse