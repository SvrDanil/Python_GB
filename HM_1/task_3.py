# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint

lower_rand = 0
upper_rand = 1001
first = 1
last = 11

secret_num = randint(lower_rand, upper_rand)
for i in range(first, last):
    n = int(input(f"Попытка номер {i}, введите число: "))
    turn = ""
    if n > secret_num :
        turn = "Меньше"
    elif n < secret_num :
        turn = "Больше"
    else:
        print("Победа!")
        break
    print(turn)
else:
    print("Вы проиграли.")
    print(f"Загаданное число было: {secret_num}")