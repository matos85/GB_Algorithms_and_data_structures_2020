'''
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.


'''
print('Введите натуральное число!')
i = int(input('Ввведите ваше число: '))
r = 0
while i > 0:
    z = i % 10
    i = i // 10
    r = r * 10
    r = r + z
print(f'Обратное вашему числу есть число: {r}')
