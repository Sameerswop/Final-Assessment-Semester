rivers = {
    'Chari': 'Chad',
    'Thames': 'England',
    'Río de la Plata': 'Argentina'
    } #variable "rivers" is stored data including 'Chari', 'Thames', 'Río de la Plata' and their data

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.") #prints the river names and country

print("\nThis dictionary includes the following rivers:") #prints the statement in this line
for river in rivers.keys():
    print(f"- {river.title()}")  #prints the river names

print("\nThis dictionary includes the following countries:") #prints the statement in this line
for country in rivers.values():
    print(f"- {country.title()}") #prints the country names