#Напишите программу, которая принимает на вход цифру, 
#weekday = int(input("Введите номер дня недели: "))
#print("Вы выбрали: ", weekday)

'''if weekday <= 5:
    print('да')
elif 8 > weekday > 5:
    print('нет')
else:
    print("Это не день недели")'''


#Напишите программу для. проверки истинности утверждения
#¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (расшифровка этого выражения
#not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.
"""xyz = ["x", "y", "z"]
x = []
for i in range(len(xyz)):
    x.append(int(input(f"Введите значение {xyz[i]}: ")))

left =not (x[0] or x[1] or x[2])
right = (not x[0] and not x[1] and not x[2])
if left == right:
    print('true')
else:
    print('false')"""
    
    
#Напишите программу, которая принимает на вход координаты точки 
#(X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .
'''xy = ['x', 'y']
k = []
for i in range(len(xy)):
    k.append(int(input(f'Введите координату {xy[i]} ')))

if k[0] == 0 or k[1] == 0:
    print('Некорректный ввод')
else:
    if k[0] > 0 and k[1] > 0:
        print('1')
    elif k[0] < 0 and k[1] < 0:
        print("3")
    elif k[0] > 0 and k[1] < 0:
        print('4')
    elif k[0] < 0 and k[1] > 0:
        print('2')'''
    
#Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
'''numQua = int(input('Введиет номер четверти: '))

if numQua == 1:
    print('x ∈ (0;+∞), y ∈ (0;+∞)')
elif numQua == 2:
    print('x ∈ (-∞;0), y ∈ (0;+∞)')
elif numQua == 3:
    print('x ∈ (-∞;0), y ∈ (-∞;0)')
elif numQua == 4:
    print('x ∈ (0;+∞), y ∈ (-∞;0)')
else:
    print('Некорректный ввод')'''




#Напишите программу, которая принимает на вход координаты двух точек и 
#находит расстояние между ними в 2D пространстве
'''xy = ['x1', 'y1', 'x2', 'y2']
k = []
for i in range(len(xy)):
    k.append(int(input(f'Введите координату {xy[i]} ')))

distance = ((k[2] - k[0]) ** 2 + (k[1] - k[3]) ** 2) ** (0.5)

print(distance)'''