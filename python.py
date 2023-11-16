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
  print()
3. print('Python', 'is the best', '!!')
4. print("The world's a little blurry", "Or maybe it's my eyes", end='!!!', sep=':)')
  print("Honey, what's your hurry", end='?')
  print("Told you not to worry", "But maybe that's a lie" sep=':)')
5. input()
6. n = int(input())
7. - Имя переменной может начинаться с символа подчеркивания (_)
    - Имя переменной не может начинаться с цифры
    - Имя переменной не может совпадать с ключевым (зарезерврованным) словом
8. 60
9. 56
10. print('*****************')
    print('*               *')
    print('*               *')
    print('*****************')
11. a = int(input())
    b = int(input())
    x = (a + b) ** 2
    y = a ** 2 + b ** 2
    print('Квадрат суммы', a, 'и', b, 'равен', x)
    print('Сумма квадратов', a, 'и', b, 'равна', y)
12. a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(a ** b + c ** d)
13. n = int(input())
    nn = n * 10 + n
    nnn = n * 100 + n * 10 + n
    print(n + nn + nnn)
            Модуль 3
      Площадь треугольника
a = int(input())
b = int(input())
s = 1/2 * a * b
print(s)
      Две старушки
S = float(input())
V1 = float(input())
V2 = float(input())
t = S / (V1 + V2)
print(t)
      Обратное число
a = float(input())
if a == 0:
    print('Обратного числа не существует')
else:
    b = a ** -1
    print(b)
      451 градус по Фаренгейту
F = float(input())
C = (5 / 9) * (F - 32)
print(C)
      Dog age
a = int(input())
if a <= 2:
    print(a * 10.5)
else:
    print(a * 4)
      Первая цифра после точки
a = float(input())
x = (a * 10) % 10
print(int(x))
      Дробная часть
a = float(input())
x = a - int(a)
print(x)
      Наименьшее и наибольшееa = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print('Наименьшее число = ', (min(a,b,c,d,e)))
print('Наибольшее число = ', (max(a,b,c,d,e)))
      Сортировка трех
a = int(input())
b = int(input())
c = int(input())
x = max(a,b,c)
n = min(a,b,c)
y = (a + b + c - x - n)
print(x)
print(y)
print(n)
      Интересное число
a = int(input())
x = a // 100
y = (a - (x * 100)) // 10
n = a - ((x * 100) + (y * 10))
if max(x,y,n) - min(x,y,n) == (x + y + n) - max(x,y,n) - min(x,y,n):
    print('Число интересное')
else:
    print('Число неинтересное')
      Абсолютная сумма
a1 = float(input())
a2 = float(input())
a3 = float(input())
a4 = float(input())
a5 = float(input())
x = abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5)
print(x)
      Манхэттенское движение
p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())
x = abs(p1 - q1) + abs(p2 - q2)
print(x)
      Неизвестное название задания
print('"Python is a great language!", said Fred. I do not ever remember having this much fun before."')
      What's Your Name?
a = input()
b = input()
print('Hello', a, b, '!', 'You have just delved into Python')
      Футбольная команда
a = input()
print('Футбольная команда', a, 'имеет длину', len(a), 'символов')
      Три города
a = input()
b = input()
c = input()
x = len(a)
y = len(b)
n = len(c)
if x == min(x,y,n):
    print(a)
elif y == min(x,y,n):
    print(b)
else:
    print(c)
if x == max(x,y,n):
    print(a)
elif y == max(x,y,n):
    print(b)
else:
    print(c)
      Пол и потолок
a = float(input())
x = abs(a) + abs(a)
print(int(x))
      Арифметичесские строки
a = len(input())
b = len(input())
c = len(input())
if a + b + c == (max(a,b,c) + min(a,b,c)) // 2 * 3:
    print('YES')
else:
    print('NO')
      Евклидово расстояние
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
p = ((x1 - x2) ** 2 + (y1- y2) ** 2) ** 0.5
print(p)
      Средние значения
a = float(input())
b = float(input())
y = (a + b) / 2
x = (a * b) ** 0.5
z = (2 * a * b) / (a + b)
c = ((a ** 2 + b ** 2) / 2) ** 0.5
print(y)
print(x)
print(z)
print(c)
