# second largest number 

lst = [10,20,5,15]

first = second = -999999

for n in lst:
    if n > first:
        second = first
        first = n
    elif n > second and n != first:
        second = n

print(second)