f = float(input("Enter first number:"))
operator = input("Choose operator ( + - * /): ")
s = float(input("Enter second number: "))
if operator == "+" :
    ans=f+s
    print(f"The answer is {ans}")
elif operator == "-":
    ans = f-s
    print(f"The answer is {ans}")
elif operator == "*":
    ans = f*s
    print(f"The answer is {ans}")
elif operator == "/":
    ans = f/s
    print(f"The answer is {ans}")
else:
    print("Invalid operator")


