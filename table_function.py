# Define a function to print the multiplication table of a number
def table(num):
    # Loop through numbers from 1 to 10
    for i in range(1, 11):
        # Print the product of the number with the current value of i
        print(num, "x", i, "=", num * i)

# Prompt the user to input a number
n = int(input("Enter a number: "))

# Call the function to print the table of the entered number
table(n)
