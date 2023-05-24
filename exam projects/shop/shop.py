import json
from time import strftime
from colorama import Back, Fore
import bcrypt


def hashing(data):
    data = data.encode('ASCII')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(data, salt)
    hashed = hashed.decode('ASCII')
    return hashed


def hashing_read(data, password):
    data = data.encode('ASCII')
    password = password.encode('ASCII')
    if bcrypt.checkpw(password, data):
        return True
    else:
        return False


class File:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            try:
                list_ = json.load(file)
            except:
                list_ = []
        return list_

    def write(self, data) -> None:
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=3)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = hashing(password)
        self.myproduct = []

    def save_user(self):
        obj = File('user.json')
        list_ = obj.read()
        list_.append(self.__dict__)
        obj.write(list_)

    def check_username(self):
        obj = File('user.json')
        list_ = File('admin.json').read()
        q = []
        for i in obj.read():
            if self.username == i['username']:
                q.append(False)
                break
        else:
            q.append(True)

        for i in list_:
            if self.username == i['username']:
                q.append(False)
                break
        else:
            q.append(True)

        if q[0] == True and q[1] == True:
            return True
        else:
            return False

    def check_login(self, password):
        obj = File('user.json')
        for i in obj.read():
            if i['username'] == self.username and hashing_read(i['password'], password):
                return True
        else:
            return False

    def user_product(self):
        user = File('user.json').read()
        for i in user:
            print(*i['myproduct'], end='')

    def price(self, amount, id):
        a = False
        product = File('product.json').read()
        userss = File('user.json').read()
        my_product = File('my_product.json').read()
        new = {}

        for i in product:
            string = strftime('%Y-%m-%d %H:%M:%S %p')
            if i['id'] == id and i['amount'] >= amount:
                new.update({
                    "name": i['name'],
                    "amount": amount,
                    "id": id,
                    "time": string,
                })
                a = True
        if a:
            my_product.append(new)
            File('my_product.json').write(my_product)
            sh = 'Mahsulot sotib olindi'
            print(sh.expandtabs(50))
        sum = File('product.json').read()
        for i in sum:
            if i['id'] == id and i['amount'] >= amount:
                i['amount'] -= amount
            elif i['id'] == id and i['amount'] < amount:
                print("bizda buncha mahsulot yoq")
            File('product.json').write(sum)
        for j in userss:
            if j['username'] == username and a:
                j['myproduct'].append(new)
        File('user.json').write(userss)


class Admin:
    def __init__(self, username, password):

        self.username = username
        self.password = hashing(password)
        self.new_product = []

    def save_user(self):
        obj = File('admin.json')
        list_ = obj.read()
        list_.append(self.__dict__)
        obj.write(list_)

    def check_username(self):
        obj = File('admin.json')
        list_ = File('user.json').read()
        q = []
        for i in obj.read():
            if self.username == i['username']:
                q.append(False)
                break
        else:
            q.append(True)

        for i in list_:
            if self.username == i['username']:
                q.append(False)
                break
        else:
            q.append(True)

        if q[0] == True and q[1] == True:
            return True
        else:
            return False

    def check_login(self, password):
        obj = File('admin.json')
        for i in obj.read():
            if i['username'] == username and hashing_read(i['password'], password):
                return True
        else:
            return False

    def user_product(self):
        user = File('admin.json').read()
        for i in user:
            print(*i['new_product'], end='')

    def add_product(self, name, amount, id):
        new = {}
        a = False
        obj = File('product.json').read()
        if amount <= 0:
            print(Fore.RED + "minus son kritmang ")
            return 0
        for i in obj:
            if i['name'] != name:
                new.update({
                    'id': id,
                    'name': name,
                    'amount': amount,
                }, )
                a = True
            elif i['name'] == name:
                print('bunaqa nomli product mavjud')
                break
        if a:
            obj.append(new)
            File('product.json').write(obj)
            d = 'MAhsulot qushildi'
            print(d.expandtabs(50))
        data = File('admin.json').read()
        for i in data:
            if username == i['username'] and password == i['password']:
                i['new_product'].append(new)
        File('admin.json').write(data)

    def check_(self, name, amount):
        obj = File('product.json').read()
        for i in obj:
            if i['name'] == name:
                i['amount']: amount
                File('product.json').write(obj)
                return True
        else:
            return False


def get_id():
    with open('product.json') as file:
        data = json.load(file)
        count = 1
        for i in data:
            count += 1
        return count


class Product:
    def __init__(self, name=None, amount=None):
        self.name = name
        self.amount = amount
        self.id = get_id()

    def save_product(self):
        products = File('product.json').read()
        products.append(self.__dict__)
        File('product.json').write(products)

    def take_list(self):
        product = File('product.json').read()
        print(Fore.LIGHTCYAN_EX + '=' * 20 + ' Mahsulotlarimiz ' + Fore.LIGHTCYAN_EX + '=' * 20)
        for i in product:
            print(Fore.LIGHTYELLOW_EX)
            print("id  :", i["id"], "  ", "name : ", i["name"], "  ", 'number of products', i["amount"])
            print(Fore.BLACK + '=' * 50)


while True:
    print(Fore.BLUE + '=' * 10, Fore.LIGHTMAGENTA_EX + 'SHOP', Fore.BLUE + '=' * 10)
    print('tanlang>>>')
    text1 = '''    
    1) Login 
    2) Register
    3) chiqish    
    >>>  '''
    check = input(text1)

    if check == '1':
        username = input("Enter username  : ")
        password = input("Enter password  : ")
        user = User(username=username, password=password)
        if user.check_login(password):
            while True:
                print(Fore.YELLOW)
                text2 = '''    
                    1) Mahsulotlar
                    2) Men olgan mahsulotlar            
                    3) chiqish                
                    >>>  '''
                check2 = input(text2)
                if check2 == '1':
                    info = Product()
                    info.take_list()
                    print(Fore.LIGHTMAGENTA_EX + " mahsulotlarimizdan tanlang")
                    id = int(input("Product id : "))
                    amount = int(input("Product amount : "))
                    buy = User(username, password)
                    if amount > 0 and id > 0:
                        buy.price(amount, id)
                    else:
                        print(Fore.RED)
                        print("MINUS RAQAM KRITMANG ❌ ")

                if check2 == '2':
                    malumot = User(username=username, password=password)
                    obj = File('user.json').read()
                    for i in obj:
                        if i['username'] == username and hashing_read(i['password'], password):
                            print(i['myproduct'])
                if check2 == '3':
                    print(Fore.MAGENTA + "Kelganingiz uchun rahmat 🙂")
                    break
        user1 = Admin(username=username, password=password)
        if user1.check_login(password):
            while True:
                print('tanlang>>')
                text = Fore.YELLOW + """
                 1) Sotib olingan mahsulotlar
                 2) Mahsulot qushish
                 3) Mahsulotlat infarmatsiyasi
                 5) Chiqish
                >>>>"""
                admin = input(text)
                if admin == '2':
                    name = input('Mahsulot nomi : ')
                    amount = int(input('mahsulot amounti : '))
                    buy1 = Admin(username, password)
                    a = Admin(username, password)
                    if a.check_(name, amount):
                        buy1.check_(name, amount)
                    if amount > 0:
                        buy = Product(name, amount)
                        buy.save_product()
                        print('mahsulot saqlandi')
                    else:
                        print("Begzotaka blyet")
                elif admin == '1':
                    data = File('user.json').read()
                    for i in data:
                        print(i)
                elif admin == '3':
                    info = Product()
                    info.take_list()
                elif admin == '5':
                    print(Fore.MAGENTA + "Kelganingiz uchun rahmat 🙂")
                    break
    elif check == '2':
        print(Fore.BLUE)
        username = input("Enter username : ")
        password = input("Enter password : ")
        add = Fore.LIGHTMAGENTA_EX + ''' adminmisiz (ha/ yoq ) '''
        chk1 = input(add)
        if chk1 == 'yoq':
            reg = User(username, password)
            if reg.check_username():
                reg.save_user()
                print("Muvaffaqiyatli Registatsiya")
            else:
                print("Bu username oldin ishlatilgan")
        elif chk1 == 'ha':
            reg1 = Admin(username, password)
            if reg1.check_username():
                reg1.save_user()
                print("Muvaffaqiyatli kirish")
            else:
                print("bu username oldin ishlatilgan")
        else:
            print(Fore.RED + "hato tanlov")
    elif check == '3':
        print('Kelganingiz uchun raxmat 🙂')
        break
    else:
        print(Fore.RED + 'Xato tanlov❌')

