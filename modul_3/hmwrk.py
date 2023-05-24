import psycopg2
import bcrypt

con = psycopg2.connect(
    dbname='project_db',
    user='abc',
    password='1',
    host='localhost',
)

cur = con.cursor()


#
# quary = """create table product(
#     id serial primary key,
#     name varchar(50),
#     price integer not null ,
#     amount integer not null
# );"""
#
# cur.execute(quary)
# con.commit()

def add_prod(name, price, amount):
    quary = 'insert into product(name,price,amount) values (%s,%s,%s)'
    data = (name, price, amount)
    cur.execute(quary, data)
    con.commit()


def get_prod(id):
    query = 'select * from product where id = %s'
    cur.execute(query, (id,))
    for i in cur.fetchall():
        print(*i)


def show_prod():
    qu = 'select * from product'
    cur.execute(qu)
    for i in cur.fetchall():
        print(*i)


def remave_prod(id):
    qur = 'delete from product where id = %s'
    cur.execute(qur, id)
    con.commit()
    show_prod()


def change_prod(id, name, price, amount):
    qury = 'update product set name = %s,price = %s,amount = %s where id =%s'
    data = (name, price, amount, id)
    cur.execute(qury, data)
    con.commit()


def get_user(username):
    query = 'select * from users where username = %s;'
    cur.execute(query, (username,))
    return cur.fetchone()


def add_user(first_name: str, username: str, password: str, year: int, balance: int, is_admin: bool) -> tuple[
    bool, str, int]:
    password = hashing(password)
    if not get_user(username):
        query = ('insert into users(first_name,username,password,year,balance,is_admin) values (%s,%s,%s,%s,%s,%s)')
        cur.execute(query, (first_name, username, password, year, balance, is_admin))
        con.commit()
        print('User saqlandi!!!!')
    else:
        print('Bunday username mavjud!!!')


def hashing(data):  # noqa
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


def buy_prod(id: int, count: int, username):
    qu = 'select * from product where id = %s'
    cur.execute(qu, (id,))
    prod = cur.fetchone()
    con.commit()
    qur = 'insert into orders(username,prod_name,price,amount) values (%s,%s,%s,%s)'
    cur.execute(qur, (username, prod[1], prod[2], count))
    con.commit()
    qury = 'select * from users where username = %s'
    cur.execute(qury, (username,))
    data = cur.fetchone()

    if data[5] >= (prod[2] * count):
        ayr = data[5] - (prod[2] * count)
        qury = 'update users set balance = %s where username = %s'
        cur.execute(qury, (ayr, username))
        con.commit()
    else:
        print('Sizda mablaq` yetarli emas!!!!')

    if prod[3] >= count:
        res = prod[3] - count
        quryy = 'update product set amount = %s where id = %s'
        cur.execute(quryy, (res, id))
        con.commit()
    else:
        print('Maxsulot yetarli emas!!!!')


def is_admin(username: str) -> bool:
    qury = 'select * from users where username = %s'
    cur.execute(qury, (username,))
    user = cur.fetchone()
    return user and user[6] == True


def check_balace(username: str) -> None:
    query = 'select balance from users where username = %s'
    cur.execute(query, (username,))
    for i in cur.fetchall():
        print('Sizning balansingiz:', *i)


def get_history(username: str) -> None:
    qur = 'select * from orders where username = %s'
    cur.execute(qur, (username,))
    for i in cur.fetchall():
        print(f'Nomi: {i[1]} -> Narxi: {i[2]} -> Soni: {i[-2]}')

def get_daily_report():
    qr = "select * from orders where register_date <= now() - interval '1 day' and register_date <= now()"
    cur.execute(qr)
    for i in cur.fetchall():
        print(f" {i[1]} -> {i[2]} -> {i[3]} -> {i[4]}")

def get_weekly_report():
    qr = "select * from orders where register_date <= now() - interval '7 day' and register_date <= now()"
    cur.execute(qr)
    for i in cur.fetchall():
        print(f" {i[1]} -> {i[2]} -> {i[3]} -> {i[4]}")

def get_monthly_report():
    qr = "select * from orders where register_date <= now() - interval '1 month' and register_date <= now()"
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
            username = input('Username kiriting:')
            password = input('Password kiriting:')
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
                                show_prod()
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
                         1) Hamma maxsulotlarni ko`rish
                         2) Bitta maxsulotni ko`rish
                         3) Maxsulot qo`shish
                         4) Maxsulot ayrish
                         5) Maxsulotni o`zgartirish
                         6) Xisobotlar
                         0) Exit
                         '''
                    while True:
                        choise = input(menu + '>>>')
                        match choise:
                            case '1':
                                print('N: id  name  price  amount')
                                show_prod()
                                continue
                            case '2':
                                pk = int(input('Maxsulot ID sini kiriting :'))
                                get_prod(pk)

                            case '3':
                                add_prod(input("name: "), int(input("price: ")), int(input("amount: ")))
                                print('Maxsulot qo`shildi!!!')

                            case '4':
                                remave_prod(input('ID kiriting: '))
                                print('Mxasulot o`chirildi$$$')
                            case '5':
                                show_prod()
                                change_prod(input('ID kiriting:'), input('name kiriting: '), input('price: '),
                                            input('amount: '))
                                print('Maxsulot o`zgardi!!!')

                            case '6':
                                while True:
                                    mirror = '''
                                    1) Kunlik xisobot
                                    2) Xaftalik xisobot
                                    3) Oylik xisobot
                                    '''
                                    choise4 = input(mirror + '>>>>')
                                    match choise4:
                                        case '1':
                                            print('Bugungi xisob!!!')
                                            get_daily_report()
                                        case '2':
                                            print('Xaftalik xisobot!!!')
                                            get_weekly_report()
                                        case '3':
                                            print('Oylik xisobot!!!')
                                            get_monthly_report()
                            case '0':
                                break

        case '2':
            ism = input('Ismingizni kiriting: ')
            username = input('Username kiriting: ')
            password = input('Passwordingizni kiriting: ')
            year = int(input('Tug`ilgan yilingiz:'))
            balance = int(input('Balance: '))
            is_admin = int(input('Admin 1  ||  user 0 :'))

            if is_admin:
                balance = 0
                add_user(ism, username, password, year, balance, is_admin)

            if not is_admin:
                add_user(ism, username, password, year, balance, is_admin)