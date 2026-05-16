a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if b != 0:   
    if a % b == 0:
        print(f"{a} is divisible by {b}")
    else:
        print(f"{a} is not divisible by {b}")