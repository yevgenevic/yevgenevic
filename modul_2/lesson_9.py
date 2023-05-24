# l = [7, 3, 6, 2, 8, 9]
# q = [n for n in l if n % 2 == 0]
# w = [n for n in l if n % 2 != 0]
# print(sorted(q))
# print(sorted(w))


# s = 'helloworld736289'
# unli = 'aeiou'
# k = ''
# t = ''
# a = 0
# for i in s:
#     if i in unli:
#         k += i
#     elif i.isdigit():
#         a+=1
#         for i in a:
#
#
#     else:
#         t += i
#         k = ''.join(sorted(k))
#         t = ''.join(sorted(t))
#
# print(k + t)
# s = 'helloworld736289'

# q = ''.join(sorted(s, key=lambda i: (i not in s, i)))
# print(''.join(sorted(s)))

# print(q)

# a = [2, 3, [2, [2, 3, 5, [3], 2]], 4, [3], 5]
# q = 0
# w = []
# for i in a:
#     if i == '[':
#         w.append(i)
#         q += 1
#     else:
#         break
# print(q)


import json
from datetime import datetime


class File:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, "r") as f:
            try:
                listy = json.load(f)
            except:
                listy = []
        return listy

    def write(self, data) -> None:
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)


class Admin:
    def __init__(self, adminname=None, adminpassword=None):
        self.adminname = adminname
        self.adminpassword = adminpassword

    def check_admin(self):
        admins = File("admin.json").read()
        for admin in admins:
            if admin["adminName"] == self.adminname and admin["adminPassword"] == self.adminpassword:
                return True
        else:
            return False


class User:
    def __init__(self, fullname=None, username=None, password=None, my_product=[]):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.my_product = my_product

    def check_login(self):
        users = File('mijoz.json').read()
        for user in users:
            if user["username"] == self.username:
                return True
        else:
            return False

    def save_user(self):
        obj = File('mijoz.json')
        listy = obj.read()
        listy.append(self.__dict__)
        obj.write(listy)

    def add_product(self, product):
        users = File('mijoz.json').read()
        data = datetime.now()
        product['time'] = data.strftime("%Y:%m:%d %H:%M")
        for user in users:
            if user['username'] == self.username:
                user['my_product'].append(product)
        File('mijoz.json').write(users)

    def my_profile(self):
        users = File('mijoz.json').read()
        for user in users:
            if user['username'] == self.username:
                for i in user['my_product']:
                    print(f"{i['name']} -> price: {i['price']} -> count: {i['count']} -> {i['time']}")

    def user_case_1(self, choice, amount, filename):
        users = File(filename).read()
        for user in users:
            if user['username'] == self.username:
                for i in user['my_product']:
                    if i['id'] == choice:
                        i['count'] = amount
                        with open(filename, 'w') as f:
                            json.dump(users, f, indent=3)

    def productni_tekt(self):
        users = File("mijoz.json").read()
        for user in users:
            if user['username'] == self.username:
                if user['my_product']:
                    return True
                return False

    def get_hisob(self):
        filename = File("mijoz.json").read()
        for user in filename:
            count = 0
            if user["username"] == self.username:
                for i in user["my_product"]:
                    count += i["count"] * i["price"]
                print("Sizdan ", count, "bo'ldi")


class Product:
    def __init__(self, id=None, name=None, price=None, amount=None):
        self.id = id
        self.name = name
        self.price = price
        self.amount = amount

    def save_product(self):
        products = File("products.json").read()
        products.append(self.__dict__)
        File('products.json').write(products)

    def user_case_1(self, choice, amount, filename):
        ovqatlar = File(filename).read()
        for ovqat in ovqatlar:
            if choice == ovqat['id']:
                ovqat['count'] -= amount
                with open(filename, 'w') as f:
                    json.dump(ovqatlar, f, indent=3)


def admin_add_product2(pid, pname, pprice, pamount):
    file = File("products.json").read()
    for n in file:
        if n["name"] != pname:
            continue
        if n["name"] == pname:
            n['count'] += pamount
            n['price'] = pprice
            with open("products.json", "w") as f:
                json.dump(file, f, indent=3)
            return True
        return False


def admin_add_product3(pid, pname, pprice, pamount):
    file = File("products.json").read()
    for n in file:
        if n["name"] != pname:
            file.append(
                {
                    "id": pid,
                    "name": pname,
                    "price": pprice,
                    "count": pamount
                }
            )
            with open("products.json", "w") as f:
                json.dump(file, f, indent=3)
            break
    print("Mahsulot qo'shildi")


def case_admin_1(admin):
    x = File("products.json").read()
    k = 0
    for xy in x:
        if k < xy["id"]:
            k = xy["id"]
    print(k, " ta mahsulot bor")
    pid = int(input("id: "))
    pname = input("name: ")
    pprice = int(input("price: "))
    pamount = int(input("count: "))
    b = admin_add_product2(pid, pname, pprice, pamount)
    if b:
        print(b)
        print("1->Yana mahsulot qo'shish")
        print("2->menu")
        op = input(">>>")
        match op:
            case "1":
                case_admin_1(admin)
            case "2":
                adminMenu(admin)
    else:
        print(b)
        admin_add_product3(pid, pname, pprice, pamount)
        print("1->Yana mahsulot qo'shish")
        print("2->menu")
        op = input(">>>")
        match op:
            case "1":
                case_admin_1(admin)
            case "2":
                adminMenu(admin)


def case_admin_2(admin):
    users = File("mijoz.json").read()
    summa = 0
    for user in users:
        for us in user["my_product"]:
            pass
            print(user["username"], "=-->", us["name"], "->", us["price"], "->", us["count"])
            print("-----------------------------------------")
            summa += us["count"] * us["price"]
    print("----------------------------")
    print("|                           |")
    print("|Opshe Tushum->", summa, "     |")
    print("|                           |")
    print("|___________________________|")
    adminMenu(admin)


def case_admin_3(admin):
    newsAdmin = input("adminName: ")
    newsAdminPassword = input("adminPassword: ")
    f = File("admin.json").read()
    f.append(
        {
            "adminName": newsAdmin,
            "adminPassword": newsAdminPassword
        }
    )
    print("Admin qo'shildi")
    print("-----------------------------------------")
    with open("admin.json", "w") as file:
        json.dump(f, file, indent=3)
    adminMenu(admin)


def case_admin_4(admin):
    mahsulotlar = File('products.json').read()
    for mahsulot in mahsulotlar:
        print(mahsulot["name"], "->price->", mahsulot["price"], "-> count->", mahsulot['count'])
    print("\n")
    adminMenu(admin)


def adminMenu(admin):
    print("1->mahsulot qoshish")
    print('2->hisobot')
    print("3->admin qo'shish")
    print("4->mahsulotlarni ko'rish")
    print("5->Exit")
    tanlov = input(">>>")
    match tanlov:
        case '1':
            case_admin_1(admin)
        case "2":
            case_admin_2(admin)
        case "3":
            case_admin_3(admin)
        case "4":
            case_admin_4(admin)
        case "5":
            magazin()


def get_desktop(filename, filename2, user):
    products = File(filename).read()
    text = ''
    for i, product in enumerate(products, 1):
        text += f"{i}){product['name']}-> price = {product['price']}\n"
    print(text)
    choice = int(input('\n>>>'))
    amount = int(input("count: "))
    user.add_product(products[choice - 1])
    user.user_case_1(choice, amount, filename2)
    Product().user_case_1(choice, amount, filename)
    bool_ = user.productni_tekt()
    if bool_:
        print("Buyurtma  sotib olindi\n")
    print("1->yana mahsulot olish")
    print("2->menuga qaytish")
    exit = input(">>>\n")  # noqa
    match exit:
        case "1":
            get_desktop(filename, filename2, user)
        case "2":
            menu(user)


def menu(user):
    print("1. Mahsulotlar")
    print("2. oldingi xaridlar")
    print("3. hisob")
    print("4. chiqish")
    menuTanlov = input(">>>")
    match menuTanlov:
        case "1":
            print("\n")
            get_desktop('products.json', 'mijoz.json', user)
            print("\n")
        case "2":
            print("\n")
            user.my_profile()
            print("\n")
            menu(user)
            print("\n")
        case '3':
            user.get_hisob()
            print("\n")
            menu(user)
        case "4":
            print("Sog'bo'lasiz")
    return


def magazin():
    while True:
        d = """
        1.login
        2.register
        >>>"""
        userTanlov = input(d)
        if userTanlov == '1':
            username = input("username: ")
            password = input("password: ")
            user = User(username=username, password=password)
            b = user.check_login()
            admin = Admin(username, password)
            q = admin.check_admin()
            if q:
                print("Admin xush kelipsiz")
                adminMenu(admin)
            if b:
                print("mijoz xush kelipsiz")
                menu(user)
            else:
                print("bizda bunday user mavjud emas")
        if userTanlov == "2":
            name = input("name: ")
            username = input("username: ")
            password = input('password: ')
            user = User(name, username, password)
            b = user.check_login()
            if not b:
                print("Siz registratsiyadan o'tdingiz")
                user.save_user()
                magazin()
            else:
                print("bizda bunday user bor")
                magazin()


magazin()
