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
        print(
            'Sum is:', calcNumbers.x + calcNumbers.y,
            '\nSubtract is:', calcNumbers.x - calcNumbers.y,
            '\nMultiply is:', calcNumbers.x * calcNumbers.y,
            '\nDivide is:', calcNumbers.x / calcNumbers.y
            )
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




#---------------------------------------------------- <2> ----------------------------------------------------
#CREATE EMPLOYEE LIST FILTERS & SO ON
# Import CSV library for workin' on .csv format files
import csv
# Create class Employee
class Employee:
    # Assign values to object   
    def __init__(data, poorname, poorsurname, poorage, poorsalary, oldname, oldsurname, oldage, oldsalary):
        # Poor
        data.poorname = poorname
        data.poorsurname = poorsurname
        data.poorage = poorage
        data.poorsalary = poorsalary
        # Old
        data.oldname = oldname
        data.oldrsurname = oldsurname
        data.oldage = oldage
        data.oldsalary = oldsalary
    # Create first function
    def printingLowest(dataRead):
        print(
            'The poorest employer is:', dataRead.poorname, dataRead.poorsurname, 
            ', Age:', dataRead.poorage, 
            ', Salary:', dataRead.poorsalary, 'GEL',
            '\nThe oldest employer is:', dataRead.oldname, dataRead.oldrsurname,
            ', Age:', dataRead.oldage,  
            ', Salary:', dataRead.oldsalary, 'GEL'
            )
# Let's open our .csv file
with open('data.csv') as csvFile:
    # Create dictreader object
    reader = csv.DictReader(csvFile)
    # Create lists to appent infos in here
    name = []
    surname = []
    age = []
    salary = []
    # Create for loop for reading columns & appending it in .csv file
    for col in reader:
        name.append(col['name'])
        surname.append(col['surname'])
        age.append(col['age'])
        salary.append(col['salary'])
# Let's find out min & max indexes
indexMinSalary = salary.index(min(salary))
indexMaxAge = age.index(max(age))
minSalary = Employee(
    # Min salary
    name[indexMinSalary], 
    surname[indexMinSalary], 
    age[indexMinSalary], 
    salary[indexMinSalary],
    # Max age
    name[indexMaxAge], 
    surname[indexMaxAge], 
    age[indexMaxAge], 
    salary[indexMaxAge]
    )
# Call the function to print it
minSalary.printingLowest()
#OKAT THAT'S IT
#---------------------------------------------------- </2> ----------------------------------------------------
