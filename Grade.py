# grade system to provide grades based on the obtained marks

marks = int(input("Enter marks: "))
#defining the condition for grades
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("D")