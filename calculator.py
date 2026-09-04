a=int(input("Enter the first number: "))
op=input("Enter the operator (+, -, *, /): ")
b=int(input("Enter the second number: "))

if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    if b!=0:
        print(a/b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator. Please use +, -, *, or /.")