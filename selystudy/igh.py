from dtbs import users, products

session = dict


def check_user(username, password):
    global session
    for i in users:
        if username == i.get('username') and password == i.get('password'):
            session = i
            return True
    else:
        return False


def show_balance(username):
    for i in users:
        if i.get('username') == username:
            return i.get('balance')
    return 0


def product(count, choice_product):
    products[choice_product - 1]['count'] = products[choice_product - 1]['count'] - count


def user(all_sum):
    for i in users:
        if i.get('username') == session.get('username'):
            i['balance'] = i['balance'] - all_sum
            print(f"Sizdan {all_sum} SUM yechib olindi")
            print(f"Sizda {i['balance']} SUM qoldi")
            break


def user_menu(username):
    i = '\n\n\n'
    print('1. Shop')
    print('2. Balance')
    print('3. logout')

    click_btn = input('>>>')

    if click_btn == '1':
        for i, v in enumerate(products, 1):
            print(f"{i}) {v.get('name')} -> {v.get('price')} SUM : count {v.get('count')}")
        choice = input('>>>')
        if not choice.isnumeric() and not 1 <= int(choice) <= len(products):
            print("Bunday tanlov yo'q ❌")
            user_menu(username)
        count = int(input('Nechta olmoqchisiz ? :\n>>>'))
        if count * products[int(choice) - 1].get('price') > session.get('balance'):
            print("Hisobingizda yetarlicha mablag'yoq ⛔️")
            user_menu(username)

        if products[int(choice) - 1].get('count') <= count:
            print(f"Bizda {products[int(choice) - 1].get('count')} ta shuncha qolgan")
            user_menu(username)

        user(count * products[int(choice) - 1].get('price'))
        product(count, int(choice))

        print(i)

        user_menu(username)



    elif click_btn == '2':
        print(f"Sizning balansingiz {show_balance(username)} Sum")
        user_menu(username)
    elif click_btn == '3':
        print('🔙 Back\n\n\n')
        print('---------------------------------')


def menu():
    q = "ASSALOMU ALEYKUM BZNING DUKONIMIZGA XUSH KELIBSIZ 🙌"
    print(q)
    while True:
        print('1. Register')
        print('2. Login')
        print('3. Exit')
        click = input('>>>')

        if click == '1':
            # ism = input('Ismingizni kriting ')
            # print('______________________________')
            # parol = int(input('parolingizni kriting '))
            # print('_____________________________________')
            # confpass = int(input('parolingizni qayta kriting '))
            # print('_____________________________________________')

            new_user = ({'username': input("Enter Username : "),
                         'password': input("Enter Password : "),
                         'balance': int(input('Enter your balance : '))})
            print('Foydalanuvchi Yaratildi ✅')
            users.append(new_user)

            # if (parol == confpass):
            #     print('Foydalanuvchi Yaratildi ✅')
            #     users.append(ism,parol,)

            # else:
            #     print('ism yoki parol xato kritilgan 😢')
            #     print('_____________________________________')
            #     print('iltimos qayta urunib kuring')
        elif click == '2':
            username = input('Username : ')
            password = input('Password : ')
            response = check_user(username, password)
            if response:

                print('Muvaffaqiyatli kirish ✅')
                print('-------------------------')
                print('Assalomu aleykum 👋')
                print('Iltimos pasdagi bulimlardan birini tanlang 👇')
                user_menu(username)
            else:
                print('Bunday foydalanuvchi mavjud emas ❌')
                print('---------------------------------')
                print('ismingiz va parolingizni qayta tekshirib kuring! ')
        elif click == '3':
            break


menu()

print("Program finish !")

