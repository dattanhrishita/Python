
def factorial(num):
    if num == 0 or num == 1: #if num is 0 or 1 , returm 1
        return 1
    else:
        return num * factorial(num - 1) 

# taking input from user
number = int(input("Enter a number: "))

#calcuating the factoial of the enterered number using factorial function
result = factorial(number)

#print the result
print(f"The factorial of ",number, "is : ", result)
