# class Product:
#     def __init__(self,title,price,production_year,expiration_year,country,type):
#         self.title = title
#         self.price = price
#         self.production_year = production_year
#         self.expiration_year = expiration_year
#         self.country = country
#         self.type = type
#
# product1 = Product('Lays',10000,2024,2025,'Uzbekistan','chips')
# product2 = Product('AlpenGold',15000,2023,2024,'Switzerland','chocolate')
# baza = [product1,product2]
#
#
# def view_product(s:list):
#     count = 0
#     for item in s:
#         count += 1
#         print(f'{count}. title:{item.title} price:{item.price}')
# # view_product(baza)
#
# def add_product(s:list):
#     title = input('title=')
#     price = input('price=')
#     production_year = input('production year=')
#     expiration_year = input('expiration year=')
#     country = input('country=')
#     type = input('type=')
#
#     a=Product(title,price,production_year,expiration_year,country,type)
#     s.append(a)
# # add_product(baza)
# # view_product(baza)
#
# def product_manager(s:list):
#     while True:
#         kod = input(' 1. view product\n 2. add product\n 3. break\n tanlang:')
#         if kod == '1':
#             view_product(s)
#         elif kod == '2':
#             add_product(s)
#         else:
#             break
#
# product_manager(baza)

class Contacts:
    def  __init__(self,name,phone,email,age):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age

contact1 = Contacts("Ziyoda",'+998981748639','ziyoda@gmail.com',15)
contact2 = Contacts('Maftuna','+998996473737',"maftuna@gmail.com",18)
contact3 = Contacts("Akmal",'+998983786344','akmal@gmail.com',15)

baza = [contact1,contact2,contact3]

def view_contact(s:list):
    count = 0
    for item in s:
        count += 1
        print(f"{count}. name:{item.name} phone:{item.phone}")
# view_contact(baza)

import re

def check_phone(s:list):
    for item in s:
        if re.match(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$',item.phone):
            print(f"{item.phone} is valid")
        else:
            print(f"{item.phone} is not valid")
# check_phone(baza)


def check_email(s:list):
    for item in s:
        if re.match(r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+',item.email):
            print(f"{item.email} is valid")
        else:
            print(f"{item.email} is not valid")

# check_email(baza)

def add_contact(s:list):
    name = input('name:')
    phone = input('phone:')
    email = input('email:')
    age = input('age:')

    n = Contacts(name,phone,email,age)
    s.append(n)

# add_contact(baza)
# view_contact(baza)

def contact_manager(s:list):
    while True:
        kod = input(f' 1. view contacts \n 2. add contact \n 3. check phone number \n 4. check email \n 5.exit \n tanlang:')
        if kod == "1":
            view_contact(s)
        elif kod == "2":
            add_contact(s)
        elif kod == "3":
            check_phone(s)
        elif kod == "4":
            check_email(s)
        else:
            break
contact_manager(baza)

