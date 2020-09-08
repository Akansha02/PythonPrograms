#Operators
'''
#Assignment operator - 2
#Swap 2 numbers

a,b = 4,5
print("a = ", a)
print("b = ", b)
a = b
b = a
print("a = ", a)
print("b = ", b)


#Swap 2 numbers - Solution 1 (with third variable)

a,b = 4,5
c = None
print("a = ", a)
print("b = ", b)
c = a
a = b
b = c
print("a = ", a)
print("b = ", b)
'''

#Swap 2 numbers - Solution 2 (without using third variable)

a,b = 4,5
print("a = ", a)
print("b = ", b)
a = b + a
b = a - b
a = a - b
print("a = ", a)
print("b = ", b)


'''
#Assignment operator - 1

a,b = 4,5
print(a)
print(b)
print(a,b)



# Arithmetic operator - 1

a = 7
b = 2
print("1: ", a+b)
print("2: ", a-b)
print("3: ", a/b)
print("4: ", a*b)
print("5: ", a//b)
print("6: ", a%b)
print("7: ", a**b)



# Logical operators - 3

a = True
print(a)
print(not(a))
b = False
print(not(b))
a = b
print(a)
a = not(a)
print(a)
print(not(a))

# Logical operators - 2

a = True
print(a)
b = False
print(not(b))
print(a or b)
print(a and b)
a = b
print(a and b)


# Logical operators - 1

a = True
print(a)
print(not(a))
b = False
print(not(b))
a = b
print(not(a))
print(not(b))
'''