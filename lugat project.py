import mysql.connector
import os
class Dictionary:
    def __init__(self):
        self.numbers = ["1", "2", "3", "4"]
        self.enter()

    def enter(self):
        self.show()
        which_one = input("select :").strip()
        while which_one not in self.numbers:
            os.system("cls")
            self.show()
            which_one = input("select :").strip()
        self.check(which_one)

    def show(self):
        print(f"""\n\t\t\t\t\t\tPlease select one of this
                        1.append new words
                        2.look words in the dictionary
                        3.search in dictionary
                        4.exit
                """)

    def check(self, which):
        if which == self.numbers[0]:
            self.append()
        elif which == self.numbers[1]:
            self.look()
        elif which == self.numbers[2]:
            self.search()
        elif which == self.numbers[3]:
            self.eksit()

    def append(self):
        english_word = input("Please enter english word :").strip()
        ozbek_word = input("ozbekcha soz kirting :").strip()
        while not ozbek_word or not english_word:
            os.system("cls")
            print("Invalid syntax")
            english_word = input("Please enter english word :")
            ozbek_word = input("ozbekcha soz kirting :")
        word = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345678",
            database="users"
        )
        project = word.cursor()
        project.execute("use dictionary")
        project.execute(f"insert into lugat(english, ozbek) values('{english_word}', '{ozbek_word}')")
        word.commit()
        self.enter()

    def look(self):
        word = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345678",
            database="users"
        )
        project = word.cursor()
        project.execute("use dictionary")
        project.execute("select english, ozbek from lugat")
        korish = project.fetchall()
        print(korish)
        self.enter()

    def search(self):
        self.find_show()
        find = input("select :")
        while find != "1" and find != "2" and find != "3":
            self.find_show()
            find = input("select :")
        self.check_search(find)

    def check_search(self, which):
        if which == "1":
            self.find_id()
        elif which == "2":
            self.find_english_word()
        elif which == "3":
            self.find_ozbek_word()

    def find_id(self):
        from_id = input("Please enter ID which do you want see :")
        while not from_id:
            from_id = input("Please enter ID which do you want see :")
        word = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345678",
            database="users"
        )
        project = word.cursor()
        project.execute("use dictionary")
        istrue = f"select id from lugat where id={from_id}"
        if istrue:
            word = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345678",
                database="users"
            )
            project = word.cursor()
            project.execute("use dictionary")
            project.execute(f"select english, ozbek from lugat where id={from_id}")
            korish = project.fetchall()
            print(korish)
            self.enter()
        else:
            print("This ID hasn't in server")
            self.enter()

    def find_english_word(self):
        from_english_word = input("Please enter english word which do you want see :")
        while not from_english_word:
            from_english_word = input("Please enter english word which do you want see :")
        word = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345678",
            database="users"
        )
        project = word.cursor()
        project.execute("use dictionary")
        istrue = f"select english from lugat where english={from_english_word}"
        if istrue:
            word = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345678",
                database="users"
            )
            project = word.cursor()
            project.execute("use dictionary")
            project.execute(f"select english, ozbek from lugat where english={from_english_word}")
            korish = project.fetchall()
            print(korish)
            self.enter()
        else:
            print("This english word hasn't in server")
            self.enter()

    def find_ozbek_word(self):
        find_ozbek_word = input("Iltimos ozbekcha soz kiriting :")
        while not find_ozbek_word:
            find_ozbek_word = input("Iltimos ozbekcha soz kiriting :")
        word = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345678",
            database="users"
        )
        project = word.cursor()
        project.execute("use dictionary")
        istrue = f"select ozbek from lugat where ozbek={find_ozbek_word}"
        if istrue:
            word = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345678",
                database="users"
            )
            project = word.cursor()
            project.execute("use dictionary")
            project.execute(f"select english, ozbek from lugat where ozbek={find_ozbek_word}")
            korish = project.fetchall()
            print(korish)
            self.enter()
        else:
            print("Bu ozbekcha soz lugatda mavjud emas1")
            self.enter()


    def eksit(self):
        exit()

    def find_show(self):
        print(f"""\t\t\t\t\t\tPlease select one of this
                                1.find with ID
                                2.find with english words
                                3.find with ozbek words
                        """)


users = Dictionary()
