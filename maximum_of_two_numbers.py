def find_maximum(num1, num2):
    #returns maximum of two numbers
    if num1 > num2:
        return num1
    else:
        return num2

# Input two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Find and display the maximum number
maximum = find_maximum(number1, number2)
print(f"The maximum of {number1} and {number2} is {maximum}.")
