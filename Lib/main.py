goods = ['Банан (Зелений)', 23.34, 'Полуниця', 45.56, 'Картопля молода', 15.99, 'Морква мита', 57.78]
users = ['vvv@gmail.com', '1111']
admins = ['vl@admin.com', 'qwerty'] #@admin.com
basket = []
admin_email_pattern = '@admin.com'

is_login_true = False
is_admin = False
try:
    #Авторизація
    while True:
        while True:
            login = input("Ведіть логін: ")
            password = input("Ведіть пароль: ")
            if admin_email_pattern in login:
                if admins.count(login) == 0:
                    print("Такого адміністратора не існує. Спробуйте ще раз")
                    continue
                if admins[admins.index(login) + 1] == password:
                    print("Ви ввійшли як адміністратор")
                    is_admin = True
                    break
                else:
                    print("Пароль не вірний. Спробуйте ще раз")

                    continue


            elif login in users:
                if users[users.index(login) + 1] == password:
                    print(f"Ви ввійшли як користувач - {login}")
                    break
                else:
                    print("Пароль не вірний")
            else:
                print("Користувача з таким логіном не існує")
                print("Бажаєте зареєструватися?")
                answer = input("Ведіть так або ні: ")
                if answer == 'так':
                    users.append(login)
                    users.append(password)
                    print("Ви успішно зареєструвались")
                    print("Ви можете увійти в систему")

        # Робота системи
        while True:
            if is_admin == True:
                print('Ви ввійшли як адміністратор')
                while True:
                    print('Для виходу введіть "exit"')
                    print('Для додавання товару введіть "add"')
                    print('Для видалення товару введіть "del"')
                    print('Для виходу від адміністратора введіть "exit admin"')
                    answer = input("Ведіть команду: ")
                    if answer == 'exit':
                        exit()
                    elif answer == 'add':
                        name = input("Ведіть назву товару: ")
                        price = input("Ведіть ціну товару: ")
                        goods.append(name)
                        goods.append(price)
                        print("Товар додано")
                    elif answer == 'del':
                        name = input("Ведіть назву товару: ")
                        if name in goods:
                            goods.remove(name)
                            goods.remove(goods[goods.index(name) + 1])
                            print("Товар видалено")
                        else:
                            print("Такого товару не існує")
                    elif answer == 'exit admin':
                        is_admin = False
                        break
            else:
                counter = 0
                for i in range(0, len(goods), 2):
                    counter += 1
                    print(f"{counter} : {goods[i]}\t\t{goods[i + 1]}$")
                print('Який продукт бажаєте купити?')
                print('Для виходу введіть "exit"')
                answer = input("Ведіть назву продукту: ")
                if answer == 'exit':
                    print('Бажаєте вийти з програми?')
                    answer = input("Ведіть так або ні: ")
                    if answer == 'так':
                        print('До побачення!')
                        exit()
                    else:
                        break

                else:
                    if answer in goods:
                        basket.append(answer)
                        print("Продукт додано до кошика")
                    else:
                        print("Такого продукту не існує")
                        continue
            break



except Exception as e:
    print(e)