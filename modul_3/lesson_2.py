# import bcrypt
# import psycopg2
#
# from typing import Optional
#
# from psycopg2.extras import DictCursor
#
# con = psycopg2.connect(
#     dbname='shopdb',
#     user='abc',
#     password='1',
#     host='localhost',
#     cursor_factory=DictCursor
# )
#
# cur = con.cursor()

# #
# # # query = '''create table users(
# # #     id serial primary key,
# # #     name varchar(255) not null,
# # #     username varchar(255) not null unique ,
# # #     password varchar(255) not null,
# # #     birth_data integer not null ,
# # #     register_at timestamp default now()
# # # );'''
# #
# # # cur.execute(query)
# # # con.commit()
# #
# # def make_hash(password: str) -> str:
# #     password = password.encode('utf-8')
# #     salt = bcrypt.gensalt()
# #     hashed = bcrypt.hashpw(password, salt)
# #     hashed = hashed.decode('utf-8')
# #     return hashed
# #
# #
# # def check_hash(password: str, db_password: str) -> bool:
# #     db_password = db_password.encode('utf-8')
# #     password = password.encode('utf-8')
# #     return bcrypt.checkpw(password, db_password)
# #
# #
# # def get_user(username: str) -> Optional[tuple]:
# #     query = 'select * from users where username = %s;'
# #     cur.execute(query, (username,))
# #     return cur.fetchone()
# #
# #
# # def add_user(name: str, username: str, password: str, year: int) -> tuple[bool, str]:
# #     password = make_hash(password)
# #     if get_user(username):
# #         return False, 'Bu username bor'
# #     else:
# #         query = 'insert into users(name, username, password, year) values(%s, %s, %s,%s)'
# #         data = (name, username, password, year)
# #         cur.execute(query, data)
# #         con.commit()
# #         return True, 'Qoshildi'
# #
# #
# # def register(name: str, username: str, password: str, year: int) -> None:
# #     is_add, msg = add_user(name, username, password, year)
# #     print(msg)
# #
# #
# # def check_login(username: str, password: str) -> bool:
# #     password = make_hash(password)
# #     query = 'select * from users where username = %s;'
# #     cur.execute(query, (username,))
# #     user = cur.fetchone()
# #     return user and check_hash(user['password'], password)
# #
# #
# # def add_product(name: str, price: int, amount: int) -> None:
# #     query = 'insert into product(name, price, amount) values(%s, %s, %s)'
# #     cur.execute(query, (name, price, amount))
# #     con.commit()
# #
# #
# # def add_products(name, price, amount):
# #     query = 'insert into product(name, price, amount) values(%s, %s, %s)'
# #     data = (name, price, amount)
# #     cur.execute(query, data)
# #     con.commit()
# #
# #
# # def get_products(id):
# #     query = 'select * from product where id = %s'
# #     cur.execute(query, (id,))
# #     for i in cur.fetchall():
# #         print(*i)
# #
# #
# # # add_products(input('Name: '), int(input('Price: ')), int(input('Amount: ')))
# # # get_products()
# #
# # def show_products():
# #     query = 'select id, name, price from product'
# #     cur.execute(query)
# #     for i in cur.fetchall():
# #         print(*i)
# #
# #
# # def delate_product(id):
# #     query = 'delete from product where id = %s'
# #     cur.execute(query, (id,))
# #     con.commit()
# #     show_products()
# #
# #
# # def change_product(id, name, price, amount):
# #     query = 'update product set name = %s, price = %s, amount = %s where id = %s'
# #     data = (name, price, amount, id)
# #     cur.execute(query, data)
# #     con.commit()
# #     get_products(id)
# #
# #
# # def mart():
# #     while True:
# #         m = '''
# #         1) mahsulotlar
# #         2) mahsulot qoshish
# #         3) mahsulot ochirish
# #         4) mahsulotni ozgartirish
# #         5 chiqish
# #         '''
# #         print(m)
# #         n = int(input('>>>  : '))
# #         match n:
# #             case 1:
# #                 print('barcha mahsulotlar ! : ')
# #                 show_products()
# #             case 2:
# #                 add_product(input('Name: '), int(input('Price: ')), int(input('Amount: ')))
# #                 show_products()
# #             case 3:
# #                 delate_product(input('Id = '))
# #                 print("Ochrildi ! ")
# #             case 4:
# #                 show_products()
# #                 change_product(input("id = "), input("name = "), input("price = "), input("amount"))
# #                 print("Ozgartirildi !")
# #             case 5:
# #                 break
# #
# #
# # t = '''
# # 1) login
# # 2) register
# # '''
# # while True:
# #     b = input(f'{t}\n>>>: ')
# #     match b:
# #         case '1':
# #             _username = input('username: ')
# #             _password = input('password: ')
# #             user =  check_login(_username, _password)
# #             if user:
# #                 mart()
# #             else:
# #                 print('xato')
# #         case '2':
# #             register(input("name "), input('username '), make_hash(input('password ')), int(input('year ')))
#
# import bcrypt
# import psycopg2
#
# from typing import Optional
#
# from psycopg2.extras import DictCursor
#
# con = psycopg2.connect(
#     dbname='shopdb',
#     user='abc',
#     password='1',
#     host='localhost',
#     cursor_factory=DictCursor
# )
#
# cur = con.cursor()
#
#
# # query = '''create table users(
# #     id serial primary key,
# #     name varchar(255) not null,
# #     username varchar(255) not null unique ,
# #     password varchar(255) not null,
# #     birth_data integer not null ,
# #     register_at timestamp default now()
# # );'''
#
# # cur.execute(query)
# # con.commit()
#
# def make_hash(password: str) -> str:
#     password = password.encode('utf-8')
#     salt = bcrypt.gensalt()
#     hashed = bcrypt.hashpw(password, salt)
#     hashed = hashed.decode('utf-8')
#     return hashed
#
#
# def check_hash(password: str, db_password: str) -> bool:
#     db_password = db_password.encode('utf-8')
#     password = password.encode('utf-8')
#     return bcrypt.checkpw(password, db_password)
#
# #
# # db_p = '$2b$12$tbeZcV9dxALHfonMqIUSlu7imY16S2fX/Bg7/3b0fqrW5BVvcptLG'
# # p = '1234578'
# # print(check_hash(p, db_p))
# # h = '1енг234578'
# # # raw string
# # print(type(h), h)
# # h = h.encode('utf-8')
# # print(bytes('helloнг2', encoding='utf-8'))
# # print(type(h), h)
# # h = h.decode()
# #
# # print(type(h), h)
#
#
# def get_user(username: str) -> Optional[tuple]:
#     query = 'select * from users where username = %s;'
#     cur.execute(query, (username,))
#     return cur.fetchone()
#
#
# def add_user(name: str, username: str, password: str, year: int) -> tuple[bool, str]:
#     password = make_hash(password)
#     if get_user(username):
#         return False, 'Bu username bor'
#     else:
#         query = 'insert into users(name, username, password, year) values(%s, %s, %s,%s)'
#         data = (name, username, password, year)
#         cur.execute(query, data)
#         con.commit()
#         return True, 'Qoshildi'
#
#
# def register(name: str, username: str, password: str, year: int) -> None:
#     is_add, msg = add_user(name, username, password, year)
#     print(msg)
#
#
# def check_login(username: str, password: str) -> bool:
#     password = make_hash(password)
#     query = 'select * from users where username = %s;'
#     cur.execute(query, (username,))
#     user = cur.fetchone()
#     return user and check_hash(user['password'], password)
#
#
# def add_product(name: str, price: int, amount: int) -> None:
#     query = 'insert into product(name, price, amount) values(%s, %s, %s)'
#     cur.execute(query, (name, price, amount))
#     con.commit()
#
#
# def get_product(pk: int) -> Optional[tuple]:
#     query = 'select * from product where id = %s'
#     cur.execute(query, (pk, ))
#     product = cur.fetchone()
#     print(product)
#     return product
#
#
# def get_all_products() -> list[Optional[tuple]]:
#     query = 'select id, name, price from product'
#     cur.execute(query)
#     return [product for product in cur.fetchall()]
#
#
# def delete_product(id):
#     query = 'delete from product where id = %s'
#     cur.execute(query, (id, ))
#     con.commit()
#
#
# def change_product(id, name, price, amount):
#     query = 'update product set name = %s, price = %s, amount = %s where id = %s'
#     cur.execute(query, (name, price, amount, id))
#     con.commit()
#
#
# #
# #
# def menu():
#     while True:
#         m = '''
#         1) mahsulotlar
#         2) mahsulot qoshish
#         3) mahsulot ochirish
#         4) mahsulotni ozgartirish
#         5 chiqish
#         '''
#
#         while True:
#             print(m)
#             n = int(input('>>>  : '))
#             match n:
#                 case 1:
#                     print('barcha mahsulotlar ! : ')
#                     get_all_products()
#                 case 2:
#                     add_product(input('Name: '), int(input('Price: ')), int(input('Amount: ')))
#                     get_all_products()
#                 case 3:
#                     delete_product(input('Id = '))
#                     print("Ochrildi ! ")
#                 case 4:
#                     get_all_products()
#                     change_product(input("id = "), input("name = "), input("price = "), input("amount"))
#                     print("Ozgartirildi !")
#                 case _:
#                     break
#
# t = '''
# 1) login
# 2) register
# '''
# while True:
#     b = input(f'{t}\n>>>: ')
#     match b:
#         case '1':
#             _username = input('username: ')
#             _password = input('password: ')
#             user = check_login(_username, _password)
#             if user:
#                 menu()
#             else:
#                 print('xato')
#
#         case '2':
#             register(input("name "), input('username '), make_hash(input('password ')), input('year '))
#
#
#
#

import bcrypt
import psycopg2

from typing import Optional

from psycopg2.extras import DictCursor

con = psycopg2.connect(
    dbname='shopdb',
    user='abc',
    password='1',
    host='localhost',
    cursor_factory=DictCursor
)

cur = con.cursor()


# query = '''create table users(
#     id serial primary key,
#     name varchar(255) not null,
#     username varchar(255) not null unique ,
#     password varchar(255) not null,
#     balance integer not null ,
#     year integer not null ,
#     is_admin int ,
#     register_at timestamp default now()
#
# );'''
#
# cur.execute(query)
# con.commit()


# query = '''create table products(
#     id serial primary key,
#     name varchar(255) not null,
#     amount varchar(255) not null,
#     price varchar not null ,
#     register_at timestamp default now()
# );'''
#
# cur.execute(query)
# con.commit()
#
# query = '''create table order_(
#     id serial primary key,
#     user_name varchar(255) not null,
#     product_name varchar(255) not null,
#     amount varchar(255) not null,
#     price varchar not null ,
#     shop_at timestamp default now()
# );'''
#
# cur.execute(query)
# con.commit()

def add_product(name: str, price: int, amount: int) -> None:
    query = 'insert into products(name,price,amount)values (%s,%s,%s)'
    data = (name, price, amount)
    cur.execute(query, data)
    con.commit()


def get_product(pk: int) -> Optional[tuple]:
    query = 'select * from products where id = %s'
    cur.execute(query, (pk,))
    for i in cur.fetchall():
        print(*i)


def get_all_products() -> list[Optional[tuple]]:
    query = 'select * from products'
    cur.execute(query)
    for i in cur.fetchall():
        print(*i)


def delete_product(pk: int):
    query = 'delete from products where id =%s'
    cur.execute(query, (pk,))
    con.commit()
    get_all_products()


def change_product(pk, name, price, amount):
    query = 'update products set name = %s, price = %s, amount = %s where id = %s'
    cur.execute(query, (name, price, amount, pk))
    con.commit()


def get_user(username):
    query = 'select * from users where username = %s;'
    cur.execute(query, (username,))
    return cur.fetchone()


def add_user(name: str, username: str, password: str, year: int, balance: int, is_admin: bool) -> tuple[
    bool, str, int]:
    password = hashing(password)
    if not get_user(username):
        query = 'insert into users(name,username,password,balance,year,is_admin) values (%s,%s,%s,%s,%s,%s)'
        cur.execute(query, (name, username, password, balance, year, is_admin))
        con.commit()
        print('User saved')
    else:
        print('this username already used')


def hashing(data):
    data = data.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(data, salt)
    hashed = hashed.decode('utf-8')
    return hashed


def hashing_read(password: str, db_data: str) -> bool:
    db_data = db_data.encode('utf-8')
    password = password.encode('utf-8')
    return bcrypt.checkpw(password, db_data)


def login_user(username: str, password: str) -> bool:
    qu = 'select * from users where username = %s '
    cur.execute(qu, (username,))
    user = cur.fetchone()
    return user and hashing_read(password, user[3])


def login():
    qu  = 'sel'
def buy_prod(id, count, username):
    qu = 'select * from products where id = %s'
    cur.execute(qu, (id,))
    prod = cur.fetchone()
    con.commit()
    qur = 'insert into order_(user_name,product_name,amount,price) values (%s,%s,%s,%s)'
    cur.execute(qur, (username, prod[1], prod[2], count))
    con.commit()
    qury = 'select * from users where username = %s'
    cur.execute(qury, (username,))
    data = cur.fetchone()
    if data[3] >= (prod[2] * count):
        a = data[3] - (prod[2] * count)
        query = 'update users set balance = %s where user_name = %s'
        cur.execute(query, (a, username))
        con.commit()
    else:
        print('not enought money')

    if prod[3] >= count:
        res = prod[3] - count
        quryy = 'update products set amount = %s where id = %s'
        cur.execute(quryy, (res, id))
        con.commit()
    else:
        print('not have enought products')


def is_admin(username: str) -> bool:
    qury = 'select * from users where username = %s'
    cur.execute(qury, (username,))
    user = cur.fetchone()
    return user and user[6] == True


def check_balace(username: str) -> None:
    query = 'select balance from users where username = %s'
    cur.execute(query, (username,))
    for i in cur.fetchall():
        print('your balance:', *i)


def get_history(username: str) -> None:
    qur = 'select * from order_ where username = %s'
    cur.execute(qur, (username,))
    for i in cur.fetchall():
        print(f'name: {i[1]} -> price: {i[2]} -> amount: {i[-2]}')


def get_daily_report():
    qr = "select * from order_ where shop_at <= now() - interval '0 day' and shop_at <= now()"
    cur.execute(qr)
    for i in cur.fetchall():
        print(f" {i[1]} -> {i[2]} -> {i[3]} -> {i[4]}")


def get_weekly_report():
    qr = "select * from order_ where shop_at <= now() - interval '7 day' and shop_at <= now()"
    cur.execute(qr)
    for i in cur.fetchall():
        print(f" {i[1]} -> {i[2]} -> {i[3]} -> {i[4]}")


def get_monthly_report():
    qr = "select * from order_ where shop_at <= now() - interval '1 month' and shop_at <= now()"
    cur.execute(qr)
    for i in cur.fetchall():
        print(f" {i[1]} -> {i[2]} -> {i[3]} -> {i[4]}")


while True:
    text = '''
    1) Log in
    2) Register
    0) Exit
    '''
    choise1 = input(text + '>>>>')
    match choise1:
        case '1':
            username = input('enter username:')
            password = input('enter password:')
            sd = username
            zx = login_user(username, password)
            sad = is_admin(username)
            if zx:
                if not sad:
                    while True:
                        text3 = '''
                           1) Buy product
                           2) Check balance
                           3) History
                           0) Exit
                           '''
                        choise3 = input(text3 + '>>>')

                        match choise3:
                            case '1':
                                get_all_products()
                                pk = int(input('Id kiriting: '))
                                count = int(input('Qancha kerak :'))
                                buy_prod(pk, count, sd)
                            case '2':
                                check_balace(username)
                            case '3':
                                get_history(username)
                            case '0':
                                break


                else:
                    menu = '''
                         1) all products
                         2) view one product
                         3) add product
                         4) delete product
                         5) change product
                         6) reports
                         0) Exit
                         '''
                    while True:
                        choise = input(menu + '>>>')
                        match choise:
                            case '1':
                                print('N: id  name  price  amount')
                                get_all_products()
                                continue
                            case '2':
                                pk = int(input('enter product id :'))
                                get_product(pk)

                            case '3':
                                add_product(input("name: "), int(input("price: ")), int(input("amount: ")))
                                print('product added')

                            case '4':
                                delete_product(input('enter id: '))
                                print('product is deleted')
                            case '5':
                                get_all_products()
                                pkk = input('enter id: ')
                                name = input('enter the name: ')
                                price = int(input('price: '))
                                amount = int(input('amount: '))
                                change_product(pkk,name,price,amount)
                                print('product is changed')

                            case '6':
                                while True:
                                    mirror = '''
                                    1) daily report
                                    2) weekly report
                                    3)monthly report
                                    4) exit
                                    '''
                                    choise4 = input(mirror + '>>>>')
                                    match choise4:
                                        case '1':
                                            print('1 day report')
                                            get_daily_report()
                                        case '2':
                                            print('weeekly report')
                                            get_weekly_report()
                                        case '3':
                                            print('monthly report')
                                            get_monthly_report()
                                        case '4':
                                            break
                            case '0':
                                break

        case '2':
            ism = input('enter the name: ')
            username = input('enter the username: ')
            password = input('enter your password: ')
            year = int(input('enter your birthdate:'))
            balance = int(input('Balance: '))
            is_admin = int(input('Admin 1  ||  user 0 :'))
            if is_admin:
                balance = 0
                add_user(ism, username, password, year, balance, is_admin)

            if not is_admin:
                add_user(ism, username, password, year, balance, is_admin)


