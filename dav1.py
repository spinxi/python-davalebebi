#---------------------------------------------------- <1> ----------------------------------------------------
#CREATE CALCULATOR 
# Create class Calculator
class Calculator:
    # Assign values to object   
    def __init__(numbers, x, y):
        numbers.x = x
        numbers.y = y
    # Create function that makes operations
    def calculateIt(calcNumbers):
        print('Sum is: ', calcNumbers.x + calcNumbers.y)
        print('Subtract is: ', calcNumbers.x - calcNumbers.y)
        print('Multiply is: ', calcNumbers.x * calcNumbers.y)
        print('Divide is: ', calcNumbers.x / calcNumbers.y)
# Create an empty list for input numbers
calculatorList = []
# Create loop for input to run two times
for i in range(2):
    i+=1
    inputNumbers = int(input('Submit your {} number: '.format(i)))
    calculatorList.append(inputNumbers)
# Assign lists to values
x = calculatorList[0]
y = calculatorList[1]
# Create an object and assign values for calculating
calculator = Calculator(x, y)
# Call the calculator function for makin' operations
calculator.calculateIt()
#OKAY THAT'S IT
#---------------------------------------------------- </1> ----------------------------------------------------

# #---------------------------------------------------- <2> ----------------------------------------------------
# #CREATE EMPLOYEE LIST FILTERS & SO ON
# # Import CSV library for workin' on .csv format files
# import csv
# # Create class Calculator
# class Employee:
#     # Assign values to object   
#     def __init__(data, name, surname, age, salary):
#         data.name = name
#         data.surname = surname
#         data.age = age
#         data.salary = salary
#     # Create first function
#     def printingLowest(dataRead):
#         print('The poorest employer is:', dataRead.name, dataRead.surname, ', Age:', dataRead.age, ', Salary:', dataRead.salary, 'GEL')
#     # Create first function    
#     def printingOldest(dataRead):
#         print('The oldest employer is:', dataRead.name, dataRead.surname, ', Salary:', dataRead.salary, 'GEL')
# # Let's open our .csv file
# with open('data.csv') as csvFile:
#     # Create dictreader object
#     reader = csv.DictReader(csvFile)
#     # Create lists to appent infos in here
#     name = []
#     surname = []
#     age = []
#     salary = []
#     # Create for loop for reading columns & appending it in .csv file
#     for col in reader:
#         name.append(col['name'])
#         surname.append(col['surname'])
#         age.append(col['age'])
#         salary.append(col['salary'])
# # Let's find out min salary index in list to set the index for every list to take the info
# indexMinSalary = salary.index(min(salary))
# minSalary = Employee(name[indexMinSalary], surname[indexMinSalary], age[indexMinSalary], salary[indexMinSalary])
# # Call the function to print it
# minSalary.printingLowest()
# # Let's find out max age index in list to set the index for every list to take the info
# indexMaxAge = age.index(max(age))
# maxAge = Employee(name[indexMaxAge], surname[indexMaxAge], age[indexMaxAge], salary[indexMaxAge])
# # Call the function to print it
# maxAge.printingOldest()
# #OKAT THAT'S IT
# #---------------------------------------------------- </2> ----------------------------------------------------
