import sqlite3
import os

db = sqlite3.connect('CREATE DATABASE IF NOT EXISTS server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE  IF NOT EXISTS users (
NAME TEXT,
AGE Int16,
PHONE TEXT
)""")
db.commit()
while True:
    user_choose = int(input(' Ввыберите действие:\n 1) добавить запись в таблицу\n 2)вывести таблицу \n'))
    if user_choose == 1:
        user_name = input(' Введите имя: ')
        user_age = int(input(' Введите возраст: '))
        user_phone = input(' Введите номер телефона: ')
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_name, user_age, user_phone))
        db.commit()
    elif user_choose == 2:
        for value in sql.execute("SELECT * FROM users"):
            print(value)
    else:
        print("такого варианта не существует")
import os
os.system('cls')