# divisible by 3 and 5

n = int(input("Enter payment : ")) # taking number as input
# checking the condition
if n % 3 == 0 and n % 5 == 0:
    print("Yes")
else:
    print("No")