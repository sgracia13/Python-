def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"

#Remember that the function has already been defined above.
#This part runs the definition and plugs numbers directly in 
print "we can just give the function numbers directly:"
cheese_and_crackers(20,30)

#This function is the same as above but it breaks the function down into its individual variables
print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#this just re-states the problem above
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

