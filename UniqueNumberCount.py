# unique number counter

lst = [1,1,2,3,3]

unique = [] #creating array or storing unique number

for x in lst:
    if x not in unique:
        unique.append(x)

print(len(unique))