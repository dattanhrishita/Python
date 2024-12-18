# WAP to check whether the number is even or not.

#taking input from user converting input from string to integer
num= int(input("enter a number:"))

#to check whether the number is even or odd
# when divided by 2 remainder is 0 , the number is even
if(num % 2 ==0):
    print("Number is even") # prints when condition is true
else:
    print("number is odd") # prints when condition is false
