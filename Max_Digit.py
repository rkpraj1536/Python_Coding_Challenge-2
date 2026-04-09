# max without builtin

nums = [5,8,2]

mx = nums[0]

for n in nums:
    if n > mx:
        mx = n

print(mx)