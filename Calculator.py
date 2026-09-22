num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition: ", num1 + num2)
print("Substraction: ", num1 - num2)
print("Multiplication: ", num1 * num2)

# Yahan check hoga ke kahin doosra number 0 to nahi hai
if num2 != 0:
    print("Division: ", num1 / num2)
else:
    print("Division: Cannot divide by zero!")
