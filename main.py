import sqlite3
import keyboard

connection = sqlite3.connect("final.db")
cursor = connection.cursor()
print("Press 1 to add a number\nPress 2 to find a number")
status_for_1 = keyboard.is_pressed("1")
status_for_2 = keyboard.is_pressed("2")
while True:
    if status_for_1 == True:
        name_to_be_added = input("Enter the name of the person").strip()
        number_to_be_added = input("Enter the number of the person")
        cursor.execute("CREATE TABLE IF NOT EXISTS Users(name, number)")
        print("INSERT INTO Users(name, number)VALUES ('" + name_to_be_added + "','" + number_to_be_added + "')")
        cursor.execute(
            "INSERT INTO Users(name, number)VALUES ('" + name_to_be_added + "','" + number_to_be_added + "')")
        '''cursor.execute("INSERT INTO Users (name, number)VALUES ('Pom','9955410708')")'''
        connection.commit()
        break

    elif status_for_2 == True:
        raw_result = cursor.execute("SELECT * FROM USERS")

        finished_result = list(raw_result)

        name_for_search = input("Enter the number you want to search for").lower().strip()

        qualified_words = []
        qualified_numbers = []
        for row in finished_result:
            if name_for_search in str(row[0]).lower():
                qualified_words.append(str(row[0]))
                qualified_numbers.append(str(row[1]).lower())

        if len(qualified_words) > 0:
            i = -1
            for best in qualified_words:
                i = i + 1
                print(qualified_words[i], end=" - ")
                print(qualified_numbers[i])
            break
        else:
            print("Sorry No Matching Contact")
            break
    else:
        status_for_2 = keyboard.is_pressed("2")
        status_for_1 = keyboard.is_pressed("1")



