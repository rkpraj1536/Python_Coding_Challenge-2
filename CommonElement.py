# common elements checker

a = [1,2,3]
b = [2,3,4]

common = [] #creating a common array for storing common elements
# iterating the arrays for hecking if the eemnt commont or not
for x in a:
    if x in b:
        common.append(x)

print(common)