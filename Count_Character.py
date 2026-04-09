# count character

text = input("Enter text: ")
ch = input("Enter character: ")

count = 0

for c in text:
    if c == ch:
        count += 1

print(count)