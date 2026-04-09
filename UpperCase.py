# uppercase without method

s = input("Enter text: ")

result = ""

for ch in s:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch)-32)
    else:
        result += ch

print(result)