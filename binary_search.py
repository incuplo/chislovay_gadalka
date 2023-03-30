import random

count = 0
name = input('Добро пожаловать в игру угадайка! Как тебя зовут?\n')
print(f'{name}, я загадал число от 1 до 100, а ты попробуй угадать его')
range_ = random.randint(1, 101)
flag = True
while True:
    number = int(input('Введите число:'))
    count += 1
    if number < 1 or number > 100:
        print('Число не входит в заданный диапазон')
    elif number > range_:
        print('Неверно,попробуй ещё раз! Загаданное число меньше!')
    elif number < range_:
        print('Неправда, загаданное число чуть больше!')
    else:
        print('Ура! Ты угадал! Это было число:', range_)
        flag = False
        break