import os
import requests
import sqlite3
import pandas as pd

#/---------------------------------<1>--------------------------/
# შექმენით მონაცემთა ბაზა persons.db. ბაზაში შექმენით ცხრილი employees. employees ცხრილს შეუქმენით ველები:
# სახელი(not null), გვარი, ასაკი, ქალაქი(not null), ანაზღაურება. ბაზაში მონაცემების
# ჩაწერა არ არის სავალდებულო. დაითვალეთ საშუალო ხელფასი თითოეულ ქალაქში და დაბეჭდეთ
# ეკრანზე.(3 ქულა

con = sqlite3.connect('persons.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS employees
               (name TEXT NOT NULL, surname TEXT, age INT, country TEXT NOT NULL, salary INT)''')

cur.execute("INSERT INTO employees VALUES ('გიორგი', 'ქურდაძე', 23, 'თბილისი',2500)")

con.commit()
data_pd = pd.read_sql("""SELECT country AS 'ქალაქი',
        avg(salary) AS 'საშუალო ხელფასი'
        FROM employees
        GROUP BY country;""",con)
print(data_pd)
con.close()
#/---------------------------------</1>--------------------------/





#/---------------------------------<2>--------------------------/
# requests მოდულის გამოყენებით
# https://httpbin.org/image/webp მისამართიდან გადმოწერეთ
# ფაილი და შეინახეთ ფაილურ სისტემაში.(1 ქულა)

url1 = 'https://httpbin.org/image/webp'
r = requests.get(url1, allow_redirects=True)
open('image.png', 'wb').write(r.content)


print("Current working directory: {0}".format(os.getcwd()))


#/---------------------------------</2>--------------------------/



#/---------------------------------<3>--------------------------/
# requests მოდულის გამოყენებით
# https://httpbin.org/post მისამართზე გაგზავნეთ
# ინფორმაცია ავტომანქანის შესახებ: მარკა, მოდელი, მწარმოებელი, ფასი. მნიშვნელობები
# თქვენ შეარჩიეთ.(1 ქულა)

url2 = 'https://httpbin.org/post'
obj = {
    'Mark': 'Ferrari',
    'Model': '812 GTS',
    'Manufacturer': 'Exor',
    'Price': '$500000'
    }

snd_post = requests.post(url2, data = obj)

print(snd_post.text)

#/---------------------------------<3>--------------------------/