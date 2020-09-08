'''
# Type of Argument - Variable length
def add(a,b):
    print(a)
    print(b)
    c = a
    for i in b:
        c = c + i
    print("Sum = ",c)
    
add(2,3,4,5)
'''


# Type of Argument - Variable length
def add(a,*b):
    print(a)
    print(b)
    c = a
    for i in b:
        print("Value from tuple: ", i)
        c = c + i
        print("Sum till now: ", c)
    print("Sum = ",c)
    
add(2,3,4,5)







# Type of Argument - Position
'''
def student(name, clas, subj):
    print("Name of student is: ", name)
    print("Class of student is: ", clas)
    print("Number of subjects that the student in class are: ", subj)

student('shanaya', 3, 5)
'''

'''
def default_Args(food="pizza"):
    print("I love eating: "+ food)

default_Args("burger")
default_Args()
default_Args("Rice")
default_Args("food")
'''


'''
def team(mem1, mem2, mem3):
    print("Name of team members is: ",mem1,mem2,mem3)
    
team(mem3 = "rajat", mem1 = "akshay", mem2 = "renu")
'''




'''
def displaying(b):
    print("ID of b: ", id(b))
    b = b+1
    print("ID of updated b: ", id(b))
    print("Value of b: ",b)  

a = 10
print("ID of a: ", id(a))
displaying(a)
print("Value of a: ",a)
'''


'''
def displaying(b):
    print("ID of b: ", id(b))
    b = b+1
    print("Value of b: ",b)  

a = 10
print("ID of a: ", id(a))
displaying(a)
print("Value of a: ",a)
'''


'''
def displaying(b):
    b = b+1
    print("Value inside function: ",b)  

a = 10
displaying(a)
print("Value outside function: ",a)
'''





# Multiple return values
''' 
def add_sub(a,b):
    c = a+b
    d = a-b
    return c,d    

rADD, rSUB = add_sub(3,2)
print("Sum is =", rADD)
print("Difference is =", rSUB)
'''