''' Case 1 '''

'''
import array
age = array('i',[34,45])
print(age)
'''

''' Case 2 '''

'''
import array as arr
age = arr('i',[34,12,23,10,14])
print(age)
'''

''' Case 3 '''


import array as arr
age = arr.array('i',[34,12,23,10,14])
print(age)

# Print single value from array
print(age[3])

# Operations on array
# Find length of the array
print("Length of array:", len(age))

# Add/append value
age.append(20)
print(age)

# Append a value at an index
age.insert(0, 30)
print(age)

# Pop an index value
age.pop(2)
print(age)

# Remove an element
age.remove(10)
print(age)

# Reverse array
age.reverse()
print(age)



'''
for i in range (0,len(age)):
    print(age[i], " ")
'''
    
''' Case 4 '''

'''from array import * '''


