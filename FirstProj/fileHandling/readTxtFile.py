from _socket import close

#Open file
file = open("testFile","r")
    
#Close file
file.close()


'''
#Read file without any inbuilt function
file = open("testFile","r")
for c in file:
    print(c)
'''

'''
#Read file using readlines()

file = open("testFile","r")
counter = file.readlines()
for c in counter:
    print(c.strip())
'''

'''
#Read file using readline()

file = open("testFile","r")
print(file.readline())
'''

'''
#Read file using read()

file = open("testFile","r")
print(file.read())
'''