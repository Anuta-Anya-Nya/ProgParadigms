from random import randint


def print_game(game_list):
    field = f"-------------\n| {game_list[0]} | {game_list[1]} | {game_list[2]} |\n-------------\n| {game_list[3]} | {game_list[4]} | {game_list[5]} |\n-------------\n| {game_list[6]} | {game_list[7]} | {game_list[8]} |\n-------------\n"
    print(field)


def is_win(game_list, count, end):
    result = (game_list[0] == game_list[1] and game_list[1] == game_list[2]) or (
        game_list[3] == game_list[4] and game_list[5] == game_list[4]) or (
        game_list[6] == game_list[7] and game_list[7] == game_list[8]) or (
        game_list[0] == game_list[3] and game_list[3] == game_list[6]) or (
        game_list[1] == game_list[4] and game_list[4] == game_list[7]) or (
        game_list[2] == game_list[5] and game_list[5] == game_list[8]) or (
        game_list[0] == game_list[4] and game_list[4] == game_list[8]) or (
        game_list[2] == game_list[4] and game_list[4] == game_list[6]) or count == 9 or end
    return result


def change_person(person):
    person = int(not bool(person))
    return person


def start():
    print("Привет! давай поиграем в крестики-нолики!")
    return input("Готовы играть? 2-да, 1-выход ")


def first_step():
    global my_game_list, person, count, end
    user_answer = start()
    if (user_answer == '2'):
        print("Определяем, какой игрок ходит первым...")
        person = randint(0, 1)
        if person:
            print("Первым ходит игрок 2!")
        else:
            print("Первым ходит игрок 1!")
        print_game(my_game_list)
        print(f"Ход игрока {person+1}. Введите число от 1 до 9. Выход - 0")
        play_game()
    elif (user_answer == '1'):
        print("До свидания!")
    else:
        user_answer = input("Введено неверное число!")
        first_step()


def play_game():
    global my_game_list, person, count, end

    while not is_win(my_game_list, count, end):
        number = input("введите число: ")
        if number == '':
            print("Введено неверное значение! Введите число от 1 до 9. Выход - 0")
            play_game()
        elif number in '1 2 3 4 5 6 7 8 9':
            number = int(number)
            if my_game_list[number-1] == number:
                if person:
                    my_game_list[number-1] = chr(10060)
                else:
                    my_game_list[number-1] = chr(11093)
                count += 1
                print_game(my_game_list)

                if not is_win(my_game_list, count, end):
                    person = change_person(person)
                    print(
                        f"Ход игрока {person+1}. Введите число от 1 до 9. Выход - 0")
                    play_game()
                else:
                    if count == 9:
                        print("Ничья")
                    else:
                        print(f"Игрок {person+1} выиграл!!!")
            else:
                print(
                    "Указанное место уже занято! Введите другое число от 1 до 9. Выход - 0")
                play_game()
        elif number == '0':
            print("До свидания!")
            end = True
        else:
            print("Введено неверное значение! Введите число от 1 до 9. Выход - 0")
            play_game()


person = 0
my_game_list = [i for i in range(1, 10)]
count = 0
end = False
first_step()
