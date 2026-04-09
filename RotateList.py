# rotate list 
#creating a list
lst = [1,2,3]

last = lst[-1]

lst = [last] + lst[:-1]

print(lst)