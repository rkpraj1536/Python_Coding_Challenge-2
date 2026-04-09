# duplicate characters checker

s = input("Enter text: ") # taking text input 

seen = []
dup = []

for ch in s:
    if ch not in seen:
        seen.append(ch)
    elif ch not in dup:
        dup.append(ch)

print(*dup)