
#Creating tuple

tup_a = (2,4,6,8,10)

print("Tuple A = ", tup_a)
#Fetching index values

print("Value at index 1: ", tup_a[1])

print("Value at index 3: ", tup_a[3])

#Trying to edit a value
#tup[3] = 12

#print(tup[3])

# Create a tuple with mixed values

tup_b = ('a',4,'hello',5.5)
print("Tuple B = ", tup_b)


#concatenate two or more tuples

tup_c = tup_a + tup_b

print("Tuple C = ", tup_c)

# Fetch value from the tuple C

print(tup_c[1])


#Operations on tuple
tup_d = (4,6,2,8,2,6)

print("Number of times 5 is there in tuple D - ", tup_d.count(5))

print("Number of times 6 is there in tuple D - ", tup_d.count(6))

print("The first occurance of value '8' is at the index: ", tup_d.index(8))

print("The first occurance of value '2' is at the index: ", tup_d.index(2, 0, ))

print("The first occurance of value '2' (starting with index 3) is at the index: ", tup_d.index(2, 3, ))



