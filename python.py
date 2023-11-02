  Пересчет ввременного интервала
a = int(input())
b = a // 60
c = a - b * 60
print(a, 'мин - это', b, 'час', c, 'минут')
  Трехзначное число
m = int(input())
a = m // 100
b = m % 100 // 10
c = m % 10
n = a + b + c
d = a * b * c
print('Сумма цифр =', n)
print('Произведение цифр =', d)
  Четырехзначное число
a = int(input())
b = a // 1000
c = (a - b * 1000) // 100
d = (a - (b * 1000) - c * 100) // 10
e = (a - (b * 1000) - c * 100 - d * 10) // 1
print('Цифра в позиции тысяч равна', b)
print('Цифра в позиции сотен равна', c)
print('Цифра в позиции десятков равна', d)
print('Цифра в позиции единиц равна', e)
  Пароль
a = input()
b = input()
if a == b:
    print('Пароль принят')
else:
    print('Пароль не принят')
  Четное или нечетное
a = int(input())
if a % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
  Роскомнадзор
a = int(input())
if a >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')
  Наименьшее из двух чисел
a = int(input())
b = int(input())
if a < b:
    print(a)
if b < a:
    print(b)
  Наименьшее из четырех чисел
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min(a, b, c, d))
  Возростная группа
a = int(input())
if a <= 13:
    print('Детство')
if a >=14 | a <= 24:
    print('Молодость')
if a >= 25 | a <= 59:
    print('Зрелость')
if a >= 60:
    print('Старость')
  Только +
a = int(input())
b = int(input())
c = int(input())
print((a if a > 0 else 0) + (b if b > 0 else 0) + (c if c > 0 else 0))
  Красивое число
a = int(input())
if (1000 <= a <= 9999) and ( a % 7 == 0 or a % 17 == 0):
    print('YES')
else:
    print("NO")
  
