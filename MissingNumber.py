# missing number

lst = [1,2,4,5]

n = len(lst)+1
expected = n*(n+1)//2

actual = sum(lst)

print(expected-actual)