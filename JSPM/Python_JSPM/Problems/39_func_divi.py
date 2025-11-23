def divide(a, b):
    if b == 0:
        return "Error! Division by zero not allowed."
    return a / b
print("Arithmatic Operations using functions")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Division:", divide(a, b))
