# total bill function

def total_bill(lst):
    total = 0
    for i in lst:
        total += i
    return total
# storing items
items = [100,200,300]
#print total_bill
print(total_bill(items))