# import json

# def load():
#     with open("users.json", "r") as file:
#         print(json.load(file))

# def write(data):
#     with open("users.json", "w") as file:
#         json.dump(data, file, ensure_ascii=False, indent=4)
    
# # load()

# write({"username": "admin1"})
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, username, password, f_name, age, phone, email):
        self.username = username
        self.__password = password
        self.f_name = f_name
        self.age = age
        self.phone = phone
        self.email = email

    def get_info(self):
        text = (f"Username: {self.username}\n"
                f"Password: {self.__password}\n"
                f"Full Name: {self.f_name}\n"
                f"Age: {self.age}\n"
                f"Email: {self.email}")
        return text
    
    @abstractmethod
    def role(self):
        pass
    
    def to_dict(self):
        return {
            "username": self.username,
            "password": self.__password,
            "f_name": self.f_name,
            "age": self.age,
            "email": self.email,
            "phone": self.phone
        }

class Student(User):
    def __init__(self, username, password, f_name, age, phone, email, group):
        super().__init__(username, password, f_name, age, phone, email)
        self.group = group
    
    def get_info(self):
        text = super().get_info()
        text += f"Group: {self.group}"
        print(text)
        
    def role(self):
        return "student"
    
    def to_dict(self):
        data = super().to_dict()
        data["group"] = self.group
        return data
        
class Teacher(User):
    def __init__(self, username, password, f_name, age, phone, email, subject):
        super().__init__(username, password, f_name, age, phone, email)
        self.subject = subject
    
    def get_info(self):
        text = super().get_info()
        text += f"Subject: {self.subject}"
        print(text)
        
    def role(self):
        return "teacher"
    
    def to_dict(self):
        data = super().to_dict()
        data["subject"] = self.subject
        return data

import json

class Storge:
    def __init__(self , filename):
        self.filename = filename

    def load(self):
        with open (self.filename, "r") as file:
            return json.load(file)
    def save(self, data):
        with open(self.filename, "w") as file:
            json.dump(data,  file , ensure_ascii=False , indent= 4) 

    def add_user(self , user):
        data = self.load()
        data[user.username] = user.to_dict()
        self.save(data)
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
class App:
    def __init__(self):
        self.storge = Storge("./users.json")
    def register(self):
        print("Ro'yhatdan o'tish")
        username = input("Yuzerneym:  ")
        password = input("Parol:  ")
        f_name = input("FID: ")
        phone  = input("Telefon raqam:...")
        age = input("Yosh:...")
        email = input("E-mail: ")
        role = input("Tanlang 1)Student 2) Ustoz")

        if role == "1":
            group = input("Gurux: ")
            user = Student(username , password , f_name , age , phone , email , group)
        elif role == "2":
            subject = input("Fan: ")
            user = Teacher(username , password , f_name , age , phone , email , subject)

        self.storge.add_user(user)
    def run(self):
        while True:
            print("1: Registration \n 2: Login \n 3:Exit")
            choice = input("Select: ")
            if choice == "1":
                self.register()
            elif choice == "2":
                print("Login!")
            elif choice == "3":
                print("Xayr")
            break
        

app = App()
app.run()

