num1 = float(input("Enter the number 1: "))
num2 = float(input("Enter the number 2: "))

operation = input("enter the operation (+,-,*,%,/,^): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "%":
    result = num1 % num2
elif operation == "/":
    result = num1 / num2
elif operation == "^":
    result = num1 ** num2
else:
    result = "Invalid Input"
print(f"The Answer is {result}")        
                          