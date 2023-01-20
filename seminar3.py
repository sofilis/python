#Задайте список из нескольких чисел. Напишите программу, которая 
#найдёт сумму элементов списка, стоящих на нечётной позиции.
'''s = [ int(i) for i in input().split()]
t = []
l = len(s)-1
k = 0
i = 0
if len(s)==0:
    print(str(0))
else:
    for st in s:
        if len(s)>1:
            if i==0:
                k = s[i+1] + s[-1]
                t.append(k)
            elif i>0 and i<l:
                k=s[i-1]+s[i+1]
                t.append(k)
            elif i==l:
                k = s[i-1]+s[0]
                t.append(k)
        elif len(s)==1:
            k = s[i]
            t.append(k)       
        i +=1
    j = 0
    for st2 in t:
        print(str(t[j])+' ',end='')
        j +=1'''



#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д
'''def mult_lst(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst)


lst = [2, 3, 4, 5, 6]
mult_lst(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
mult_lst(lst)'''



#Задайте список из вещественных чисел. Напишите программу, которая найдёт
#разницу между максимальным и минимальным значением дробной части элементов.
#(если получаются длинные числа после запятой, это нормально и особенность
#данного языка программирования. ваш ответ может не совпадать с примером(может получитя 0,20))
'''lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
print(max(new_lst) - min(new_lst))'''



#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
'''s = ""
n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while n != 0:
    s = str(n % 2) + s
    n //= 2
print(s)'''



#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
'''def findFib(index):
    if index == 1:
        return 0
    elif index == 2:
        return 1
    return findFib(index-1) + findFib(index-2)

n = int(input(
    "Введите число для преобразовывания десятичного числа в двоичное:\n"))
lst = [findFib(i) for i in range(1, n+2)]
print(lst)
lst = lst[::-1] + lst[1:]
print(lst, '\n')'''

