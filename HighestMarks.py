# highest marks

data = {"A":80,"B":95,"C":78}

top = ""
marks = 0

for k in data:
    if data[k] > marks:
        marks = data[k]
        top = k

print(top)