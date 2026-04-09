# login validation

user = input("Enter username: ")
pwd = input("Enter password: ")

if user == "admin" and pwd == "1234":
    print("Login Successful")
else:
    print("Login Failed")