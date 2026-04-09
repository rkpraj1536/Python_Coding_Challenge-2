# replace vowels with astric mark

s = input("Enter text: ")

result = ""

for ch in s:
    if ch in "aeiouAEIOU":
        result += "*"
    else:
        result += ch

print(result)