import smtplib
import ssl
from email.message import EmailMessage

import bcrypt
import psycopg2

mail_content = 'hello'  # noqa
con = psycopg2.connect(
    dbname='exam',  # noqa
    user='ali',
    password='1',
    host='localhost'
)
cur = con.cursor()


def register(name: str, username: str, password: str, year: str, email: str, balance: int,  # noqa
             is_admin: bool) -> bool:  # noqa
    password = hashing(password)  # noqa
    if not get_user(username):
        query = 'insert into users(name, username, password, year, email, balance, is_admin) values (%s,%s,%s,%s,%s,%s,%s)'  # noqa
        cur.execute(query, (name, username, password, year, email, balance, is_admin))
        con.commit()
        print('User Saqlandi')
    else:
        print('BU username oldin  ishlatilgan')


def hashing(data: str) -> str:  # noqa
    data = data.encode('utf-8')
    hash = bcrypt.gensalt()  # noqa
    hashed = bcrypt.hashpw(data, hash)
    hashed = hashed.decode('utf-8')
    return hashed


def get_user(username: str) -> bool:  # noqa
    query = 'select username from users where username = %s'  # noqa
    cur.execute(query, (username,))
    return cur.fetchone()


def hash_read(password: str, db_data: str) -> bool:  # noqa
    db_data = db_data.encode('utf-8')
    password = password.encode('utf-8')  # noqa
    return bcrypt.checkpw(password, db_data)


def check_login(username: str, password: str) -> bool:  # noqa
    query = 'select * from users where username = %s'  # noqa
    cur.execute(query, (username,))
    user = cur.fetchone()
    return user and hash_read(password, user[4])


def _is_admin(username: str) -> bool:  # noqa
    query = 'select * from users where username = %s'  # noqa
    cur.execute(query, (username,))
    admin = cur.fetchone()
    return admin and admin[7] == bool(True)


def show_all_product() -> None:  # noqa
    query = 'select * from product'  # noqa
    cur.execute(query)
    for i in cur.fetchall():  # noqa
        print(f" ID: {i[0]} -> Nomi: {i[2]} -> Narxi: {i[3]} -> Miqdori: {i[4]}")


def show_one_product(id: int) -> None:  # noqa
    query = 'select * from product where id = %s'  # noqa
    cur.execute(query, (id,))
    for i in cur.fetchall():  # noqa
        print(f" ID: {i[0]} -> Nomi: {i[2]} -> Narxi: {i[3]} -> Miqdori: {i[4]}")


def show_my_product(id_create: int) -> None:  # noqa
    query = 'select * from product where admin_id = %s'  # noqa
    cur.execute(query, (id_create,))
    for i in cur.fetchall():  # noqa
        print(f" ID: {i[0]} -> Nomi: {i[2]} -> Narxi: {i[3]} -> Miqdori: {i[4]}")


def add_product(id_create: str, name: str, price: int, amount: int) -> str:  # noqa
    try:
        with con.cursor() as cur:  # noqa
            query = 'SELECT * FROM product WHERE admin_id = %s AND name = %s'  # noqa
            cur.execute(query, (id_create, name))
            result = cur.fetchone()
            if not result:
                query = 'INSERT INTO product (admin_id, name, price, amount) VALUES (%s, %s, %s, %s)'  # noqa
                cur.execute(query, (id_create, name, price, amount))
                con.commit()
                print('Mahsulot qushildi')
            else:
                new_amount = result[4] + amount
                query = 'UPDATE product SET amount = %s, price = %s WHERE admin_id = %s AND name = %s'  # noqa
                cur.execute(query, (new_amount, price, id_create, name))
                con.commit()
                return 'Siz bu mahsulotni ko\'paytirdingiz'
    except Exception as e:
        print(f'Error: {e}')


def check_product_id(id: int, id_create: int):  # noqa
    query = 'select * from product where id = %s and admin_id = %s'  # noqa
    cur.execute(query, (id, id_create))
    return cur.fetchone()


def remove_product(id: int, id_create: int) -> None:  # noqa
    if check_product_id(id, id_create):
        query = 'DELETE FROM product WHERE id = %s AND admin_id = %s'  # noqa
        with con.cursor() as cur:  # noqa
            cur.execute(query, (id, id_create))
            con.commit()
        print('Mahsulot uchirildi')
    else:
        print('Bunday id mavjud emas')


def change_product(id: int, id_create: int, name: str, price: int, amount: int) -> None:  # noqa
    if check_product_id(id, id_create):
        query = 'update product set name = %s, price = %s, amount =%s where id = %s and admin_id = %s'  # noqa
        cur.execute(query, (name, price, amount, id, id_create))
        con.commit()
        print('Mahsulot uzgartirildi')
    else:
        print('Bunday id mavjud emas')


def daily_date() -> None:
    query = "SELECT * FROM order_ WHERE register_date BETWEEN NOW() - INTERVAL '1 DAY' AND NOW()"  # noqa
    cur.execute(query)
    for i in cur.fetchall():
        print(f"ID: {i[0]} -> User_id: {i[1]} -> Prod_id: {i[2]} -> Narxi: {i[3]} -> Miqdori: {i[4]}")


def weekly_date() -> None:
    query = "SELECT * FROM order_ WHERE register_date BETWEEN NOW() - INTERVAL '7 DAY' AND NOW()"  # noqa
    cur.execute(query)
    for i in cur.fetchall():
        print(f"ID: {i[0]} -> User_id: {i[1]} -> Prod_id: {i[2]} -> Narxi: {i[3]} -> Miqdori: {i[4]}")


def monthly_date() -> None:
    query = "SELECT * FROM order_ WHERE register_date BETWEEN NOW() - INTERVAL '1 month' AND NOW()"  # noqa
    cur.execute(query)
    for i in cur.fetchall():
        print(f"ID: {i[0]} -> User_id: {i[1]} -> Prod_id: {i[2]} -> Narxi: {i[3]} -> Miqdori: {i[4]}")


def show_product() -> None:  # noqa
    query = 'select * from product'  # noqa
    cur.execute(query)
    for i in cur.fetchall():  # noqa
        print(f"Mahsulot id: {i[0]} -> Mahsulot nomi: {i[2]} -> Mahsulot narxi: {i[3]} ->Mahsulot miqdori: {i[4]}")


def check_id_product(id: int) -> bool:  # noqa
    query = 'select id from product where id =%s'  # noqa
    cur.execute(query, (id,))
    return cur.fetchone()


def buy_product(id: int, count: int, id_create: str, username: str) -> None:  # noqa
    query = 'select p.price, p.amount, u.balance from product p, users u where p.id = %s and u.username = %s'  # noqa
    cur.execute(query, (id, username))
    data = cur.fetchone()

    if data and data[1] >= count and data[2] >= (data[0] * count):
        new_amount = data[1] - count
        new_balance = data[2] - (data[0] * count)

        quert = 'update product set amount = %s where id = %s'  # noqa
        cur.execute(quert, (new_amount, id))

        qure = 'update users set balance = %s where username = %s'  # noqa
        cur.execute(qure, (new_balance, username))

        qur = 'insert into order_(user_id, prod_id, price, amount) values (%s, %s, %s, %s)'  # noqa
        cur.execute(qur, (id_create, id, data[0], count))

        con.commit()
        print('Mahsulot sotib olindi')
    elif not data:
        print('Bunday id mavjud emas')
    elif data[1] < count:
        print('Mahsulot yetarli emas')
    else:
        print('Hisobingiz yetarli emas')


def check_balance(username: str) -> int:  # noqa
    query = 'select balance from users where username = %s'  # noqa
    cur.execute(query, (username,))
    for i in cur.fetchall():  # noqa
        print('Siznig balansingiz', *i)


def check_username(id: int) -> bool:  # noqa
    query = 'select id from order_ where user_id = %s'  # noqa
    cur.execute(query, (id,))
    return cur.fetchone()


def get_history(id: int) -> None:  # noqa
    if check_username(id):
        quer = 'select * from order_ where user_id = %s'  # noqa
        cur.execute(quer, (id,))
        for i in cur.fetchall():  # noqa
            pr = 'select * from product'  # noqa
            cur.execute(pr)
            c = cur.fetchall()
            for j in c:
                if i[2] == j[0]:
                    print(f"Id: {j[0]} -> Nomi: {j[2]} -> Narxi: {i[3]} -> Miqdori: {i[4]}")
    else:
        print("Siz hali mahsulot sotib olmagansiz!")


def send_msg(id_create: int, my_email: str) -> None:  # noqa
    query = 'select u.name, p.name, o.amount, o.price, o.register_date from order_ o join product p on p.id = o.prod_id join users u on u.id = o.user_id where p.admin_id = %s'  # noqa
    cur.execute(query, (id_create,))
    t = ''  # noqa
    for i in cur.fetchall():  # noqa
        t += f"'Xaridor:  {i[0]}  {i[3]} ming sum dan {i[2]} ta {i[1]} xarid qildi  soat {i[4]} da" + '\n'
    email_sender = 'tannagashevalisher07@gmail.com'
    email_password = 'cjnljtiexucjhqpe'  # noqa
    email_receiver = my_email
    subject = 'HISOBOT'  # noqa
    body = f"{t}"
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        print('Send message')


def emails(email):  # noqa
    cur.execute('select * from users where email = %s', (email,))  # noqa
    return cur.fetchone()


while True:  # noqa
    t = """
    1) login
    2) registratsiya
    0) Chiqish
    """
    choice = input(t + '>>>')
    match choice:
        case '1':
            username = input('username: ')
            password = input('password: ')
            query = 'select id from users where username = %s'  # noqa
            cur.execute(query, (username,))
            id_create = cur.fetchone()
            query = 'select email from users where username = %s'  # noqa
            cur.execute(query, (username,))
            my_email = cur.fetchone()
            if check_login(username, password):
                if not _is_admin(username):
                    while True:  # noqa
                        te = """
                        1) Mahsulot sotib olish
                        2) Hisobni tekshirish
                        3) Tarix
                        0) Chiqish
                        """
                        choice1 = input(te + '>>>')  # NOQA
                        match choice1:
                            case '1':
                                show_product()
                                id = int(input('Id kiriting: '))  # noqa
                                count = int(input('Miqdor kiriting: '))
                                buy_product(id, count, id_create, username)
                            case '2':
                                check_balance(username)
                            case '3':
                                query = 'select * from users where username = %s'  # noqa
                                cur.execute(query, (username,))
                                d = cur.fetchone()
                                get_history(d[0])
                            case '0':
                                break
                else:
                    while True:
                        te1 = """
                        1) Barcha mahsulotlarni kurish
                        2) Bitta mahsulot kurish
                        3) Men qushgan mahsulotlarim
                        4) Mahsulot qushish
                        5) Mahsulot uchirish
                        6) Mahsulot uzgartirish
                        7) Hisobot
                        8) Hisobotni email ga yuborish
                        0) Chiqish
                        """
                        choice1 = input(te1 + '>>>')
                        match choice1:
                            case '1':
                                show_all_product()
                            case '2':
                                id = int(input('MAhsulot id : '))  # noqa
                                show_one_product(id)
                            case '3':
                                show_my_product(id_create)
                            case '4':
                                name = input('Nomi: ')
                                price = int(input('Narxi: '))
                                amount = int(input('Miqdori: '))
                                if price > 0 and amount > 0:
                                    add_product(id_create, name, price, amount)
                                else:
                                    print('hato kiritdingiz')
                            case '5':
                                show_my_product(id_create)
                                id = int(input('Mahsulot  id : '))  # noqa
                                remove_product(id, id_create)
                                show_my_product(id_create)
                            case '6':  # noqa
                                show_my_product(id_create)
                                id = int(input('id: '))  # noqa
                                if check_product_id(id, id_create):
                                    name = input('Nomi: ')
                                    price = int(input('Narxi: '))
                                    amount = int(input('Miqdori: '))
                                    change_product(id, id_create, name, price, amount)
                            case '7':
                                while True:
                                    text3 = '''
                                        1) Kunlik hisobot
                                        2) Haftalik hisobot
                                        3) Oylik hisbot
                                        0) Chiqish
                                        '''
                                    choise2 = input(text3 + '>>>>')  # noqa
                                    match choise2:
                                        case '1':
                                            print('Kunlik hisobot')
                                            daily_date()
                                        case '2':
                                            print("Haftalik hisobot")
                                            weekly_date()
                                        case '3':
                                            print('Oylik hisbot')
                                            monthly_date()
                                        case '0':
                                            break
                            case '8':
                                send_msg(id_create, my_email)
                            case '0':
                                break
        case '2':
            name = input('name: ')
            username = input('username: ')
            password = input('password: ')
            year = input('year: ')
            email = input('email: ')
            is_admin = input('Admin Y/n: ')
            if '@gmail.com' in email:
                if not emails(email):
                    if is_admin == 'Y':
                        balance = 0
                        register(name, username, password, year, email, balance, is_admin)  # noqa
                    elif is_admin =='n':
                        balance = input('balance: ')
                        if balance == '':
                            balance = 5000
                            register(name, username, password, year, email, balance, is_admin)  # noqa
                        else:
                            register(name, username, password, year, email, balance, is_admin)  # noqa
                    else:
                        print('hato')
                else:
                    print('bu email oldin oishlatilgan')
            else:
                print('Email xato')
        case '0':
            print('sog bulas')
            break
