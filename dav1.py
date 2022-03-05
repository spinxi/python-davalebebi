#---------------------------------------------------- <1> ----------------------------------------------------
#CREATE CALCULATOR 
# Create class Calculator
class Calculator:
    # Assign values to object   
    def __init__(numbers, x, y):
        numbers.x = x
        numbers.y = y
    # Create function that makes operations
    def calculateit(calcnumbers):
        print(
            'Sum is:', calcnumbers.x + calcnumbers.y,
            '\nSubtract is:', calcnumbers.x - calcnumbers.y,
            '\nMultiply is:', calcnumbers.x * calcnumbers.y,
            '\nDivide is:', calcnumbers.x / calcnumbers.y
            )
# Create an empty list for input numbers
calculatorlist = []
# Create loop for input to run two times
for i in range(2):
    i+=1
    inputnumbers = int(input('Submit your {} number: '.format(i)))
    calculatorlist.append(inputnumbers)
# Assign lists to values
x = calculatorlist[0]
y = calculatorlist[1]
# Create an object and assign values for calculating
calculator = Calculator(x, y)
# Call the calculator function for makin' operations
calculator.calculateit()
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
    def printing(dataread):
        print(
            'The poorest employer is:', dataread.poorname, dataread.poorsurname, 
            ', Age:', dataread.poorage, 
            ', Salary:', dataread.poorsalary, 'GEL',
            '\nThe oldest employer is:', dataread.oldname, dataread.oldrsurname,
            ', Age:', dataread.oldage,  
            ', Salary:', dataread.oldsalary, 'GEL'
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
indexminsalary = salary.index(min(salary))
indexmaxage = age.index(max(age))
minsalary = Employee(
    # Min salary
    name[indexminsalary], 
    surname[indexminsalary], 
    age[indexminsalary], 
    salary[indexminsalary],
    # Max age
    name[indexmaxage], 
    surname[indexmaxage], 
    age[indexmaxage], 
    salary[indexmaxage]
    )
# Call the function to print it
minsalary.printing()
#---------------------------------------------------- </2> ----------------------------------------------------
