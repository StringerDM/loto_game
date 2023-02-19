import random

from card import Card

print('Игра начинается')


player_card = Card('Ваша карточка')
comp_card = Card('Карточка компьютера')
barrels = [i for i in range(1, 91)]
player_count = 0
comp_count = 0

while True:
    number = barrels.pop(random.randint(0, len(barrels) - 1))
    print(f'Новый бочонок: {number} (осталось {len(barrels)})')
    player_card.print_card()
    comp_card.print_card()
    player_answer = input('Зачеркнуть цифру? (y/n): ')
    is_answer_correct = player_card.try_number(number)
    if player_answer == 'y':
        if not is_answer_correct:
            print('Такого числа нет на вашей карточке, вы проиграли!')
            break
        else:
            player_count += 1
    elif player_answer == 'n':
        if is_answer_correct:
            print('Такое число есть на вашей карточке, вы проиграли!')
            break
    if comp_card.try_number(number):
        comp_count += 1

    if player_count == 15:
        print('Вы победили!')
        break
    if comp_count == 15:
        print('Победил комьютер!')
        break

