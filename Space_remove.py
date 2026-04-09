# remove spaces

s = input("Enter text: ")

result = ""

for ch in s:
    if ch != " ":
        result = result + ch

print(result)