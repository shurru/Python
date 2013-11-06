#create a mapping of state to abb

states = {
	'oregon': 'OR',
	'florida': 'FL', 
	'California': 'CA', 
	'NewYork': 'NY', 
	'Michigan': 'MI',
}
#creates the cities in the states
cities= {
	'CA': 'San Fran', 
	'MI': 'Detroit', 
	'FL': 'Jacksonville', 
}

#add cities
cities ['NY']= 'New York'
cities ['OR']= 'Portland'

#print some 

print '-' *10 #prints the - 10 times
print "New York state has: ", cities['NY']
print "Oregon has : ", cities ['OR']

#print states 

print '-' *20
print "Michigan abbreviated is: " ,states['Michigan']
print "california abbreviated is: " , states['California']

#using the two dicts

print '-' *10
print "Michigan has: ", cities[states["Michigan"]]
print "California has: ", cities[states['California']]

#print abbreviation for every state
print '-' * 10

for state, abr in states.items(): 
	print "%s is abbreviated for %s" %(state, abr)

#print every city in the state
for abr, city in cities.items(): 
	print "%s in in %s" %(city, abr)

print '-' *10 

for state, abbrev in states.items(): 
	print "%s state is abbreviated %s and has city %s" %(state, abbrev, cities[abbrev])

print '-' *10 

state= states.get('Texas', None)

if not state: 
	print "Sorry, no Texas"

city= cities.get('TX', 'Doesnt exist')
print "Te city for the state'TX' is %s" %city
	

