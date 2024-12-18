'''
WAP to create dictionaries for below task and perform all the above operations on it.

Each student in a school is associated with their grade.
'''

#crating a dictionary products
students = {
    "Hrishita": "A",
    "Dan": "B",
    "Neil": "O",
    "Matt": "C"
}


#prints the dictionary
print("The students and their grades are :",students)

#price of a specified dictionary value 
print("Grade of hrishita: ",students["Hrishita"])

#storing the value in a variable and displaying  
y=students["Dan"]
print("Grade of Dan :",y)

#Adding new element to the dictionary
students["Renee"]="E"
print("After adding new element: ",students)

#updating a dan's grade
#before updation
print("Grade of Dan before updation :",students["Dan"])

students.update({"Dan":"E"})
print("Grade of Dan after updation: ",students["Dan"])

#finding all keys present in the dictionary
k=students.keys()
print("The keys are : ",k)

#Remove Neil from the dictonary
students.pop("Neil")
print("Dictionary after removing Neil :",students)


#looping over dictionary
for i in students:
    print(i)

#to get keys from the dictionary
for i in students.keys():
     print(i)

#to get values from the dictionary
for i in students.values():
    print(i)
