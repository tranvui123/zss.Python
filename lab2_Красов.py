import math

x = float(input("Enter x:"))
y = float(input("Enter y:"))

# координаты прямоугольника
x1 = -1
x2 = 6
y1 = -2
y2 = 1
# центр окружности и радиус
yc = 0
xc = 2
r =  3
#прямая линия y=kx+b
k = 1
b = -2
if(y<k*x+b):
    if((x-xc)**2+(y-yc)**2<r**2):
        if(x1<x<x2) and (y1<y<y2):
            print("Обл.4")
        else:
            if(y>y2):
                print("Обл.5")
            else:
                print("Обл.6")
    else:
        if (x1 < x < x2) and (y1 < y < y2):
            print("Обл.7")
        else:
            print("Обл.8")
else:
    if ((x - xc) ** 2 + (y - yc) ** 2 < r ** 2):
        if (x1 < x < x2) and (y1 < y < y2):
            print("Обл.3")
        else:
            print("Обл.2")
    else:
        print("Обл.1")
print("Конец")