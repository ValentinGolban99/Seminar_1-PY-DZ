# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите число: '))
y = int(input('Введите число: '))
z = int(input('Введите число: '))

left = not(x or y or z)
right = not x and not y and not z

if left == right:
    print('Истинно')
else:
    print('Ложно')

# Не уверен что правильно понял задачу. Решил оставить такое решение.