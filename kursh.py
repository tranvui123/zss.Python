import pygame
import math
import sys
from pygame import *
from math import *

pygame.init()# инициализировать все импортированные модули pygame

#шрифт для использования
font = pygame.font.SysFont('Verdana', 16)
font2 = pygame.font.SysFont('Serif', 24)
font3 = pygame.font.SysFont('Arial', 14)

# цветы исползуютя
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 200, 50)
blue = (0, 50, 200)
graphcolor = (255, 0, 0)  # цвет графики - красный
gridcolor = (100, 250, 240)  # цвет сетки

width, height = 400, 400 # длина и ширина экрана, содержащий графики
extraW = 400 # дополнительная длина экрана
screen = pygame.display.set_mode((width + extraW, height))
#Возвращает экран размеров (800,400)
pygame.display.set_caption("Чан В.В. - График")


def graphpaper(k):
    # рисовать бумагу
    for i in range(int(width / k)+1):
        gridx = k * i
        gridy = k * i
        pygame.draw.line(screen, gridcolor, (gridx, 0), (gridx, height), 1)
        """рисовать линию:
                gridcolor: цвет линии
                gridx, 0: начальная точка линии
                gridx, height: конечная точка линии
                1: ширина линии
        """
        pygame.draw.line(screen, gridcolor, (0, gridy), (width, gridy), 1)

    # рисовать оси x и y
    midx, midy = int(width / (2 * k)), int(height / (2 * k))
    pygame.draw.line(screen, black, (midx * k, 0), (midx * k, height), 2)
    pygame.draw.line(screen, black, (0, midy * k), (width, midy * k), 2)

# основная функция
def mymain(Graphs, eq):
    screen.set_clip(None)
    # пиксель на сетку
    k = 20

    if Graphs == 1:
        screen.fill(white)# очисти экран
        graphpaper(k)
        equation = []# массив, который будет содержать уравнение
        eq2 = ' '
    else:
        screen.set_clip(width, 0, width + extraW, height)
        screen.fill(white)
        screen.set_clip(None)
        eq2 = eq
        equation = []

    # инструкции и результаты

    t = font.render("Введите Функция. Пример: sin(x)", 1, black)
        #render: Отформатировать размер и цвет строки
    screen.blit(t, (width + 10, 70))
        #blit: Отображается t на экране с начальным координатами (410,70)

    t = font.render("Выберите 'Enter', когда закончите.", 1, black)
    screen.blit(t, (width + 10, 100))

    t = font.render("Выберите 'Q' для начала.", 1, black)
    screen.blit(t, (width + 10, 130))

    t = font.render("Выберите 'Backspace' для очистки.", 1, black)
    screen.blit(t, (width + 10, 160))

    t = font3.render("s=sin(), c=cos(), t=tan(), r=sqrt(), a=abs(), l=log10(), n=log(), e=e, p=pi", 1, black)
    screen.blit(t, (width + 10, 190))

    active = True

    while active:
        # обновить экран
        screen.set_clip(width+10, height - 30, width + extraW, height)
            #set_clip: Укажите рабочую область экрана
        screen.fill(white)#заполнить экран

        # массив уравнений
        eq = str().join(equation)
        eq = str.replace(eq, " ", "")

        #показать уравнение
        eqshow = font.render("Function:  y = " + eq, 1, blue)
        screen.blit(eqshow, (width + 10, height - 30))

        pygame.display.update()#Обновление частей экрана для отображения


        # действия клавиатуры и мышки
        for event in pygame.event.get():

            if event.type == pygame.QUIT: #выход
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:#ввод с клавиатуры

                # математические операции и символы для уравнения
                if event.unicode == u'*':
                    equation.append("*") #добавить * к массиву equation
                elif event.unicode == u'+':
                    equation.append("+")
                elif event.unicode == u'/':
                    equation.append("/")
                elif event.unicode == u'-':
                    equation.append("-")
                elif event.unicode == u'.':
                    equation.append(".")
                elif event.unicode == u'(':
                    equation.append("(")
                elif event.unicode == u')':
                    equation.append(")")
                elif event.unicode == u'^':
                    equation.append("**")

                # числа, введенные для уравнения, и переменная x
                elif event.key == K_1:
                    equation.append("1")
                elif event.key == K_2:
                    equation.append("2")
                elif event.key == K_3:
                    equation.append("3")
                elif event.key == K_4:
                    equation.append("4")
                elif event.key == K_5:
                    equation.append("5")
                elif event.key == K_6:
                    equation.append("6")
                elif event.key == K_7:
                    equation.append("7")
                elif event.key == K_8:
                    equation.append("8")
                elif event.key == K_9:
                    equation.append("9")
                elif event.key == K_0:
                    equation.append("0")

                # команды математической функции
                elif event.key == K_s:
                    equation.append("sin(")
                elif event.key == K_c:
                    equation.append("cos(")
                elif event.key == K_t:
                    equation.append("tan(")
                elif event.key == K_r:
                    equation.append("sqrt(")
                elif event.key == K_a:
                    equation.append("abs(")
                elif event.key == K_l:
                    equation.append("log10(")
                elif event.key == K_n:
                    equation.append("log(")
                elif event.key == K_e:
                    equation.append("e")
                elif event.key == K_p:
                    equation.append("pi")

                elif event.key == K_x:
                    equation.append("x")

                elif event.key == K_RETURN:
                    active = False
                elif event.key == K_BACKSPACE:
                    equation = []
                elif event.key == K_q:
                    mymain(1, ' ')

    screen.set_clip(None)  # Удалить указанную область c None
    # рисовать график
    for i in range(width):
        try:
            x = (width / 2 - i) / float(k)
            y = eval(eq)
            pos1 = (width / 2 + x * k, height / 2 - y * k)

            nx = (width / 2 - (i + 1)) / float(k)
            ny = eval(eq)
            pos2 = (width / 2 + nx * k, height / 2 - ny * k)
            pygame.draw.line(screen, graphcolor, pos1, pos2, 3)
        except:
            pass

    #редактировать правый экран
    screen.set_clip(width, 0, width + extraW, height - 30)
    screen.fill(white)
    # инструкции
    instruct = font.render("Выберите 'Q', чтобы продолжить.", 1, black)
    screen.blit(instruct, (width + 10, 70))

    screen.set_clip(None)
    pygame.display.update()#показать графики

    #сделать следующий?
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #выход
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_q:#Введите Q, чтобы продолжить
                    mymain(1, ' ')
                else :
                    pygame.quit()# else выход
                    sys.exit()

if __name__ == '__main__':
    mymain(1, ' ')