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
                    2 модуль
  Гонка спидстеров
n = int(input())
k = int(input())
if n > k:
    print('NO')
if k > n:
    print('YES')
if n == k:
    print('Dont know')
  Вид треугольника
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Равносторонний')
if a == b or b == c or c == a:
    print('Равнобедренный')
if a != b != c:
    print('Разносторонний')
  Среднее число
a = int(input())
b = int(input())
c = int(input())
x = (a + b + c)//3
print(x)
  Церемония взвешивания
a = int(input())
if a < 60:
    print('Легкий вес')
if 60 <= a < 64:
    print('Первый полусредний вес')
if 64 <= a < 69:
    print('Полусредний вес')
  Количество дней
a = int(input())
if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
    print('31')
if a == 2:
    print('29')
if a == 4 or a == 9 or a == 11 or a == 6:
    print('30')
  Цветовой микшер
a = input()
b = input()
if (a == 'красный' and b == 'синий') or (a =='синий' and b == 'красный'):
    print('фиолетовый')
if (a == 'красный' and b == 'желтый') or (a == 'желтый' and b == 'красный'):
    print('оранжевый')
if (a == 'синий' and b == 'желтый') or (a == 'желтый' and b == 'синий'):
    print('зеленый')
else:
    print('Ошибка')
  Цвета колеса рулетки
a = int(input())
if a < 0 or a > 36:
    print('ошибка ввода')
elif a == 0:
    print('зеленый')
elif (1 <= a <= 10) or (19 <= a <= 28):
    if a % 2 == 0:
        print('черный')
    else:
        print('красный')
elif (11 <= a <= 18) or (29 <= a <= 36):
    if a % 2 == 0:
        print('красный')
    else:
        print('черный')
  Пересечение отрезков
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a2 < a1:
    print(b1, a1)
if b2 < a1:
    print('Пустое множество')
elif b2 == a1:
    print(b2)
elif a1 < b2 <= b1:
    print(a1, b2)
elif b2 > b1:
    print(a1, b1)
elif a2 == a1:
    if b2 <= b1:
        print(a2, b2)
    else:
        print(a2, b1)
elif a2 < b1:
    if b2 <= b1:
        print(a2, b2)
    else:
        print(a2, b1)
elif a2 == b1:
    print(a2)
else:
    print('Пустое множество')
  Самописный калькулятор
a = int(input())
b = int(input())
c = input()
if c == '+':
    print(a + b)
if c == '-':
    print(a - b)
if c == '*':
    print(a * b)
if c == '/' and b != 0:
    print(a / b)
if c == '/' and b == 0:
    print('На ноль делить нельзя')
    Контрольная работа
1. print()
2. print('Поэма "Мертвые души" одна из самых интересных')
  print('I'm 16 and I'm from Northern Ireland.')
  print("3.1415")
