# class Person:
#     def __init__(self,name):
#         print("Inside Constructor")
#         self.name = name
#         print('Object initialized')
#     def show(self):
#         print('Hello,my name is ',self.name)
#
#     def __del__(self):
#         print('Inside Destructor')
#         print('Object destroyed')
#
# s1 = Person('ali')
# s1.show()
# # delete object
# del s1

# class Student:
#     def __init__(self,name,age,phone):
#         self.name = name
#         self.age = age
#         self.phone = phone
#
#     def info(self):
#         print(f'name: {self.name} age: {self.age} phone: {self.phone}')
# s1=Student("James",22,"555454564")
# s2=Student("Alan",20,"4567890898")
# data = [s1,s2]
#
# def view_student(s:list):
#     for item in s:
#         item.info()
#
# view_student(data)
#
#
# class Car:
#     total_cars = 0
#
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#         Car.total_cars += 1
#
#     @classmethod
#     def get_total_cars(cls):
#         return f'Total cars: {Car.total_cars}'
# all-class methods
# exam project -

# class MathUtils:
#     @staticmethod
#     def add(a,b):
#         return a+b
#
#     @staticmethod
#     def summ(a:list):
#         return sum(a)
#
# test_obj = MathUtils()
# print(test_obj.add(105,545))


#
# class Product:
#     def __init__(self,title,price,year,type):
#         self.title = title
#         self.price = price
#         self.year = year
#         self.type = " "
#
# class Shop:
#     def __init__(self,name,phone):
#         self.name = name
#         self.phone = phone
#         self.baza = []
#
#
#     def add_water(self):
#         title = input("title:")
#         price = int(input("price:"))
#         year = int(input("year:"))
#         p1 = Product(title,price,year,'water')
#         p1.type = "water"
#         self.baza.append(p1)
#
#     def add_food(self):
#         title = input("title:")
#         price = int(input("price:"))
#         year = int(input("year:"))
#         p2 = Product(title,price,year,"food")
#         p2.type = "food"
#         self.baza.append(p2)
#
#     def add_fruit(self):
#         title = input("title:")
#         price = int(input("price:"))
#         year = int(input("year:"))
#         p3 = Product(title,price,year,"fruit")
#         p3.type = "fruit"
#         self.baza.append(p3)
#     def view_all(self):
#         for item in self.baza:
#             print(f'title: {item.title} price: {item.price} type: {item.type}')
#     def view_water(self):
#         for item in self.baza:
#             if item.type == "water":
#                 print(f'title: {item.title} price: {item.price}')
#     def view_food(self):
#         for item in self.baza:
#             if item.type == "food":
#                 print(f'title: {item.title} price: {item.price}')
#     def view_fruit(self):
#         for item in self.baza:
#             if item.type == "fruit":
#                 print(f'title: {item.title} price: {item.price}')
#
#     def edit_product(self):
#         name = input("Qaysi product ozgartirilsin? ")
#
#         for item in self.baza:
#             if item.title == name:
#                 print("Topildi")
#
#                 new_title = input(f"New title ({item.title}): ")
#                 if new_title != "":
#                     item.title = new_title
#
#                 new_price = input(f"New price {item.price}: ")
#                 if new_price != "":
#                     item.price = int(new_price)
#
#                 new_year = input(f"New year ({item.year}): ")
#                 if new_year != "":
#                     item.year = int(new_year)
#
#                 new_type = input(f"New type ({item.type}): ")
#                 if new_type != "":
#                     item.type = new_type
#
#                 print("Product o'zgartirildi!")
#                 return
#
#
#
#     def delete_product(self):
#             name = input("Qaysi product ochirilsin? ")
#             for item in self.baza:
#                 if item.name == name:
#                     self.baza.remove(item)
#                 else:
#                     print("Product mavjud emas!")
#
# shop1= Shop('shop1',643236787)
#
# def shop_manager(shop:Shop):
#     while True:
#         kod = input(' 1. add water \n 2. add food \n 3. add fruit \n 4. view all \n 5. delete product \n 6. edict product \n 7. exit \n :')
#         if kod == '1':
#             shop.add_water()
#         elif kod == '2':
#             shop.add_food()
#         elif kod == '3':
#             shop.add_fruit()
#         elif kod == '4':
#             shop.view_all()
#         elif kod == '5':
#             shop.delete_product()
#         elif kod == '6':
#             shop.edit_product()
#         elif kod == '7':
#             break
#
# shop_manager(shop1)
# homework - sms manager

class Contact:
    def __init__(self,name,phone,age,email):
        self.name = name
        self.phone = phone
        self.age = age
        self.email = email

class Message:
    def __init__(self,text,receiver:Contact):
        self.text = text
        self.receiver = receiver   # receiver is a Contact object

class SmsManager:
    def __init__(self):
        self.contacts = []
        self.messages = []

    def add_contact(self):
        name = input("Contact Name: ")
        phone = input("Phone: ")
        age = int(input("Age: "))
        email = input("Email: ")
        c = Contact(name,phone,age,email)
        self.contacts.append(c)
        print("Contact added!\n")

    def view_contact(self):
        print("\n--- CONTACTS ---")
        for c in self.contacts:
            print(f'name: {c.name} | phone: {c.phone} ')
        print()

    def add_message(self):
        receiver_name = input("Qaysi kontaktga sms yuborasiz?: ")

        for c in self.contacts:
            if receiver_name == c.name:
                text = input("Text: ")
                m = Message(text, c)    # save Contact object
                self.messages.append(m)
                print("SMS yuborildi!\n")
                return

        print("Bu ismli contact topilmadi!\n")

    def view_messages(self):
        print("\n--- MESSAGES ---")
        for m in self.messages:
            print(f'To: {m.receiver.name} | Text: {m.text}')
        print()

    def edit_contact(self):
        contact_name = input("Qaysi kontakt ozgartirilsin?: ")

        for c in self.contacts:
            if contact_name == c.name:
                print('Topildi!')

                new_name = input('New contact name: ')
                if new_name != "":
                    c.name = new_name

                new_phone = input('New contact phone: ')
                if new_phone != "":
                    c.phone = new_phone

                new_age = input('New contact age: ')
                if new_age != "":
                    c.age = int(new_age)

                new_email = input('New contact email: ')
                if new_email != "":
                    c.email = new_email

                print('Contact ozgartirildi!\n')
                return

        print("Contact topilmadi!\n")

    def delete_contact(self):
        name = input("Qaysi contactni ochirishni xohlaysiz?: ")

        for c in self.contacts:
            if name == c.name:
                self.contacts.remove(c)
                print('Contact o\'chirildi!\n')
                return

        print("Contact topilmadi!\n")


def menu():
    sms = SmsManager()

    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Send SMS")
        print("6. View Messages")
        print("7. Exit")

        kod = input("Tanlang: ")

        if kod == "1":
            sms.add_contact()
        elif kod == "2":
            sms.view_contact()
        elif kod== "3":
            sms.edit_contact()
        elif kod == "4":
            sms.delete_contact()
        elif kod == "5":
            sms.add_message()
        elif kod == "6":
            sms.view_messages()
        elif kod == "7":
            break

menu()



























