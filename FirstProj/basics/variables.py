a,b,c = 'vdf',4,3
print(type(a,b,c))


'''
#Immutable string 2
imm_str = "Strings are immutable in python"
print(len(imm_str))


print(imm_str[2:9])
imm_str[2:9] = 'niceeee'
print(imm_str[2:9])
'''


'''
#Immutable string 1
imm_str = "Strings are immutable"
print(id(imm_str))
imm_str = "Strings are immutable in python"
print(id(imm_str))

print(imm_str)
'''








'''
#global variable
name = "Python"

def new_name():
    print("Programming language: " + name)
    #name = "Java"
    #print("Programming language: " + name)
    
new_name()
'''




'''
#global variable
name = "Python"

def new_name():
    global name
    print("Programming language: " + name)
    name = "Java"
    print("Programming language: " + name)
    
new_name()
print("Programming language: " + name)
'''




'''
print("Here, is my First program")
v = 4;
print("Value of v is: ")
print(v)
'''