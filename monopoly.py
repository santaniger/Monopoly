# -*- coding: utf-8 -*-
import random
import os
import webbrowser
k=0
l=0
def check():
    global player1_pass
    global player2_pass
    global k
    if player1_pass > 15:
        k=1
    if player2_pass > 15:
        k=2
def new_game():
    global player1_pos
    global player2_pos
    global player1_bal
    global player2_bal
    global player1_pass
    global player2_pass
    global lot
    global lot_cost
    global lot_size
    player1_pos=0
    player2_pos=0
    player1_bal=1500
    player2_bal=1500
    player1_pass=0
    player2_pass=0
    lot=["ВПЕРЁД", "Мадрид", "ШАНС", "Гитхорн", "АЭРОПОРТ Берлин-Бранденбург", "МОНОПОЛИЯ", "Тайбэй", "Первый класс", "Кейптаун", "Куинстаун", "Просто посетители", "ТЮРЬМА", "Сидней", "ШАНС", "Амстердам", "Нью-Йорк", "МОНОПОЛИЯ", "Токио", "Первый класс", "Москва", "Лондон", "БЕСПЛАТНАЯ СТОЯНКА", "Белград", "ШАНС", "Афины", "Белфаст", "МОНОПОЛИЯ", "Сантьяго", "Мехико", "ПЕРВЫЙ КЛАСС", "Варшава", "ОТПРАВЛЯЙТЕСЬ В ТЮРЬМУ", "Стамбул", "Лиссабон", "ШАНС", "Рига", "Монополия", "АЭРОПОРТ Им. Генри Коанды", "Гонконг", "ПЕРВЫЙ КЛАСС", "Лима"]
    lot_cost=[-200, 60, 0, 60, 100, 0, 100, 100, 100, 100, 0, 0, 160, 0, 160, 160, 0, 200, 100, 200, 200, 0, 260, 0, 260, 260, 0, 300, 300, 100, 300, 0, 360, 360, 0, 360, 0, 100, 400, 100, 400]
    lot_size=[0, 1.6, 0, 1.6, 0, 0, 1.6, 1.4, 1.6, 1.6, 0, 0, 1.8, 0, 1.8, 1.8, 0, 1.8, 1.4, 1.8, 1.8, 0, 2.2, 0, 2.2, 2.2, 0, 2.2, 2.2, 1.4, 2.2, 0, 2.5, 2.5, 0, 2.5, 0, 0, 2.5, 1.4, 2.5]
def cubes1():
    global player1_pos
    print("\n-------------------------------\nХод игрока №1")
    input("Enter- Бросить кубики\n")
    first_cube= random.randint(1, 6)
    second_cube= random.randint(1, 6)
    goto= first_cube+second_cube
    print("Выпало ", goto)
    if goto + player1_pos < 41:
        player1_pos = goto + player1_pos
#        player1_pos=12
    else:
        player1_pos = goto + player1_pos - 41
def cubes2():
    global player2_pos
    print("\n-------------------------------\nХод игрока №2")
    input("Enter- Бросить кубики\n")
    first_cube= random.randint(1, 6)
    second_cube= random.randint(1, 6)
    goto= first_cube+second_cube
    print("Выпало ", goto)
    if goto + player2_pos < 41:
        player2_pos = goto + player2_pos
#        player2_pos=12
    else:
        player2_pos = goto + player2_pos - 41
def first_player_buy():
    global player1_bal
    global player1_pass
    global lot_size
    global player1_pos
    print(lot[player1_pos], "\nВаш баланс:", player1_bal, "\nСтоимость:", lot_cost[player1_pos], "\nСостояние паспорта:", player1_pass, "/ 15", "\nРазмер штампа:", lot_size[player1_pos])
    menu=int(input("1)Купить\n2)Пропустить\n"))
    if menu == 1:
        player1_bal=player1_bal-lot_cost[player1_pos]
        player1_pass=player1_pass+lot_size[player1_pos]
        print("Сделка совершена!\nВаш баланс:", player1_bal, "\nСостояние паспорта:", player1_pass, "/ 15")
    else:
        print("Пропущено")
    input("Enter- следующий ход")
    print ("OK")
def second_player_buy():
    global player2_bal
    global player2_pass
    global lot_size
    global player2_pos
    print(lot[player2_pos], "\nВаш баланс:", player2_bal, "\nСтоимость:", lot_cost[player2_pos], "\nСостояние паспорта:", player2_pass, "/ 15", "\nРазмер штампа:", lot_size[player2_pos])
    menu=int(input("1)Купить\n2)Пропустить\n"))
    if menu == 1:
        player2_bal=player2_bal-lot_cost[player2_pos]
        player2_pass=player2_pass+lot_size[player2_pos]
        print("Сделка совершена!\nВаш баланс:", player2_bal, "\nСостояние паспорта:", player2_pass, "/ 15")
    else:
        print("Пропущено")
    input("Enter- следующий ход")
    print ("OK")
def jail1():
    print("Вы попали в тюрьму за критику власти! Выйти можно выкинув дубль за 3 попытки или заплатить 100м!")
    global player1_pos
    input("Enter-кинуть кубики 1 раз")
    first_cube_jail = random.randint(1, 6)
    second_cube_jail = random.randint(1, 6)
    print("Выпало ", first_cube_jail, "и", second_cube_jail)
    if first_cube_jail == second_cube_jail:
        print("Поздравляем! Вам повезло!")
        player1_pos = first_cube_jail + second_cube_jail + player1_pos
        first_player_buy()
    else:
        input("Enter-кинуть кубики 2 раз")
        first_cube_jail = random.randint(1, 6)
        second_cube_jail = random.randint(1, 6)
        print("Выпало ", first_cube_jail, "и", second_cube_jail)
        if first_cube_jail == second_cube_jail:
            print("Поздравляем! Вам повезло!")
            player1_pos = first_cube_jail + second_cube_jail + player1_pos
            first_player_buy()
        else:
            input("Enter-кинуть кубики 3 раз")
            first_cube_jail = random.randint(1, 6)
            second_cube_jail = random.randint(1, 6)
            print("Выпало ", first_cube_jail, "и", second_cube_jail)
            if first_cube_jail == second_cube_jail:
                print("Поздравляем! Вам повезло!")
                player1_pos = first_cube_jail + second_cube_jail + player1_pos
                first_player_buy()
            else:
                print("Увы, вы выходите из тюрьмы за 100м! кидайте кубы!")
                cubes1()
                first_player_buy()
def jail2():
    print("Вы попали в тюрьму за критику власти! Выйти можно выкинув дубль за 3 попытки или заплатить 100м!")
    global player2_pos
    input("Enter-кинуть кубики 1 раз")
    first_cube_jail = random.randint(1, 6)
    second_cube_jail = random.randint(1, 6)
    print("Выпало ", first_cube_jail, "и", second_cube_jail)
    if first_cube_jail == second_cube_jail:
        print("Поздравляем! Вам повезло!")
        player2_pos = first_cube_jail + second_cube_jail + player2_pos
        second_player_buy()
    else:
        input("Enter-кинуть кубики 2 раз")
        first_cube_jail = random.randint(1, 6)
        second_cube_jail = random.randint(1, 6)
        print("Выпало ", first_cube_jail, "и", second_cube_jail)
        if first_cube_jail == second_cube_jail:
            print("Поздравляем! Вам повезло!")
            player2_pos = first_cube_jail + second_cube_jail + player2_pos
            second_player_buy()
        else:
            input("Enter-кинуть кубики 3 раз")
            first_cube_jail = random.randint(1, 6)
            second_cube_jail = random.randint(1, 6)
            print("Выпало ", first_cube_jail, "и", second_cube_jail)
            if first_cube_jail == second_cube_jail:
                print("Поздравляем! Вам повезло!")
                player2_pos = first_cube_jail + second_cube_jail + player2_pos
                second_player_buy()
            else:
                print("Увы, вы выходите из тюрьмы за 100м! кидайте кубы!")
                cubes2()
                second_player_buy()
if __name__ == '__main__':
    while l==0:
        print(" /$$      /$$                                                   /$$          \n| $$$    /$$$                                                  | $$          \n| $$$$  /$$$$  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ | $$ /$$   /$$\n| $$ $$/$$ $$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$| $$  | $$\n| $$  $$$| $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$| $$  | $$\n| $$\  $ | $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$| $$  | $$\n| $$ \/  | $$|  $$$$$$/| $$  | $$|  $$$$$$/| $$$$$$$/|  $$$$$$/| $$|  $$$$$$$\n|__/     |__/ \______/ |__/  |__/ \______/ | $$____/  \______/ |__/ \____  $$\n                                           | $$                     /$$  | $$\n                                           | $$                    |  $$$$$$/\nDEMO 0.1                                   |__/                     \______/ \n")
        main_menu=input("MENU\n1)Играть!\n2)Правила\n3)План обновлений\nВыбор: ")
        if main_menu=="1":
            clear = lambda: os.system('cls')
            clear()
            new_game()
            while k==0:
                cubes1()
                if player1_pos==11:
                    jail1()
                else:
                    first_player_buy()
                check()
                cubes2()
                if player2_pos==11:
                    jail2()
                else:
                    second_player_buy()
                check()
            if k==1:
                print("Победа первого игрока! Поздравляем!")
            if k==2:
                print("Победа второго игрока! Поздравляем!")
        if main_menu == "2":
            print("Правила просты, у каждого игрока есть паспорт, на игровом поле есть города, у каждого города есть свой штамп, каждый штамп в свою очередь имеет свой размер.\nВыигрывает тот, кто первый заполнит свой паспорт штампами.\nДля получения более подробной информации введите 2")
            menu=int(input("Ввод: "))
            input("Enter- назад в меню")
            clear = lambda: os.system('cls')
            clear()
            if menu=="2":
                webbrowser.open("https://disk.yandex.ru/i/IqwK0yjl1V7u3w")
                print("Переадресация")
        if main_menu=="3":
            print("1)Карточки 'Шанс'\n2)Отправка карточек 'Монополия' на почту\n3)Рента\n4)Собственность\n5)Аэропорты\n6)Штампы 'первый класс'\n7)История игр\nВторой поток под бота")
            input("Enter- назад в меню")
            clear = lambda: os.system('cls')
            clear()
