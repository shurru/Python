cars= 100
space_in_car = 4.0
drivers= 30
passengers= 90
cars_nt_driven= cars- drivers
cars_driven= drivers
carpool_cap= cars_driven* space_in_car
avg_pass_in_car = passengers/cars_driven

#remember the commas. you can put variables between the strings
print "There are", cars, " cars available" 
print "There are only", drivers, " drivers available" 
print "There will be ", cars_nt_driven, "cars empty" 
print "WE can transport", carpool_cap, "ppl today" 
print "We have" , passengers, "passengers to transport"
print "We need to put" , avg_pass_in_car, " passengers in each car"

