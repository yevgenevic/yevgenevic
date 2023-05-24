import psycopg2

con = psycopg2.connect(
    dbname='shopdb',
    user='abc',
    password='1',
    host='localhost',
)
cur = con.cursor()


# query = """create table product(
#     id serial primary key,
#     name varchar(255)not null,
#     price integer not null,
#     amount integer not null
# );"""
# cur.execute(query)


def add_products(name, price, amount):
    query = 'insert into products(name, price, amount) values(%s, %s, %s)'
    data = (name, price, amount)
    cur.execute(query, data)
    con.commit()


def get_products(id):
    query = 'select * from products where id = %s'
    cur.execute(query, id)
    for i in cur.fetchall():
        print(*i)


def show_products():
    query = 'select id, name, price from products'
    cur.execute(query)
    for i in cur.fetchall():
        print(*i)


def delate_product(id):
    query = 'delete from products where id = %s'
    cur.execute(query, (id, ))
    con.commit()
    show_products()

def change_products(id, name, price, amount):
    query = 'update products set name = %s, price = %s, amount = %s where id = %s'
    data = (name, price, amount, id)
    cur.execute(query, data)
    con.commit()
    get_products(id)


while True:

    menu = '''
    1. Barcha mahsulotlar
    2. Mahsulot qushish
    3. mahsulot uchirish
    4. mahsulot uzgartirish
    5. chiqish
    >>>'''
    n = input(menu)
    if n == '1':
        print('Barcha mahsulotlar: ')
        print('id''===''nomi''===''narxi')
        print('=' * 50)
        show_products()
        print('=' * 50)
    elif n == '2':
        add_products(input('Ismi: '), int(input('Narxi: ')), int(input('Miqdori: ')))
        print('Mahsulot qushildi')
        print('=' * 50)
    elif n == '3':
        show_products()
        m = input('mahsulot id sini kriting: ')
        delate_product(m)
        print("O'chirildi")
        print('=' * 50)
    elif n == '4':
        show_products()
        change_products(input('ID: '), input('nomi: '), input('Narxi: '), input('Miqdori: '))
        print("O'zgartirildi")
        print('=' * 50)
    elif n == '5':
        break
    else:
        print('Xato raqam kritdingiz !!')
