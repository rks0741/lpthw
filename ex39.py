states = {'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}

cities = {
'CA':'San Francisco',
'MI':'Detroit',
'FL':'Jacksonvile',
}

cities['NY'] = "New York"
cities['OR'] = "Portland"

#printing some cities
print('-'*10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states

print('-'*10)
print("Michigan abbreviation is: ", states['Michigan'])
print("Florida abbreviation is: ", states['Florida'])

#Another way to use cities and states
print('-'*10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])


#some testing
print('-'*10)
print(states)
print(states.items())
print(list(states.items()))
list_d = list(states.items())
print(list_d[0][1])

print(list(states['Oregon']))
print('-'*10)


#print every state abbreviation

print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")

#Print every city
print('-'*10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city} ")

#doing both at the same tuime

print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-'*10)
state = states.get('Texas')
if not state:
    print("Sorry, no Texas")

city = cities.get('TX', 'Does not exists')
print(f"The city for the state 'TX' is: {city}")
