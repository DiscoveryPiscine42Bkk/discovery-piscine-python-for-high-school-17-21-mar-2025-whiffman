a = int(input("Enter number less than 25 : "))
b = 25
if a < b:
    a = (a)
while a < 25:
    a += 1
    if a == 20:
        continue
    print("Inside the loop, my variable is", a)
else:
    print("Error")