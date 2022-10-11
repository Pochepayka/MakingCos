import math
print ("Введите X, для которого нужно расчитать значение косинуса:", end = '')
x = float(input())
x1=0
if (abs(x) > 2* math.pi):
    x1 = x
    x = abs(x) - (abs(x) // (2 * math.pi)) * 2 * math.pi
    print ("X изменён на аналогичный в промежутке [0;2pi]")
    print (x1, ' = ', x)
print ("Введите точность эпсилон:", end = '')
eps = float (input())
while (eps<=0):
    print ("Введённая эпсилон не удовлетворяет ОДЗ")
    print ("Эпсилон должна быть строго больше 0")
    print ("Попробуйте ввести точность эпсилон заново:", end = ' ')
    eps = float(input())
znak = 1
sum = 1
ch = 1
znam = 1
n = 1
slag = 2
znach = math.cos(x)
diff =abs(znach - sum)
while (abs(slag) >= eps):
    #print ('n = ', n, '; sum = ', sum, '; eps = ', eps, '; diff = ', diff)
    if (abs(slag)<diff):
        print ("ошибка на ", n)
    ch *= x * x
    znam *= 2 * n * (2 * n - 1)
    znak *= (-1)
    slag = znak * ch / znam
    sum += slag
    diff =abs(math.cos(x) - sum)
    n += 1
if (x1!=0):
    print ('cos(x) = ', 'cos(',x1,') = ', 'cos(', x, ') = ', sum, '+-', eps, ' = ', znach)
else:
    print ('cos(x) = ', 'cos(', x, ') = ', sum, '+-', eps, ' = ', znach)
print ('n = ', n, '; sum = ', sum, '; eps = ', eps, '; diff = ', diff)


