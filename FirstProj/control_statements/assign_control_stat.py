'''
#'If' stat - 1
#Print message 'It is an even number!' if the number is even

num = input("Enter a number to verify if it is an even number:")
num = int(num)
if(num%2==0):
    print("It is an even number!")

#'If else' stat - 2
num = input("Enter a number to verify if it is an even or odd number:")
num = int(num)
if(num%2==0):
    print("It is an even number!")
else:
    print("It is an odd number!")

#'If elif else' stat - 3
num = input("Enter a number to find if it is 0, even or odd number:")
num = int(num)
if(num==0):
    print("Number entered is zero!")
elif(num%2==0):
    print("It is an even number!")
else:
    print("It is an odd number!")


#Assign 1 - Check whether a number is positive, negative or zero
num = input("Enter a number to find if it is 0, positive or negative number:")
num = int(num)
if(num==0):
    print("Number is zero")
elif(num>0):
    print("Number is positive")
else:
    print("Number is negative")


#Assign - 3 - Check whether a number is divisible by 2,3,5
num = input("Enter a number: ")
num = int(num)
if(num%2==0):
    print("Number is divisible by 2")
elif(num%3==0):
    print("Number is divisible by 3")
elif(num%5==0):
    print("Number is divisible by 5")


#Assign - 3(Part 2) - Check whether a number is divisible by 2,3,5 (One way)
num = input("Enter a number: ")
num = int(num)
if(num%2==0):
    if(num%3==0):
        if(num%5==0):
            print("Number is divisible by 2,3,5")
    elif(num%5==0):
        print("Number is divisible by 2 and 5 but not 3")
    else:
        print("Number is divisible by 2 but not 3 and 5")
elif(num%3==0):
    if(num%5==0):
        print("Number is divisible by 3 and 5 but not 2")
    else:
        print("Number is divisible by 3 but not 2 and 5")
elif(num%5==0):
    print("Number is divisible by only 5")

#Assign - 3(Part 2) - Check whether a number is divisible by 2,3,5 (Second way)
num = input("Enter a number: ")
num = int(num)

if(num%2==0 and num%3==0 and num%5==0):
    print("Number is divisible by 2,3,5")
elif(num%2==0 and num%3==0 and num%5!=0):
    print("Number is divisible by 2,3")
elif(num%2==0 and num%3!=0 and num%5==0):
    print("Number is divisible by 2,5")
elif(num%2!=0 and num%3==0 and num%5==0):
    print("Number is divisible by 3,5")
elif(num%2==0 and num%3!=0 and num%5!=0):
    print("Number is divisible by 2 only")
elif(num%2!=0 and num%3==0 and num%5!=0):
    print("Number is divisible by 3 only")
elif(num%2!=0 and num%3!=0 and num%5==0):
    print("Number is divisible by 5 only")

'''
#Assign-4 - Check and print the greatest of 3 numbers (use input by user)
num_1 = input("Enter first number: ")
num_1 = int(num_1)
 