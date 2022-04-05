# შექმენით კლასი Fruit, ინიციალიზაციის
# ფუნქციაში განუსაზღვრეთ ორი ატრიბუტი: სახელი და წონა. კლასს გადაუტვირთეთ შეკრების
# ოპერატორი, ისე რომ შეკრების შედეგად შეიკრიბოს მხოლოდ წონები. კლასს გადაუტვირთეთ
# ტოლობის ოპერატორი(==). ტოლობა უნდა დადგინდეს კლასის ატრიბუტით: სახელი. შექმენით კლასის რამდენიმე ობიექტი
# აჩვენეთ რომ ფუნქციონალი გამართულად მუშაობს.(3 ქულა)



class Fruit:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight
    def __add__(self, other):
        x = self._weight + other._weight
        return x
    def __eq__(self, other):
        if(self._name == other._name):
            return "Equal"
        else:
            return "Not equal"


p1 = Fruit(1, 2)
p2 = Fruit(1, 3)
p3 = Fruit(1, 100)
print(p1._weight + p2._weight + p3._weight)
print(p1 == p2 == p3)






# sqlite3 მოდულის გამოყენებით
# შექმენით მონაცემთა ბაზა morty.db. ბაზაში შქმენით ცხრილი ძაღლების შესახებ ინფორმაციის
# შესანახად. ცხრილის შექმნა უნდა იყოს უსაფრთხო.
# ცხრილს უნდა ჰქონდეს 3 ველი: სახელი, ასაკი, ფერი. ველების ტიპები თქვენ შეარჩიეთ.
# ჩაწერეთ რამდენიმე სატესტო ჩანაწერი ცხრილში.(2 ქულა)

# import sqlite3
# import pandas as pd

# connection = sqlite3.connect('Morty.db')
# cursor = connection.cursor()

# CREATE TABLE

# cursor.execute('''CREATE TABLE IF NOT EXISTS Morty
#               (Name TEXT, Age INT, Color TEXT)''')

# INSTERT DATA

# cursor.execute('''
#                 INSERT INTO Morty (Name, Age, Color)
#                 VALUES
#                 ('jack', 3, 'white'),
#                 ('jack', 44, 'black'),
#                 ('lion', 5, 'grey'),
#                 ('biggie', 6, 'red')
#                 ''')

# CHOOSE ROWS

# cursor.execute('''
#           SELECT
#           Name,
#           Age,
#           Color
#           FROM Morty
#           ''')

# USE PANDAS FOR OUTPUT

# df = pd.DataFrame(cursor.fetchall(), columns=['Name','Age','Color'])
# print (df)

# OR USE LEGACY WAY TO DO SO

# data = cursor.execute('''SELECT * FROM Morty''')
# for row in data:
#     print(row)

# connection.commit()
# connection.close()
