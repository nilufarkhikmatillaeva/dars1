


# contacts={
#     997856363:{
#         "name":"Ziyoda",
#         "phone": "+998997856363",
#         "email":"xamidullaeva@gmail.com"
#     },
#     908684868:{
#         "name":"Amina",
#         "phone":"+998908684868",
#         "email":"xamidova@gmail.com"
#     },
#     972342323:{
#         "name":"Aziza",
#         "phone": "+998972342323",
#         "email":"xakimova@gmail.com"
#     }
# }
import csv

def add_contact():
    name=input("name=")
    phone=input("phone=")
    email=input("email=")
    columns=['name', 'phone','email']
    with open('contacts.csv','a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # writer.writerow(columns)
        writer.writerows([[name,phone,email]])
# add_contact()




def read_contact():
    with open('contacts.csv','r') as f:
        reader = csv.reader(f)
        count=0
        for i in reader:
            if count != 0:
                print(f'{count}. {i[0]} {i[1]} {i[2]}')
            else:
                print(f'   {i[0]} {i[1]} {i[2]}')
                count+=1
# read_contact()

def update_contact():
    with open('contacts.csv','r') as f:
        reader = csv.reader(f)
        s=list(reader)


        contact_id= int(input("id="))
        contact_f=int(input("tanlang: "))
        new_f=input("new_f:")
        s[contact_id][contact_f]=new_f
        with open('contacts.csv','w', newline='', encoding='utf-8') as f:
            w=csv.writer(f)
            w.writerows(s)
        print("ozgardi")
# update_contact()


def contact_manager():
    while True:
        kod = input(" 1. view contact \n 2. add contact \n 3.remove contact \n 4. update contact \n 5. exit() ")
        if kod == '1':
            print("===============VIEW CONTACTS================")
            read_contact()
            print("===============END VIEW===================")
        elif kod == '2':
            add_contact()
        elif kod == '3':
            pass
        elif kod == '4':
            update_contact()
        else:
            print("jarayon tugadi")
            break
contact_manager()


