#WAP to find whether person is eligible to vote or not.

#taking input from user
age = int(input("Enter your age:"))# converting into integer

#checking whether age is 18 or more than 18
if age >= 18: 
    print("this user is eligible to vote")#prints if age is more or equal to 18
else:
    print("this user cant vote ")#prints if age is less than 18
