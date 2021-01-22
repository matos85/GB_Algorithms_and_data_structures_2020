'''
https://drive.google.com/file/d/1CyjAuUME30JNKKWAO-QjsAFzzZJ4auEE/view?usp=sharing

Задача №5
Пользователь вводит две буквы.
    Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

Примечания:
Во всех заданиях, где речь идёт о буквах алфавита,
    решения необходимы только для строчных букв латинского алфавита от a до z.

'''
print('Введите две буквы латинского алфавита')
n = input('Введите первую букву: ').lower()
m = input('Введите вторую букву: ').lower()
number1 = ord(n) - 96
number2 = ord(m) - 96
print(f'Позиция буквы {n} в латинском алфавите {number1}')
print(f'Позиция буквы {m} в латинском алфавите {number2}')
x = (number2 - number1 - 1)
print(f'Количество букв между буквами {n} и {m} равняется {x}')