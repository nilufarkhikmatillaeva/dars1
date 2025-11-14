# working with json data in python
# try except
# exam: bank card - series - password - if wrong=block if yes=services
# add new characteristics for each electronic

# electronics={
#     "PC3242":{
#         "title":"Lenovo",
#         "price":"650$",
#         "year":2011,
#         "type":"Computer",
#         "id":"PC3242",
#         "cpu": "Intel i7",
#         "storage": "512GB SSD"
#     },
#     "Ph3443":{
#         "title":"s 24",
#         "price":"1000$",
#         "year":2022,
#         "type":"Phone",
#         "id":"Ph3443",
#         "camera": "108MP",
#         "memory": "256GB"
#     },
#     "TV1212":{
#         "title":"LG",
#         "price":"450$",
#         "year":2010,
#         "type":"TV",
#         "id":"TV1212",
#         "screen_size": "55 inches",
#         "resolution": "4K"
#     }}
# def add_tv(d:dict):
#     title=input("title:")
#     price=input("price:")
#     year=input("year:")
#     type=input("type:")
#     id=input("id:")
#     screen_size = input("screen size: ")
#     resolution = input("resolution: ")
#     s={id:{
#         "title":title,
#         "price":price,
#         "year":year,
#         "type":type,
#         "id":id,
#         "screen_size":screen_size,
#         "resolution":resolution,
#     }}
#     d.update(s)
# def add_phone(d:dict):
#     title=input("title:")
#     price=input("price:")
#     year=input("year:")
#     type=input("type:")
#     id=input("id:")
#     camera=input("camera:")
#     memory=input("memory:")
#     s={id:{
#         "title":title,
#         "price":price,
#         "year":year,
#         "type":type,
#         "id":id,
#         "camera":camera,
#         "memory":memory
#     }}
#     d.update(s)
# def add_comp(d:dict):
#     title=input("title:")
#     price=input("price:")
#     year=input("year:")
#     type=input("type:")
#     id=input("id:")
#     cpu=input("cpu:")
#     storage=input("storage:")
#     s={id:{
#         "title":title,
#         "price":price,
#         "year":year,
#         "type":type,
#         "id":id,
#         "cpu":cpu,
#         "storage":storage,
#     }}
#     d.update(s)
#
#
# def view_tv(d:dict):
#     for k,v in d.items():
#         if v.get("type","").lower()=="tv":
#             print(f"id.{k}. title:{v['title']} price:{v['price']}")
# def view_phone(d:dict):
#     for k,v in d.items():
#         if v.get("type","").lower()=="phone":
#             print(f"id.{k}. type:Phone  title:{v['title']}")
# def view_comp(d:dict):
#     for k,v in d.items():
#         if v.get("type","").lower()=="computer":
#             print(f"id.{k}. type:Computer  title:{v['title']}")
#
# def electronic_manager(d:dict):
#     while True:
#         kod=input(" 1. view TV \n 2. add TV \n 3. view Phone \n 4. add Phone \n 5. view computer \n 6. add computer \n 7. break")
#         if kod=="1":
#             view_tv(d)
#         elif kod=="2":
#             add_tv(d)
#         elif kod=="3":
#             view_phone(d)
#         elif kod=="4":
#             add_phone(d)
#         elif kod=="5":
#             view_comp(d)
#         elif kod=="6":
#             add_comp(d)
#         elif kod=="7":
#             break
# electronic_manager(electronics)



import json


electronics={
    "PC3242":{
        "title":"Lenovo",
        "price":"650$",
        "year":2011,
        "type":"Computer",
        "id":"PC3242",
        "cpu": "Intel i7",
        "storage": "512GB SSD"
    },
    "Ph3443":{
        "title":"s 24",
        "price":"1000$",
        "year":2022,
        "type":"Phone",
        "id":"Ph3443",
        "camera": "108MP",
        "memory": "256GB"
    },
    "TV1212":{
        "title":"LG",
        "price":"450$",
        "year":2010,
        "type":"TV",
        "id":"TV1212",
        "screen_size": "55 inches",
        "resolution": "4K"
    }}

# with open('n73.json','w') as f:
#         data = json.dump(electronics, f,indent=4)


# def add_n73(d:dict):
#     with open('n73.json','w') as f:
#         data = json.dump(electronics, f,indent=4)
# add_n73(electronics)

new_e={
    "TV1214":{
    "title": "Samsung",
    "price": "500$",
    "year": 2010,
    "type": "TV",
    "id": "TV1214",
    "screen_size": "50 inches",
    "resolution": "HD"}}


def wr_n73(d:dict):
    with open('n73.json','w') as f:
        data = json.dump(d, f, indent=4)

def read_n73():
    s=0
    with open('n73.json','r') as f:
        try:
            s=json.load(f)
            return s
        except:
            return "n_73 file doesn't exist"
read_n73()

def add_n73():
    data=read_n73()
    title = input("title:")
    price=input("price:")
    year=input("year:")
    type=input("type:")
    id=input("id:")
    s={id:{
        "title":title,
        "price":price,
        "year":year,
        "type":type,
        "id":id
    }}
    if data:
        data=dict(data)
        data.update(s)
        wr_n73(data)
    else:
        wr_n73(s)
add_n73()


