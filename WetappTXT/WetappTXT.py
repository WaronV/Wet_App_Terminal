import random 
import datetime
import re
import sys
import mysql.connector

class Dog():
    def __init__ (self,id = " ",name_owner = " ",surname_owner = " ",id_owner = [0], dog_number = 0, name_dog = " ", race_dog = " ", age_dog = 0, date_added = "", visit_history = "", note = "", foto = "" ):
        self.name_owner = name_owner
        self.surname_owner = surname_owner
        self.id_owner = id_owner
        self.dog_number = dog_number
        self.name_dog = name_dog
        self.race_dog = race_dog
        self.age_dog = age_dog
        self.date_added = date_added
        self.visit_history = visit_history
        self.note = note
        self.foto = foto

    def list(self):
        return [self.name_owner, self.surname_owner, self.id_owner, self.dog_number, self.name_dog, self.race_dog, self.age_dog, self.date_added]

    def add_dog(self):

        self.name_owner = input("Enter the name of the owner: ").lower()
        self.surname_owner = input("Enter the surname of the owner: ").lower()
        self.id_owner = check_id()
        self.dog_number = draw_number()
        self.name_dog = input("Enter the dog's name: ").lower()
        self.race_dog = input("Enter the dog's race: ").lower()
        self.age_dog = input("Enter the dog's age: ")
        self.date_added=datetime.date.today()

    def __str__ (self):
        return "Name owner:" + self.name_owner + "\nSurname owner:" + self.surname_owner + "\nID number owner:" + self.id_owner + "\nNumber dog:" + self.dog_number + "\nName dog:" + self.name_dog + "\nRace dog:" + self.race_dog + "\nAge dog:" + self.age_dog + "\nDate added:" + str(self.date_added) + "\n/\n"

    def load_dogs(self):
        cnx = mysql.connector.connect(host='localhost', user='root', password='1234567', database='wet_app1')
        return cnx

def info(z):
    mycursor = cnx.cursor(buffered=True)
    mycursor.execute("SELECT * FROM wet_app1 WHERE dog_number = %s", (z,))
    result = mycursor.fetchall()
    print(result)

def check_id():
    while True:
        n = input("Enter the ID number of the owner: ")
        if (len(n) != 11):
           print("Wrong ID number")
           continue
        mycursor = cnx.cursor(buffered=True)
        mycursor.execute("SELECT id_owner, COUNT(*) FROM wet_app1 WHERE id_owner = %s GROUP BY id_owner", (n,))
        row_count = mycursor.rowcount
        if (not n.isnumeric()):
            print("Wrong ID number")
            continue
        else:
            return n

def draw_number():  
    while True:
        tab2 = []
        for i in range(0,6):
            tab2.append(random.randint(0,9))
        tab2 = "".join([str(elm) for elm in tab2])
        mycursor = cnx.cursor(buffered=True)
        mycursor.execute("SELECT dog_number, COUNT(*) FROM wet_app1 WHERE dog_number = %s GROUP BY dog_number", (tab2,))
        row_count = mycursor.rowcount
        if (row_count != 0):
            continue
        return tab2

def add_dog():
    zmienna.add_dog()
    x = zmienna.list()
    sql = "INSERT INTO wet_app1 (name_owner, surname_owner, id_owner,  dog_number, name_dog, race_dog, age_dog, date_added) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor = cnx.cursor(buffered=True)
    mycursor.execute(sql, x)
    mycursor.execute("SELECT * FROM wet_app1")
    print("Successful addition of dog!")

def look_for_dog(func):
    while True:
        z = input("Enter the dog's number: ")
        mycursor = cnx.cursor(buffered=True)
        mycursor.execute("SELECT dog_number, COUNT(*) FROM wet_app1 WHERE dog_number = %s GROUP BY dog_number", (z,))
        row_count = mycursor.rowcount
        if (row_count != 0):
            func(z)
            break
        elif z == 'back':
            break
        else: print("Dog don't exist")
    del z

def browse_dogs():
    mycursor = cnx.cursor(buffered=True)
    mycursor.execute("SELECT * FROM wet_app1")
    result = mycursor.fetchall()
    for row in result:
        print(row)

def remove_dog(z):
    mycursor = cnx.cursor(buffered=True)
    mycursor.execute("DELETE FROM wet_app1 WHERE dog_number = %s ", (z,))
    print("Dog was deleted")

def edit_dog(z):
    print("\nWhat do you want to overwrite? \n1) Name owner \n2) Surname owner \n3) ID number owner \n4) Dog name \n5) Dog race \n6) Dog age\n7) visit history \n8) note \n9) name foto \n" )
    x = input()
    if x == "1":
        upgrade(z, "name_owner")
    elif x == "2":
        upgrade(z, "surname_owner")
    elif x == "3":
        upgrade(z, "id_owner")
    elif x == "4":
        upgrade(z, "name_dog")
    elif x == "5":
        upgrade(z, "race_dog")
    elif x == "6":
        upgrade(z, "age_owner")
    elif x == "7":
        upgrade_text(z, "visit_history")
    elif x == "8":
        upgrade_text(z, "note")
    elif x == "9":
        upgrade(z, "age_owner")
    elif z == 'back':
        return
    else:
        print("invalid command")

def upgrade(z, col):
    if col == "id_owner":
        var = check_id()
    elif z == 'back':
        return
    else:
        var = input("\n new value :")
    func = f"UPDATE wet_app1 SET {col} = %s WHERE dog_number = %s "
    mycursor = cnx.cursor(buffered=True)
    mycursor.execute(func, ( var, z,))

def upgrade_text(z, col):
    print("\n What you want to do? \n a) rewrite \n b) add text \n")
    func = f"UPDATE wet_app1 SET {col} = %s WHERE dog_number = %s"
    func1 = f"SELECT {col} FROM wet_app1 WHERE dog_number = %s"
    while True:
        x = input()
        if x == "a":
            var = input("\n new value :")
            mycursor = cnx.cursor(buffered=True)
            mycursor.execute(func, (var, z,))
            break

        elif x == "b":
            var = input("\n new value :")
            mycursor = cnx.cursor(buffered=True)
            mycursor.execute(func1, (z,))
            result = mycursor.fetchall()
            print(result)
            origin = result[0]
            var = str(origin[0]) + ";" + var
            mycursor.execute(func, (var, z,))
            break

        elif z == 'back':
            break

        else:
            print("invalid command")

def func_exit():
    while True:
        x = input("a) save \nb) don't save \nc) cancel \n").lower()
        if x == "a":
            cnx.commit()
            sys.exit(0)
        elif x == "b":
            sys.exit(0)
        elif x == "c":
            break
        else:
            print("invalid command")


#--------------------------------------------main menu--------------------------------------------
tab = []

zmienna = Dog()
cnx = zmienna.load_dogs()
while True: #main menu
    x=input("\nWhat you want to do? \na) Add dog \nb) Browse dog \nc) Look for fog \nd) Edit dog \ne) Remove dog\nx) Close app\n").lower()
    if x == "a":
        add_dog()
    elif x == "b":
        browse_dogs()
    elif x == "c":
        look_for_dog(info)
    elif x == "d":
        look_for_dog(edit_dog)
    elif x == "e":
        look_for_dog(remove_dog)
    elif x == "x":
        func_exit()
    else:
        print("invalid command")

#-----------------------------------------------------------------------------------------------------
