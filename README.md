# chislovay_gadalka
#Детская игра с использованием функции random.
# ЧИСЛОВАЯ УГАДАЙКА
import random
count = 0
name = input('Добро пожаловать в игру угадайка! Как тебя зовут?\n')
print('{0}, я загадал число от 1 до 100, а ты попробуй угадать его =)'.format(name))
num = random.randint(1, 101)
while count < 7:
    chislo = int(input('Введите число:'))
    count += 1
    if chislo < 1 or chislo > 100:
        print('Число не входит в заданный диапозон =( ну-ка давай другое =)')
        continue
    if chislo > num:
        print('Неверно,попробуй ещё раз! Загаданное число меньше!')
        continue
    if chislo < num:
        print('Неправда, загаданное число чуть больше!')
        continue
    if chislo == num:
        break
if chislo == num:
    print('Ура! Ты угадал! Это было число:', num)
else:
    print('Ничего страшного, {0}, в следющий раз! На самом деле я загадал число:'.format(name), num)
