from matplotlib.patches import Circle, Rectangle
import matplotlib.pyplot as plt
import math
from matplotlib.lines import Line2D
import random
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkinter import messagebox
from functools import partial
import tkinter.ttk as ttk

window = tk.Tk()
window.title("Добро пожаловать в приложение ПокройКругами")
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w = w // 2  # середина экрана
h = h // 2
w = w - 400  # смещение от середины
h = h - 300
window.geometry(f'700x525+{w}+{h}')


# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=tk.BOTH)

# создаем пару фреймвов
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

frame1.pack(fill=tk.BOTH, expand=True)
frame2.pack(fill=tk.BOTH, expand=True)

# добавляем фреймы в качестве вкладок
notebook.add(frame1, text="1 радиус")
notebook.add(frame2, text="2 радиуса")

#Покрытие кругами одного радиуса
def callResult(number1, number2, radius):
    if (number1.get())=="" or (number2.get())=="" or (radius.get())=="":
        return messagebox.showerror(title="Ошибка", message="Неверный ввод значений", detail="Все поля должны быть заполнены!")
    if not (number1.get()).isnumeric() or not (number2.get()).isnumeric():
        return messagebox.showerror(title="Ошибка", message="Неверный ввод значений", detail="Все значения должны быть числом!")
    if int(number1.get())<=0 or int(number2.get())<=0 or float(radius.get())<=0:
        return messagebox.showerror(title="Ошибка", message="Неверный ввод значений", detail="Все значения должны быть больше 0!")
    c = combobox.get()

    # сетка
    plt.grid(which='major')
    ax = plt.gca()

    #задаваемые параметры
    widthA = int(number1.get())
    lengthB = int(number2.get())
    R = float(radius.get())

    # размеры осей
    if (lengthB >= widthA):
        plt.xlim(-R - 1, lengthB + 2)
        plt.ylim(-R - 1, lengthB + 2)
    else:
        plt.xlim(-R - 1, widthA + 2)
        plt.ylim(-R - 1, widthA + 2)

    # рисование прямоугольника
    rec = Rectangle((0, 0), int(lengthB), int(widthA), edgecolor='blue', facecolor='none', lw=2)
    ax.add_patch(rec)

    if c == "Квадратное":

        def countSquare():
            count = 0
            i = R * math.sqrt(2) / 2
            while widthA - i + R * math.sqrt(2) / 2 > 0:
                j = R * math.sqrt(2) / 2
                while lengthB - j + R * math.sqrt(2) - R * math.sqrt(2) / 2 > 0:
                    j += R * math.sqrt(2)
                    count += 1
                i += R * math.sqrt(2)
            return count

        plt.title('Квадратное покрытие', fontsize=16, fontname='Times New Roman')
        i = R * math.sqrt(2) / 2
        while widthA - i + R * math.sqrt(2) / 2 > 0:
            j = R * math.sqrt(2) / 2
            while lengthB - j + R * math.sqrt(2) / 2 > 0:
                circle = Circle((j, i), R, edgecolor='black', facecolor='none')
                ax.scatter(j, i, c='black', s=1)
                ax.add_patch(circle)
                j += R * math.sqrt(2)
            i += R * math.sqrt(2)
        legend_elements = [Line2D([0], [0], marker='o', color='w', label='n = {value}'.format(value=countSquare()),markerfacecolor='black', markersize=4)]
        plt.legend(title='Количество кругов:', handles=legend_elements, prop={"family": "Times New Roman", "size": 12})

        plt.savefig('output.png')

        image = Image.open("output.png")
        resize_image = image.resize((410, 410))
        img = ImageTk.PhotoImage(resize_image)
        label1 = tk.Label(image=img)
        label1.image = img
        label1.place(x=262.5, y=50)

        plt.close()
        return
    else:

        def countHexagonX():
            count = 0
            row = 1
            i = R / 2
            while widthA - i + R * math.sqrt(3) / 2 > 0:
                if row % 2 == 1:
                    j = R * math.sqrt(2) / 2
                    while lengthB - j + R * math.sqrt(3) / 2 > 0:
                        j += R * math.sqrt(3)
                        count += 1
                else:
                    j = R * math.sqrt(2) / 2 - R * math.sqrt(2) / 2
                    while lengthB - j + R * math.sqrt(3) / 2 > 0:
                        j += R * math.sqrt(3)
                        count += 1
                row += 1
                i += R * 3 / 2
            return count

        def countHexagonY():
            count = 0
            row = 1
            i = R / 2
            while lengthB - i + R * math.sqrt(3) / 2 > 0:
                if row % 2 == 1:
                    j = R * math.sqrt(2) / 2
                    while widthA - j + R * math.sqrt(3) / 2 > 0:
                        count += 1
                        j += R * math.sqrt(3)
                else:
                    j = R * math.sqrt(2) / 2 - R * math.sqrt(3) / 2
                    while widthA - j + R * math.sqrt(3) / 2 > 0:
                        count += 1
                        j += R * math.sqrt(3)
                row += 1
                i += R * 3 / 2
            return count

        def hexagonX():
            plt.title('Гексагональное покрытие', fontsize=16, fontname='Times New Roman')
            row = 1
            i = R / 2
            while widthA - i + R * math.sqrt(3) / 2 > 0:
                if row % 2 == 1:
                    j = R * math.sqrt(2) / 2
                    while lengthB - j + R * math.sqrt(3) / 2 > 0:
                        circle = Circle((j, i), R, edgecolor='black', facecolor='none')
                        ax.scatter(j, i, c='black', s=1)
                        ax.add_patch(circle)
                        j += R * math.sqrt(3)
                else:
                    j = R * math.sqrt(2) / 2 - R * math.sqrt(3) / 2
                    while lengthB - j + R * math.sqrt(3) / 2 > 0:
                        circle = Circle((j, i), R, edgecolor='black', facecolor='none')
                        ax.scatter(j, i, c='black', s=1)
                        ax.add_patch(circle)
                        j += R * math.sqrt(3)
                row += 1
                i += R * 3 / 2
            legend_elements = [Line2D([0], [0], marker='o', color='w', label='n = {value}'.format(value=countHexagonX()), markerfacecolor='black', markersize=4)]
            plt.legend(title='Количество кругов:', handles=legend_elements,prop={"family": "Times New Roman", "size": 12})

        def hexagonY():
            plt.title('Гексагональное покрытие', fontsize=16, fontname='Times New Roman')
            row = 1
            i = R / 2
            while lengthB - i + R * math.sqrt(3) / 2 > 0:
                if row % 2 == 1:
                    j = R * math.sqrt(2) / 2
                    while widthA - j + R * math.sqrt(3) / 2 > 0:
                        circle = Circle((i, j), R, edgecolor='black', facecolor='none')
                        ax.scatter(i, j, c='black', s=1)
                        ax.add_patch(circle)
                        j += R * math.sqrt(3)
                else:
                    j = R * math.sqrt(2) / 2 - R * math.sqrt(3) / 2
                    while widthA - j + R * math.sqrt(3) / 2 > 0:
                        circle = Circle((i, j), R, edgecolor='black', facecolor='none')
                        ax.scatter(i, j, c='black', s=1)
                        ax.add_patch(circle)
                        j += R * math.sqrt(3)
                row += 1
                i += R * 3 / 2
            legend_elements = [Line2D([0], [0], marker='o', color='w', label='n = {value}'.format(value=countHexagonY()), markerfacecolor='black', markersize=4)]
            plt.legend(title='Количество кругов:', handles=legend_elements, prop={"family": "Times New Roman", "size": 12})

        if countHexagonX() > countHexagonY():
            hexagonY()
            print('Количество кругов при X:', countHexagonX(), 'и при Y:', countHexagonY())
        else:
            hexagonX()
            print('Количество кругов при X:', countHexagonX(), 'и при Y:', countHexagonY())

        plt.savefig('output.png')

        image = Image.open("output.png")
        resize_image = image.resize((410, 410))
        img = ImageTk.PhotoImage(resize_image)
        label1 = tk.Label(image=img)
        label1.image = img
        label1.place(x=262.5, y=50)

        plt.close()
        return

#Покрытие кругами двух радиусов
def call_covering(number1, number2, radius, radius2):
    if (number1.get())=="" or (number2.get())=="" or (radius.get())=="" or (radius2.get())=="":
        return messagebox.showerror(title="Ошибка", message="Неверный ввод значений", detail="Все поля должны быть заполнены!")
    if not (number1.get()).isnumeric() or not (number2.get()).isnumeric():
        return messagebox.showerror(title="Ошибка", message="Неверный ввод значений", detail="Все значения должны быть числом!")
    if int(number1.get())<=0 or int(number2.get())<=0 or float(radius.get())<=0 or float(radius2.get())<=0:
        return messagebox.showerror(title="Ошибка", message="Неверный ввод значений", detail="Все значения должны быть больше 0!")
    c = combobox.get()

    plt.grid(which='major')
    ax = plt.gca()

    widthA = int(number1.get())
    lengthB = int(number2.get())
    R = float(radius.get())
    r = float(radius2.get())

    # размеры осей
    if (lengthB >= widthA):
        plt.xlim(-R - 1, lengthB + 2)
        plt.ylim(-R - 1, lengthB + 2)
    else:
        plt.xlim(-R - 1, widthA + 2)
        plt.ylim(-R - 1, widthA + 2)

    rec = Rectangle((0, 0), int(lengthB), int(widthA), edgecolor='blue', facecolor='none', lw=2)
    ax.add_patch(rec)

    if c == "Квадратное":

        def countSquareTwo():
            count = 0
            i = R * math.sqrt(2) / 2 - 3 * r / 4

            if R * math.sqrt(2) + 3 * r / 4 < R:
                while widthA - i + R > 0:
                    if (i > widthA) and (i - (R * math.sqrt(2) + 3 * r / 4) + R - 3 * r / 4 > widthA):
                        return
                    j = R * math.sqrt(2) / 2 - 3 * r / 4
                    while lengthB - j + R > 0:
                        if (j > lengthB) and (j - (R * math.sqrt(2) + 3 * r / 4) + R > lengthB):
                            break
                        count += 1
                        if j - (R * math.sqrt(2) + 3 * r / 4) / 2 + 3 * r / 4 > 0 and (((j > lengthB) and (j - (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < lengthB) or ((j < lengthB) and (j - (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < lengthB)) and (((i > widthA) and (i + (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < widthA) or ((i < widthA) and (i + (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < widthA)):
                            count += 1
                        j += R * math.sqrt(2) + 3 * r / 4
                    if (j > lengthB) and (j - (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < lengthB and (((i > widthA) and (i + (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < widthA) or ((i < widthA) and (i + (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < widthA)):
                        count += 1
                    i += R * math.sqrt(2) + 3 * r / 4
                    if (i > widthA) and (i - (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < widthA and (((j > lengthB) and (j + (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < lengthB) or ((j < lengthB) and (j + (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < lengthB)):
                        count += 1
            else:
                while widthA - i + R > 0:
                    if (i > widthA) and (i - (R * math.sqrt(2) + r / 2) + R - r / 2 > widthA):
                        return
                    j = R * math.sqrt(2) / 2 - r / 2
                    while lengthB - j + R > 0:
                        if (j > lengthB) and (j - (R * math.sqrt(2) + r / 2) + R > lengthB):
                            break
                        count += 1
                        if j - (R * math.sqrt(2) + r / 2) / 2 + r / 2 > 0 and (((j > lengthB) and (j - (R * math.sqrt(2) + r / 2) / 2 - r / 2) < lengthB) or ((j < lengthB) and (j - (R * math.sqrt(2) + r / 2) / 2 - r / 2) < lengthB)) and (((i > widthA) and (i + (R * math.sqrt(2) + r / 2) / 2 - r / 2) < widthA) or ((i < widthA) and (i + (R * math.sqrt(2) + r / 2) / 2 - r / 2) < widthA)):
                            count += 1
                        j += R * math.sqrt(2) + r / 2
                    if (j > lengthB) and (j - (R * math.sqrt(2) + r / 2) / 2 - r / 2) < lengthB and (((i > widthA) and (i + (R * math.sqrt(2) + r / 2) / 2 - r / 2) < widthA) or ((i < widthA) and (i + (R * math.sqrt(2) + r / 2) / 2 - r / 2) < widthA)):
                        count += 1
                    i += R * math.sqrt(2) + r / 2
                    if (i > widthA) and (i - (R * math.sqrt(2) + r / 2) / 2 - r / 2) < widthA and (((j > lengthB) and (j + (R * math.sqrt(2) + r / 2) / 2 - r / 2) < lengthB) or ((j < lengthB) and (j + (R * math.sqrt(2) + r / 2) / 2 - r / 2) < lengthB)):
                        count += 1
            return count

        i = R * math.sqrt(2) / 2 - 3 * r / 4

        if R * math.sqrt(2) + 3 * r / 4 < R:
            while widthA - i + R > 0:
                if (i > widthA) and (i - (R * math.sqrt(2) + 3 * r / 4) + R - 3 * r / 4 > widthA):
                    return
                j = R * math.sqrt(2) / 2 - 3 * r / 4
                while lengthB - j + R > 0:
                    if (j > lengthB) and (j - (R * math.sqrt(2) + 3 * r / 4) + R > lengthB):
                        break
                    circle = Circle((j, i), R, edgecolor='black', facecolor='none')
                    ax.scatter(j, i, c='black', s=1)
                    ax.add_patch(circle)
                    if j - (R * math.sqrt(2) + 3 * r / 4) / 2 + 3 * r / 4 > 0 and (((j > lengthB) and (j - (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < lengthB) or ((j < lengthB) and (j - (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < lengthB)) and (((i > widthA) and (i + (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < widthA) or ((i < widthA) and (i + (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < widthA)):
                        circleMin = Circle((j - (R * math.sqrt(2) + 3 * r / 4) / 2, i + (R * math.sqrt(2) + 3 * r / 4) / 2), r,edgecolor='black', facecolor='none')
                        ax.add_patch(circleMin)
                    j += R * math.sqrt(2) + 3 * r / 4
                if (j > lengthB) and (j - (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < lengthB and (((i > widthA) and (i + (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < widthA) or ((i < widthA) and (i + (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < widthA)):
                    circleMin = Circle((j - (R * math.sqrt(2) + 3 * r / 4) / 2, i + (R * math.sqrt(2) + 3 * r / 4) / 2), r,edgecolor='black', facecolor='none')
                    ax.add_patch(circleMin)
                i += R * math.sqrt(2) + 3 * r / 4
                if (i > widthA) and (i - (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < widthA and (((j > lengthB) and (j + (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < lengthB) or ((j < lengthB) and (j + (R * math.sqrt(2) + 3 * r / 4) / 2 - 3 * r / 4) < lengthB)):
                    circleMin = Circle((j - (R * math.sqrt(2) + 3 * r / 4) / 2, i + (R * math.sqrt(2) + 3 * r / 4) / 2), r,edgecolor='black', facecolor='none')
                    ax.add_patch(circleMin)
        else:
            while widthA - i + R > 0:
                if (i > widthA) and (i - (R * math.sqrt(2) + r / 2) + R - r / 2 > widthA):
                    return
                j = R * math.sqrt(2) / 2 - r / 2
                while lengthB - j + R > 0:
                    if (j > lengthB) and (j - (R * math.sqrt(2) + r / 2) + R > lengthB):
                        break
                    circle = Circle((j, i), R, edgecolor='black', facecolor='none')
                    ax.scatter(j, i, c='black', s=1)
                    ax.add_patch(circle)
                    if j - (R * math.sqrt(2) + r / 2) / 2 + r / 2 > 0 and (((j > lengthB) and (j - (R * math.sqrt(2) + r / 2) / 2 - r / 2) < lengthB) or ((j < lengthB) and (j - (R * math.sqrt(2) + r / 2) / 2 - r / 2) < lengthB)) and (((i > widthA) and (i + (R * math.sqrt(2) + r / 2) / 2 - r / 2) < widthA) or ((i < widthA) and (i + (R * math.sqrt(2) + r / 2) / 2 - r / 2) < widthA)):
                        circleMin = Circle((j - (R * math.sqrt(2) + r / 2) / 2, i + (R * math.sqrt(2) + r / 2) / 2),r, edgecolor='black', facecolor='none')
                        ax.add_patch(circleMin)
                    j += R * math.sqrt(2) + r / 2
                if (j > lengthB) and (j - (R * math.sqrt(2) + r / 2) / 2 - r / 2) < lengthB and (((i > widthA) and (i + (R * math.sqrt(2) + r / 2) / 2 - r / 2) < widthA) or ((i < widthA) and (i + (R * math.sqrt(2) + r / 2) / 2 - r / 2) < widthA)):
                    circleMin = Circle((j - (R * math.sqrt(2) + r / 2) / 2, i + (R * math.sqrt(2) + r / 2) / 2), r,edgecolor='black', facecolor='none')
                    ax.add_patch(circleMin)
                i += R * math.sqrt(2) + r / 2
                if (i > widthA) and (i - (R * math.sqrt(2) + r / 2) / 2 - r / 2) < widthA and (((j > lengthB) and (j + (R * math.sqrt(2) + r / 2) / 2 - r / 2) < lengthB) or ((j < lengthB) and (j + (R * math.sqrt(2) + r / 2) / 2 - r / 2) < lengthB)):
                    circleMin = Circle((j - (R * math.sqrt(2) + r / 2) / 2, i + (R * math.sqrt(2) + r / 2) / 2), r,edgecolor='black', facecolor='none')
                    ax.add_patch(circleMin)

        legend_elements = [Line2D([0], [0], marker='o', color='w', label='n = {value}'.format(value=countSquareTwo()),markerfacecolor='black', markersize=4)]
        plt.legend(title='Количество кругов:', handles=legend_elements,prop={"family": "Times New Roman", "size": 12})

        plt.savefig('output.png')

        image = Image.open("output.png")
        resize_image = image.resize((410, 410))
        img = ImageTk.PhotoImage(resize_image)
        label1 = tk.Label(image=img)
        label1.image = img
        label1.place(x=262.5, y=50)

        plt.close()
    else:

        def countHexagonXTwo():
            count = 0
            if r >= R / math.sqrt(3):
                row = 1
                i = R / 2 - R / math.sqrt(3)
                while widthA - i + R * math.sqrt(3) / 2 > 0:
                    if row % 2 == 1:
                        j = R * math.sqrt(2) / 2 - R / math.sqrt(3) / 2
                        while lengthB - j + R * math.sqrt(3) / 2 > 0:
                            count += 1
                            if (((j > lengthB) and (j + R - R / math.sqrt(3) / 2) < lengthB) or ((j < lengthB) and (j + R - R / math.sqrt(3)) < lengthB)) and ((((i > widthA) and (i + R - R / math.sqrt(3) / 2)) < widthA) or ((i < widthA) and (i + R - R / math.sqrt(3) / 2 < widthA))):
                                count += 1
                            if (j - R / math.sqrt(3) / 2 < lengthB) and (i + R < widthA):
                                count += 1
                            j += 2 * R
                    else:
                        j = R * math.sqrt(2) / 2 - 2 * R / 2 - R / math.sqrt(3) / 2
                        while lengthB - j + R * math.sqrt(3) / 2 > 0:
                            count += 1
                            if (j - R > 0) and (((j > lengthB) and (j - R / math.sqrt(3)) < lengthB) or ((j < lengthB) and (j - R / math.sqrt(3) / 2) < lengthB)) and (((i > widthA) and (i + R - R / math.sqrt(3) / 2) < widthA) or ((i < widthA) and (i + R < widthA))):
                                count += 1
                            if (j + R - R / math.sqrt(3) / 2 < lengthB) and (i < widthA):
                                count += 1
                            j += 2 * R
                    row += 1
                    i += R * math.sqrt(3)
                return count
            else:
                row = 1
                i = R / 2 - 5 * r / 8
                while widthA - i + R > 0:
                    if row % 2 == 1:
                        j = R * math.sqrt(2) / 2 - r / 2
                        while lengthB - j + R > 0:
                            count += 1
                            if (((j > lengthB) and (j + (R * math.sqrt(3) + r / 2) / 2 - 3 * r / 4) < lengthB) or ((j < lengthB) and (j + (R * math.sqrt(3) + r / 2) / 2 - 3 * r / 4) < lengthB)) and (((i > widthA) and (i + R - 3 * r / 4 < widthA)) or ((i < widthA) and (i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 - r) < widthA)):
                                count += 1
                            if (((j > lengthB) and (j - 3 * r / 4 < lengthB)) or ((j < lengthB) and (j - 3 * r / 4 < lengthB))) and (i + R < widthA):
                                count += 1
                            j += R * math.sqrt(3) + r / 2
                    else:
                        j = R * math.sqrt(2) / 2 - r / 2 - (R * math.sqrt(3) + r / 2) / 2
                        while lengthB - j + R > 0:
                            count += 1
                            if (j - R > 0) and (((j > lengthB) and (j - 3 * r / 4) < lengthB) or ((j < lengthB) and (j - r / 2) < lengthB)) and (((i > widthA) and (i + R - r / 2) < widthA) or ((i < widthA) and (i + R < widthA))):
                                count += 1
                            if (((j > lengthB) and (j + (R * math.sqrt(3) + r / 2) / 2 - 3 * r / 4 < lengthB)) or ((j < lengthB) and (j + (R * math.sqrt(3) + r / 2) / 2 - 3 * r / 4 < lengthB))) and (((i < widthA) and (i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 - 3 * r / 4 < widthA)) or ((i > widthA) and (i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 - 3 * r / 4) < widthA)):
                                count += 1
                            j += R * math.sqrt(3) + r / 2
                    row += 1
                    i += (R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2
                return count

        def countHexagonYTwo():
            count = 0
            if r >= R / math.sqrt(3):
                row = 1
                i = R / 2 - R / math.sqrt(3)
                while lengthB - i + R * math.sqrt(3) / 2 > 0:
                    if row % 2 == 1:
                        j = R * math.sqrt(2) / 2 - R / math.sqrt(3) / 2
                        while widthA - j + R * math.sqrt(3) / 2 > 0:
                            count += 1
                            if (((j > widthA) and (j + R - R / math.sqrt(3) / 2) < widthA) or ((j < widthA) and (j + R - R / math.sqrt(3)) < widthA)) and ((((i > lengthB) and (i + R * math.sqrt(3) / 2 - R / math.sqrt(3) / 2)) < lengthB) or ((i < lengthB) and (i + R * math.sqrt(3) / 2 - R / math.sqrt(3) / 2 < lengthB))):
                                count += 1
                            if (((j > widthA) and (j - R / math.sqrt(3) / 2 < widthA)) or ((j < widthA) and (j - R / math.sqrt(3) / 2 < widthA))) and (i + R < lengthB):
                                count += 1
                            j += 2 * R
                    else:
                        j = R * math.sqrt(2) / 2 - 2 * R / 2 - R / math.sqrt(3) / 2
                        while widthA - j + R * math.sqrt(3) / 2 > 0:
                            count += 1
                            if (j - R > 0) and (((j > widthA) and (j - R - R / math.sqrt(3) / 2) < widthA) or ((j < widthA) and (j - R / math.sqrt(3) / 2) < widthA)) and (((i > lengthB) and (i + R - R / math.sqrt(3) / 2) < lengthB) or ((i < lengthB) and (i + R < lengthB))):
                                count += 1
                            if (((i < lengthB) and (i + R - R * math.sqrt(3) / 2 < lengthB)) or (i > lengthB) and (i + R - R * math.sqrt(3) / 2 < lengthB)) and (j + R - R / math.sqrt(3) / 2 < widthA):
                                count += 1
                            j += 2 * R
                    row += 1
                    i += R * math.sqrt(3)
                return count
            else:
                row = 1
                i = R / 2 - 3 * r / 4
                while lengthB - i + R > 0:
                    if row % 2 == 1:
                        j = R * math.sqrt(2) / 2 - r / 2
                        while widthA - j + R > 0:
                            count += 1
                            if (((j > widthA) and (j + R - 3 * r / 4) < widthA) or ((j < widthA) and (j + (R * math.sqrt(3) + r / 2) / 2 - 3 * r / 4) < widthA)) and (((i > lengthB) and (i + R - r / 2) < lengthB) or ((i < lengthB) and (i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 - 3 * r / 4 < lengthB))):
                                count += 1
                            if (((j > widthA) and (j - r / 2 < widthA)) or ((j < widthA) and (j - r / 2 < widthA))) and (i + R < lengthB):
                                count += 1
                            j += R * math.sqrt(3) + r / 2
                    else:
                        j = R * math.sqrt(2) / 2 - r / 2 - (R * math.sqrt(3) + r / 2) / 2
                        while widthA - j + R > 0:
                            count += 1
                            if (j - R > 0) and (((j > widthA) and (j - 3 * r / 4) < widthA) or ((j < widthA) and (j - r / 2 / 2) < widthA)) and (((i > lengthB) and (i + R - r / 2 / 2) < lengthB) or ((i < lengthB) and (i + R < lengthB))):
                                count += 1
                            if (((i < lengthB) and (i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 - r < lengthB)) or (i > lengthB) and (i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 - 3 * r / 4 < lengthB)) and (j + (R * math.sqrt(3) + r / 2) / 2 - r / 2 < widthA):
                                count += 1
                            j += R * math.sqrt(3) + r / 2
                    row += 1
                    i += (R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2
                return count

        def hexagonXTwo():
            plt.title('Гексагональное покрытие', fontsize=16, fontname='Times New Roman')
            if r >= R / math.sqrt(3):
                row = 1
                i = R / 2 - R / math.sqrt(3)
                while widthA - i + R * math.sqrt(3) - R * math.sqrt(3) / 2 > 0:
                    if row % 2 == 1:
                        j = R * math.sqrt(2) / 2 - R / math.sqrt(3) / 2
                        while lengthB - j + R * math.sqrt(3) - R * math.sqrt(3) / 2 > 0:
                            circle = Circle((j, i), R, edgecolor='black', facecolor='none')
                            ax.scatter(j, i, c='black', s=1)
                            ax.add_patch(circle)
                            if (((j > lengthB) and (j + R - R / math.sqrt(3) / 2) < lengthB) or ((j < lengthB) and (j + R - R / math.sqrt(3)) < lengthB)) and ((((i > widthA) and (i + R - R / math.sqrt(3) / 2)) < widthA) or ((i < widthA) and (i + R - R / math.sqrt(3) / 2 < widthA))):
                                circleMinCenter = Circle((j + R, i + (R / math.sqrt(3))), r, edgecolor='black', facecolor='none')
                                ax.add_patch(circleMinCenter)
                            if (j - R / math.sqrt(3) / 2 < lengthB) and (i + R < widthA):
                                circleMinUp = Circle((j, i + R + (R / math.sqrt(3)) / 2), r, edgecolor='black', facecolor='none')
                                ax.add_patch(circleMinUp)
                            j += 2 * R
                    else:
                        j = R * math.sqrt(2) / 2 - 2 * R / 2 - R / math.sqrt(3) / 2
                        while lengthB - j + R * math.sqrt(3) - R * math.sqrt(3) / 2 > 0:
                            circle = Circle((j, i), R, edgecolor='black', facecolor='none')
                            ax.scatter(j, i, c='black', s=1)
                            ax.add_patch(circle)
                            if (j - R > 0) and (((j > lengthB) and (j - R / math.sqrt(3)) < lengthB) or ((j < lengthB) and (j - R / math.sqrt(3) / 2) < lengthB)) and (((i > widthA) and (i + R - R / math.sqrt(3) / 2) < widthA) or ((i < widthA) and (i + R < widthA))):
                                circleMinUp = Circle((j, i + R + (R / math.sqrt(3)) / 2), r, edgecolor='black',facecolor='none')
                                ax.add_patch(circleMinUp)
                            if (j + R - R / math.sqrt(3) / 2 < lengthB) and (i < widthA):
                                circleMinCenter = Circle((j + R, i + (R / math.sqrt(3))), r, edgecolor='black',facecolor='none')
                                ax.add_patch(circleMinCenter)
                            j += 2 * R
                    row += 1
                    i += R * math.sqrt(3)
                legend_elements = [Line2D([0], [0], marker='o', color='w', label='n = {value}'.format(value=countHexagonXTwo()), markerfacecolor='black', markersize=4)]
                plt.legend(title='Количество кругов:', handles=legend_elements, prop={"family": "Times New Roman", "size": 12})

            else:
                row = 1
                i = R / 2 - 5 * r / 8
                while widthA - i + R > 0:
                    if row % 2 == 1:
                        j = R * math.sqrt(2) / 2 - r / 2
                        while lengthB - j + R > 0:
                            circle = Circle((j, i), R, edgecolor='black', facecolor='none')
                            ax.scatter(j, i, c='black', s=1)
                            ax.add_patch(circle)
                            if (((j > lengthB) and (j + (R * math.sqrt(3) + r / 2) / 2 - 3 * r / 4) < lengthB) or ((j < lengthB) and (j + (R * math.sqrt(3) + r / 2) / 2 - 3 * r / 4) < lengthB)) and (((i > widthA) and (i + R - 3 * r / 4 < widthA)) or ((i < widthA) and (i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 - r) < widthA)):
                                circleMinCenter = Circle((j + (R * math.sqrt(3) + r / 2) / 2, i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 - 3 * r / 4), r,edgecolor='black', facecolor='none')
                                ax.add_patch(circleMinCenter)
                            if (((j > lengthB) and (j - 3 * r / 4 < lengthB)) or ((j < lengthB) and (j - 3 * r / 4 < lengthB))) and (i + R < widthA):
                                circleMinUp = Circle((j, i + R + r / 2), r, edgecolor='black', facecolor='none')
                                ax.add_patch(circleMinUp)
                            j += R * math.sqrt(3) + r / 2
                    else:
                        j = R * math.sqrt(2) / 2 - r / 2 - (R * math.sqrt(3) + r / 2) / 2
                        while lengthB - j + R > 0:
                            circle = Circle((j, i), R, edgecolor='black', facecolor='none')
                            ax.scatter(j, i, c='black', s=1)
                            ax.add_patch(circle)
                            if (j - R > 0) and (((j > lengthB) and (j - 3 * r / 4) < lengthB) or ((j < lengthB) and (j - r / 2) < lengthB)) and (((i > widthA) and (i + R - r / 2) < widthA) or ((i < widthA) and (i + R < widthA))):
                                circleMinUp = Circle((j, i + R + r / 2), r, edgecolor='black', facecolor='none')
                                ax.add_patch(circleMinUp)
                            if (((j > lengthB) and (j + (R * math.sqrt(3) + r / 2) / 2 - 3 * r / 4 < lengthB)) or ((j < lengthB) and (j + (R * math.sqrt(3) + r / 2) / 2 - 3 * r / 4 < lengthB))) and (((i < widthA) and (i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 - 3 * r / 4 < widthA)) or ((i > widthA) and (i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 - 3 * r / 4) < widthA)):
                                circleMinCenter = Circle((j + (R * math.sqrt(3) + r / 2) / 2, i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 - 3 * r / 4), r, edgecolor='black', facecolor='none')
                                ax.add_patch(circleMinCenter)
                            j += R * math.sqrt(3) + r / 2
                    row += 1
                    i += (R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2
                legend_elements = [Line2D([0], [0], marker='o', color='w', label='n = {value}'.format(value=countHexagonXTwo()), markerfacecolor='black', markersize=4)]
                plt.legend(title='Количество кругов:', handles=legend_elements,prop={"family": "Times New Roman", "size": 12})

        def hexagonYTwo():
            plt.title('Гексагональное покрытие', fontsize=16, fontname='Times New Roman')
            if r >= R / math.sqrt(3):
                row = 1
                i = R / 2 - R / math.sqrt(3)
                while lengthB - i + R * math.sqrt(3) - R * math.sqrt(3) / 2 > 0:
                    if row % 2 == 1:
                        j = R * math.sqrt(2) / 2 - R / math.sqrt(3) / 2
                        while widthA - j + R * math.sqrt(3) - R * math.sqrt(3) / 2 > 0:
                            circle = Circle((i, j), R, edgecolor='black', facecolor='none')
                            ax.scatter(i, j, c='black', s=1)
                            ax.add_patch(circle)
                            if (((j > widthA) and (j + R - R / math.sqrt(3) / 2) < widthA) or ((j < widthA) and (j + R - R / math.sqrt(3)) < widthA)) and ((((i > lengthB) and (i + R * math.sqrt(3) / 2 - R / math.sqrt(3) / 2)) < lengthB) or ((i < lengthB) and (i + R * math.sqrt(3) / 2 - R / math.sqrt(3) / 2 < lengthB))):
                                circleMinCenter = Circle((i + (R / math.sqrt(3)), j + R), r, edgecolor='black',facecolor='none')
                                ax.add_patch(circleMinCenter)
                            if (((j > widthA) and (j - R / math.sqrt(3) / 2 < widthA)) or ((j < widthA) and (j - R / math.sqrt(3) / 2 < widthA))) and (i + R < lengthB):
                                circleMinUp = Circle((i + R + (R / math.sqrt(3)) / 2, j), r, edgecolor='black',facecolor='none')
                                ax.add_patch(circleMinUp)
                            j += 2 * R
                    else:
                        j = R * math.sqrt(2) / 2 - 2 * R / 2 - R / math.sqrt(3) / 2
                        while widthA - j + R * math.sqrt(3) - R * math.sqrt(3) / 2 > 0:
                            circle = Circle((i, j), R, edgecolor='black', facecolor='none')
                            ax.scatter(i, j, c='black', s=1)
                            ax.add_patch(circle)
                            if (j - R > 0) and (((j > widthA) and (j - R - R / math.sqrt(3) / 2) < widthA) or ((j < widthA) and (j - R / math.sqrt(3) / 2) < widthA)) and (((i > lengthB) and (i + R - R / math.sqrt(3) / 2) < lengthB) or ((i < lengthB) and (i + R < lengthB))):
                                circleMinUp = Circle((i + R + (R / math.sqrt(3)) / 2, j), r, edgecolor='black',facecolor='none')
                                ax.add_patch(circleMinUp)
                            if (((i < lengthB) and (i + R - R * math.sqrt(3) / 2 < lengthB)) or (i > lengthB) and (i + R - R * math.sqrt(3) / 2 < lengthB)) and (j + R - R / math.sqrt(3) / 2 < widthA):
                                circleMinCenter = Circle((i + (R / math.sqrt(3)), j + R), r, edgecolor='black',facecolor='none')
                                ax.add_patch(circleMinCenter)
                            j += 2 * R
                    row += 1
                    i += R * math.sqrt(3)
                legend_elements = [Line2D([0], [0], marker='o', color='w', label='n = {value}'.format(value=countHexagonYTwo()),markerfacecolor='black', markersize=4)]
                plt.legend(title='Количество кругов:', handles=legend_elements,prop={"family": "Times New Roman", "size": 12})
            else:
                row = 1
                i = R / 2 - 3 * r / 4
                while lengthB - i + R > 0:
                    if row % 2 == 1:
                        j = R * math.sqrt(2) / 2 - r / 2
                        while widthA - j + R > 0:
                            circle = Circle((i, j), R, edgecolor='black', facecolor='none')
                            ax.scatter(i, j, c='black', s=1)
                            ax.add_patch(circle)
                            if (((j > widthA) and (j + R - 3 * r / 4) < widthA) or ((j < widthA) and (j + (R * math.sqrt(3) + r / 2) / 2 - 3 * r / 4) < widthA)) and (((i > lengthB) and (i + R - r / 2) < lengthB) or ((i < lengthB) and (i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 - 3 * r / 4 < lengthB))):
                                circleMinCenter = Circle((i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 - 3 * r / 4, j + R), r,edgecolor='black', facecolor='none')
                                ax.add_patch(circleMinCenter)
                            if (((j > widthA) and (j - r / 2 < widthA)) or ((j < widthA) and (j - r / 2 < widthA))) and (i + R < lengthB):
                                circleMinUp = Circle((i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 + 3 * r / 4, j), r,edgecolor='black', facecolor='none')
                                ax.add_patch(circleMinUp)
                            j += R * math.sqrt(3) + r / 2
                    else:
                        j = R * math.sqrt(2) / 2 - r / 2 - (R * math.sqrt(3) + r / 2) / 2
                        while widthA - j + R > 0:
                            circle = Circle((i, j), R, edgecolor='black', facecolor='none')
                            ax.scatter(i, j, c='black', s=1)
                            ax.add_patch(circle)
                            if (j - R > 0) and (((j > widthA) and (j - 3 * r / 4) < widthA) or ((j < widthA) and (j - r / 2 / 2) < widthA)) and (((i > lengthB) and (i + R - r / 2 / 2) < lengthB) or ((i < lengthB) and (i + R < lengthB))):
                                circleMinUp = Circle((i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 + 3 * r / 4, j), r,edgecolor='black', facecolor='none')
                                ax.add_patch(circleMinUp)
                            if (((i < lengthB) and (i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 - r < lengthB)) or (i > lengthB) and (i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 - 3 * r / 4 < lengthB)) and (j + (R * math.sqrt(3) + r / 2) / 2 - r / 2 < widthA):
                                circleMinCenter = Circle((i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 - 3 * r / 4, j + R), r,edgecolor='black', facecolor='none')
                                ax.add_patch(circleMinCenter)
                            j += R * math.sqrt(3) + r / 2
                    row += 1
                    i += (R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2
                    legend_elements = [Line2D([0], [0], marker='o', color='w', label='n = {value}'.format(value=countHexagonYTwo()),markerfacecolor='black', markersize=4)]
                    plt.legend(title='Количество кругов:', handles=legend_elements,prop={"family": "Times New Roman", "size": 12})

        if countHexagonXTwo() > countHexagonYTwo():
            hexagonYTwo()
            print('Количество кругов для двух радиусов при X:', countHexagonXTwo(), 'и при Y:', countHexagonYTwo())
        else:
            hexagonXTwo()
            print('Количество кругов для двух радиусов при X:', countHexagonXTwo(), 'и при Y:', countHexagonYTwo())

        plt.savefig('output.png')

        image = Image.open("output.png")
        resize_image = image.resize((410, 410))
        img = ImageTk.PhotoImage(resize_image)
        label1 = tk.Label(image=img)
        label1.image = img
        label1.place(x=262.5, y=50)

        plt.close()
        return

wA = tk.StringVar()
lB = tk.StringVar()
R = tk.StringVar()

group_1 = tk.LabelFrame(frame1, padx=20, pady=10, text="Прямоугольная область:")
group_1.pack(padx=10, pady=10, anchor="nw")
tk.Label(group_1, text="Ширина:").grid(row=0)
tk.Label(group_1, text="Длина:").grid(row=1)
widthAEntry = tk.Entry(group_1, textvariable=wA)
widthAEntry.grid(row=0, column=1, sticky=tk.W)
lengthBEntry = tk.Entry(group_1, textvariable=lB)
lengthBEntry.grid(row=1, column=1, sticky=tk.W)

group_2 = tk.LabelFrame(frame1, padx=24, pady=10, text="Круги:")
group_2.pack(padx=10, pady=10, anchor="nw")
tk.Label(group_2, text="Радиус:").grid(row=0)
REntry = tk.Entry(group_2, textvariable=R)
REntry.grid(row=0, column=1, sticky=tk.W)

group_3 = tk.LabelFrame(frame1, padx=28, pady=15, text="Вид покрытия:")
group_3.pack(padx=10, pady=12, anchor="nw")
combo = tk.StringVar()
combo.set("Квадратное")
combobox = Combobox(group_3, textvariable=combo, values=["Квадратное", "Гексагональное"], state="readonly")
combobox.bind("<<ComboboxSelected>>", lambda e: REntry.focus())
combobox.pack(padx=10, pady=0, anchor="nw")

group_4 = tk.LabelFrame(window, padx=187, pady=200, text="Покрытие области:")
group_4.place(x=250, y=32)
tk.Label(group_4, text="Покрытие").grid(row=0)

call_result = partial(callResult, wA, lB, R)

btn_submit = tk.Button(frame1, text="Построить", command=call_result)
btn_submit.place(x=618, y=450)

wA2 = tk.StringVar()
lB2 = tk.StringVar()
R2 = tk.StringVar()
r2 = tk.StringVar()

group_5 = tk.LabelFrame(frame2, padx=20, pady=10, text="Прямоугольная область:")
group_5.pack(padx=10, pady=10, anchor="nw")
tk.Label(group_5, text="Ширина:").grid(row=0)
tk.Label(group_5, text="Длина:").grid(row=1)
widthAEntry2 = tk.Entry(group_5, textvariable=wA2)
widthAEntry2.grid(row=0, column=1, sticky=tk.W)
lengthBEntry2 = tk.Entry(group_5, textvariable=lB2)
lengthBEntry2.grid(row=1, column=1, sticky=tk.W)

group_6 = tk.LabelFrame(frame2, padx=20, pady=10, text="Круги:")
group_6.pack(padx=10, pady=10, anchor="nw")
tk.Label(group_6, text="Радиус 1:").grid(row=0)
tk.Label(group_6, text="Радиус 2:").grid(row=1)
REntry2 = tk.Entry(group_6, textvariable=R2)
REntry2.grid(row=0, column=1, sticky=tk.W)
rEntry2 = tk.Entry(group_6, textvariable=r2)
rEntry2.grid(row=1, column=1, sticky=tk.W)

group_7 = tk.LabelFrame(frame2, padx=28, pady=15, text="Вид покрытия:")
group_7.pack(padx=10, pady=12, anchor="nw")
combo2 = tk.StringVar()
combo2.set("Квадратное")
combobox2 = Combobox(group_7, textvariable=combo, values=["Квадратное", "Гексагональное"], state="readonly")
combobox2.bind("<<ComboboxSelected>>",lambda e: REntry2.focus())
combobox2.pack(padx=10, pady=0, anchor="nw")

call_covering = partial(call_covering, wA2, lB2, R2, r2)

btn = tk.Button(frame2, text="Построить", command=call_covering)
btn.place(x=618, y=450)

window.mainloop()

# #задаваемые параметры
# widthA = random.randint(5, 15)
# lengthB = random.randint(5, 15)
# R = random.uniform(0.75, 3)
# r = random.uniform(0.2, 1.5)
#
# # widthA = 6
# # lengthB = 7
# # R = 1
# # r = 0.45
#
#
# if (lengthB>=widthA):
#     #размеры осей
#     plt.xlim(-R-2, lengthB+4)
#     plt.ylim(-R-2, lengthB+4)
# else:
#     plt.xlim(-R-2, widthA+4)
#     plt.ylim(-R-2, widthA+4)
#
# #сетка
# plt.grid(which='major')
# ax = plt.gca()
#
# #рисование прямоугольника
# rec = Rectangle((0, 0), lengthB, widthA, edgecolor='blue', facecolor='none', lw=2)
# ax.add_patch(rec)
#
# check = input("Введите какой вид покрытия вы хотите использовать: квадратное(1) или гексагональное(2): ")
#
# def countSquare():
#     count = 0
#     i = R*math.sqrt(2)/2
#     while widthA-i+R * math.sqrt(2)-R*math.sqrt(2)/2 > 0:
#         j = R * math.sqrt(2) / 2
#         while lengthB-j+R*math.sqrt(2)-R*math.sqrt(2)/2 > 0:
#             j+=R*math.sqrt(2)
#             count+=1
#         i += R * math.sqrt(2)
#     return count
# def square():
#     plt.title('Квадратное покрытие', fontsize=16, fontname='Times New Roman')
#     i = R*math.sqrt(2)/2
#     while widthA-i+R*math.sqrt(2)/2 > 0:
#         j = R * math.sqrt(2) / 2
#         while lengthB-j+R*math.sqrt(2)/2 > 0:
#             circle = Circle((j, i), R, edgecolor='black', facecolor='none')
#             ax.scatter(j, i, c='black', s=1)
#             ax.add_patch(circle)
#             j+=R*math.sqrt(2)
#         i += R * math.sqrt(2)
#     legend_elements = [Line2D([0], [0], marker='o', color='w', label='n = {value}'.format(value=countSquare()), markerfacecolor='black', markersize=4)]
#     plt.legend(title='Количество кругов:', handles=legend_elements, prop={"family": "Times New Roman", "size": 12})
#
# def countHexagonX():
#     count = 0
#     row = 1
#     i = R / 2
#     while widthA-i+R * math.sqrt(3)-R*math.sqrt(3)/2 > 0:
#         if row % 2 == 1:
#             j = R * math.sqrt(2) / 2
#             while lengthB-j+R*math.sqrt(3)-R*math.sqrt(3)/2 > 0:
#                 j += R * math.sqrt(3)
#                 count += 1
#         else:
#             j = R * math.sqrt(2) / 2 - R * math.sqrt(2) / 2
#             while lengthB-j+R*math.sqrt(3)-R*math.sqrt(3)/2 > 0:
#                 j += R * math.sqrt(3)
#                 count += 1
#
#         row += 1
#         i += R * 3 / 2
#     return count
#
# def countHexagonY():
#     count = 0
#     row = 1
#     i = R / 2
#     while lengthB-i+R*math.sqrt(3)-R*math.sqrt(3)/2 > 0:
#         if row % 2 == 1:
#             j = R * math.sqrt(2) / 2
#             while widthA-j+R * math.sqrt(3)-R*math.sqrt(3)/2 > 0:
#                 count += 1
#                 j += R * math.sqrt(3)
#         else:
#             j = R * math.sqrt(2) / 2 - R * math.sqrt(3) / 2
#             while widthA-j+R * math.sqrt(3)-R*math.sqrt(3)/2 > 0:
#                 count += 1
#                 j += R * math.sqrt(3)
#
#         row += 1
#         i += R * 3 / 2
#     return count
#
# def hexagonX():
#     plt.title('Гексагональное покрытие', fontsize=16, fontname='Times New Roman')
#     row = 1
#     i = R/2
#     while widthA - i + R*math.sqrt(3)/2 > 0:
#         if row%2==1:
#             j = R*math.sqrt(2)/2
#             while lengthB - j + R*math.sqrt(3)/2 > 0:
#                 circle = Circle((j, i), R, edgecolor='black', facecolor='none')
#                 ax.scatter(j, i, c='black', s=1)
#                 ax.add_patch(circle)
#                 j += R * math.sqrt(3)
#         else:
#             j = R*math.sqrt(2)/2 - R * math.sqrt(3) / 2
#             while lengthB - j + R*math.sqrt(3)/2 > 0:
#                 circle = Circle((j, i), R, edgecolor='black', facecolor='none')
#                 ax.scatter(j, i, c='black', s=1)
#                 ax.add_patch(circle)
#                 j += R * math.sqrt(3)
#         row+=1
#         i += R * 3/2
#     legend_elements = [Line2D([0], [0], marker='o', color='w', label='n = {value}'.format(value=countHexagonX()), markerfacecolor='black', markersize=4)]
#     plt.legend(title='Количество кругов:', handles=legend_elements, prop={"family": "Times New Roman", "size": 12})
#
# def hexagonY():
#     plt.title('Гексагональное покрытие', fontsize=16, fontname='Times New Roman')
#     row = 1
#     i = R/2
#     while lengthB - i + R*math.sqrt(3)/2 > 0:
#         if row%2==1:
#             j = R*math.sqrt(2)/2
#             while widthA - j + R*math.sqrt(3)/2 > 0:
#                 circle = Circle((i, j), R, edgecolor='black', facecolor='none')
#                 ax.scatter(i, j, c='black', s=1)
#                 ax.add_patch(circle)
#                 j += R * math.sqrt(3)
#         else:
#             j = R*math.sqrt(2)/2 - R * math.sqrt(3) / 2
#             while widthA - j + R*math.sqrt(3)/2 > 0:
#                 circle = Circle((i, j), R, edgecolor='black', facecolor='none')
#                 ax.scatter(i, j, c='black', s=1)
#                 ax.add_patch(circle)
#                 j += R * math.sqrt(3)
#         row+=1
#         i += R * 3/2
#     legend_elements = [Line2D([0], [0], marker='o', color='w', label='n = {value}'.format(value=countHexagonY()), markerfacecolor='black', markersize=4)]
#     plt.legend(title='Количество кругов:', handles=legend_elements, prop={"family": "Times New Roman", "size": 12})
#
# def countSquareTwo():
#     count = 0
#     i = R*math.sqrt(2)/2 - 3*r/4
#
#     if R * math.sqrt(2) + 3 * r / 4 < R:
#         while widthA-i+R > 0:
#             if(i>widthA)and(i-(R * math.sqrt(2) + 3*r/4)+R-3*r/4>widthA):
#                 return
#             j = R * math.sqrt(2) / 2 - 3*r/4
#             while lengthB-j+R > 0:
#                 if (j > lengthB) and (j - (R * math.sqrt(2) + 3 * r / 4) + R > lengthB):
#                     break
#                 count+=1
#                 if j-(R*math.sqrt(2)+3*r/4)/2 + 3*r/4 > 0 and (((j>lengthB) and (j-(R*math.sqrt(2)+3*r/4)/2 - 3*r/4) < lengthB) or ((j<lengthB)and(j-(R*math.sqrt(2)+3*r/4)/2 - 3*r/4) < lengthB))and (((i>widthA) and (i+(R*math.sqrt(2)+3*r/4)/2 - 3*r/4) < widthA) or ((i<widthA)and(i+(R*math.sqrt(2)+3*r/4)/2 - 3*r/4) < widthA)):
#                     count += 1
#                 j+=R*math.sqrt(2) + 3*r/4
#             if (j>lengthB) and (j-(R*math.sqrt(2)+3*r/4)/2 - 3*r/4) < lengthB and (((i>widthA) and (i+(R*math.sqrt(2)+3*r/4)/2 - 3*r/4) < widthA) or ((i<widthA)and(i+(R*math.sqrt(2)+3*r/4)/2 - 3*r/4) < widthA)):
#                 count += 1
#             i += R * math.sqrt(2) + 3*r/4
#             if (i > widthA) and (i - (R * math.sqrt(2) + 3*r/4) / 2 - 3*r/4) < widthA and (((j > lengthB) and (j + (R * math.sqrt(2) + 3*r/4) / 2 - 3*r/4) < lengthB) or ((j < lengthB) and (j + (R * math.sqrt(2) + 3*r/4) / 2 - 3*r/4) < lengthB)):
#                 count += 1
#     else:
#         while widthA-i+R > 0:
#             if(i>widthA)and(i-(R * math.sqrt(2) + r/2)+R-r/2>widthA):
#                 return
#             j = R * math.sqrt(2) / 2 - r/2
#             while lengthB-j+R > 0:
#                 if (j > lengthB) and (j - (R * math.sqrt(2) + r / 2) + R > lengthB):
#                     break
#                 count += 1
#                 if j-(R*math.sqrt(2)+r/2)/2 + r/2 > 0 and (((j>lengthB) and (j-(R*math.sqrt(2)+r/2)/2 - r/2) < lengthB) or ((j<lengthB)and(j-(R*math.sqrt(2)+r/2)/2 - r/2) < lengthB))and (((i>widthA) and (i+(R*math.sqrt(2)+r/2)/2 - r/2) < widthA) or ((i<widthA)and(i+(R*math.sqrt(2)+r/2)/2 - r/2) < widthA)):
#                     count += 1
#                 j+=R*math.sqrt(2) + r/2
#             if (j>lengthB) and (j-(R*math.sqrt(2)+r/2)/2 - r/2) < lengthB and (((i>widthA) and (i+(R*math.sqrt(2)+r/2)/2 - r/2) < widthA) or ((i<widthA)and(i+(R*math.sqrt(2)+r/2)/2 - r/2) < widthA)):
#                 count += 1
#             i += R * math.sqrt(2) + r/2
#             if (i > widthA) and (i - (R * math.sqrt(2) + r/2) / 2 - r/2) < widthA and (((j > lengthB) and (j + (R * math.sqrt(2) + r/2) / 2 - r/2) < lengthB) or ((j < lengthB) and (j + (R * math.sqrt(2) + r/2) / 2 - r/2) < lengthB)):
#                 count += 1
#     return count
#
# def squareTwoX():
#     i = R*math.sqrt(2)/2 - 3*r/4
#
#     if R * math.sqrt(2) + 3 * r / 4 < R:
#         while widthA-i+R > 0:
#             if(i>widthA)and(i-(R * math.sqrt(2) + 3*r/4)+R-3*r/4>widthA):
#                 return
#             j = R * math.sqrt(2) / 2 - 3*r/4
#             while lengthB-j+R > 0:
#                 if (j > lengthB) and (j - (R * math.sqrt(2) + 3 * r / 4) + R > lengthB):
#                     break
#                 circle = Circle((j, i), R, edgecolor='black', facecolor='none')
#                 ax.scatter(j, i, c='black', s=1)
#                 ax.add_patch(circle)
#                 if j-(R*math.sqrt(2)+3*r/4)/2 + 3*r/4 > 0 and (((j>lengthB) and (j-(R*math.sqrt(2)+3*r/4)/2 - 3*r/4) < lengthB) or ((j<lengthB)and(j-(R*math.sqrt(2)+3*r/4)/2 - 3*r/4) < lengthB))and (((i>widthA) and (i+(R*math.sqrt(2)+3*r/4)/2 - 3*r/4) < widthA) or ((i<widthA)and(i+(R*math.sqrt(2)+3*r/4)/2 - 3*r/4) < widthA)):
#                     circleMin = Circle((j-(R*math.sqrt(2)+3*r/4)/2, i+(R*math.sqrt(2)+3*r/4)/2), r, edgecolor='black', facecolor='none')
#                     ax.add_patch(circleMin)
#                 j+=R*math.sqrt(2) + 3*r/4
#             if (j>lengthB) and (j-(R*math.sqrt(2)+3*r/4)/2 - 3*r/4) < lengthB and (((i>widthA) and (i+(R*math.sqrt(2)+3*r/4)/2 - 3*r/4) < widthA) or ((i<widthA)and(i+(R*math.sqrt(2)+3*r/4)/2 - 3*r/4) < widthA)):
#                 circleMin = Circle((j-(R*math.sqrt(2)+3*r/4)/2, i+(R*math.sqrt(2)+3*r/4)/2), r, edgecolor='black', facecolor='none')
#                 ax.add_patch(circleMin)
#             i += R * math.sqrt(2) + 3*r/4
#             if (i > widthA) and (i - (R * math.sqrt(2) + 3*r/4) / 2 - 3*r/4) < widthA and (((j > lengthB) and (j + (R * math.sqrt(2) + 3*r/4) / 2 - 3*r/4) < lengthB) or ((j < lengthB) and (j + (R * math.sqrt(2) + 3*r/4) / 2 - 3*r/4) < lengthB)):
#                 circleMin = Circle((j - (R * math.sqrt(2) + 3*r/4) / 2, i + (R * math.sqrt(2) + 3*r/4) / 2), r, edgecolor='black', facecolor='none')
#                 ax.add_patch(circleMin)
#     else:
#         while widthA-i+R > 0:
#             if(i>widthA)and(i-(R * math.sqrt(2) + r/2)+R-r/2>widthA):
#                 return
#             j = R * math.sqrt(2) / 2 - r/2
#             while lengthB-j+R > 0:
#                 if (j > lengthB) and (j - (R * math.sqrt(2) + r / 2) + R > lengthB):
#                     break
#                 circle = Circle((j, i), R, edgecolor='black', facecolor='none')
#                 ax.scatter(j, i, c='black', s=1)
#                 ax.add_patch(circle)
#                 if j-(R*math.sqrt(2)+r/2)/2 + r/2 > 0 and (((j>lengthB) and (j-(R*math.sqrt(2)+r/2)/2 - r/2) < lengthB) or ((j<lengthB)and(j-(R*math.sqrt(2)+r/2)/2 - r/2) < lengthB))and (((i>widthA) and (i+(R*math.sqrt(2)+r/2)/2 - r/2) < widthA) or ((i<widthA)and(i+(R*math.sqrt(2)+r/2)/2 - r/2) < widthA)):
#                     circleMin = Circle((j-(R*math.sqrt(2)+r/2)/2, i+(R*math.sqrt(2)+r/2)/2), r, edgecolor='black', facecolor='none')
#                     ax.add_patch(circleMin)
#                 j+=R*math.sqrt(2) + r/2
#             if (j>lengthB) and (j-(R*math.sqrt(2)+r/2)/2 - r/2) < lengthB and (((i>widthA) and (i+(R*math.sqrt(2)+r/2)/2 - r/2) < widthA) or ((i<widthA)and(i+(R*math.sqrt(2)+r/2)/2 - r/2) < widthA)):
#                 circleMin = Circle((j-(R*math.sqrt(2)+r/2)/2, i+(R*math.sqrt(2)+r/2)/2), r, edgecolor='black', facecolor='none')
#                 ax.add_patch(circleMin)
#             i += R * math.sqrt(2) + r/2
#             if (i > widthA) and (i - (R * math.sqrt(2) + r/2) / 2 - r/2) < widthA and (((j > lengthB) and (j + (R * math.sqrt(2) + r/2) / 2 - r/2) < lengthB) or ((j < lengthB) and (j + (R * math.sqrt(2) + r/2) / 2 - r/2) < lengthB)):
#                 circleMin = Circle((j - (R * math.sqrt(2) + r/2) / 2, i + (R * math.sqrt(2) + r/2) / 2), r, edgecolor='black', facecolor='none')
#                 ax.add_patch(circleMin)
#
#     legend_elements = [Line2D([0], [0], marker='o', color='w', label='n = {value}'.format(value=countSquareTwo()), markerfacecolor='black', markersize=4)]
#     plt.legend(title='Количество кругов:', handles=legend_elements, prop={"family": "Times New Roman", "size": 12})
#
# def countHexagonXTwo():
#     count = 0
#     if r >= R / math.sqrt(3):
#         row = 1
#         i = R / 2 - R / math.sqrt(3)
#         while widthA - i + R * math.sqrt(3) - R * math.sqrt(3) / 2 > 0:
#             if row % 2 == 1:
#                 j = R * math.sqrt(2) / 2 - R / math.sqrt(3) / 2
#                 while lengthB - j + R * math.sqrt(3) - R * math.sqrt(3) / 2 > 0:
#                     count+=1
#                     if (((j > lengthB) and (j + R - R / math.sqrt(3) / 2) < lengthB) or ((j < lengthB) and (j + R - R / math.sqrt(3)) < lengthB)) and ((((i > widthA) and (i + R - R / math.sqrt(3) / 2)) < widthA) or ((i < widthA) and (i + R - R / math.sqrt(3) / 2 < widthA))):
#                         count += 1
#                     if (j - R / math.sqrt(3) / 2 < lengthB) and (i + R < widthA):
#                         count += 1
#                     j += 2 * R
#             else:
#                 j = R * math.sqrt(2) / 2 - 2 * R / 2 - R / math.sqrt(3) / 2
#                 while lengthB - j + R * math.sqrt(3) - R * math.sqrt(3) / 2 > 0:
#                     count += 1
#                     if (j - R > 0) and (((j > lengthB) and (j - R / math.sqrt(3)) < lengthB) or (
#                             (j < lengthB) and (j - R / math.sqrt(3) / 2) < lengthB)) and (
#                             ((i > widthA) and (i + R - R / math.sqrt(3) / 2) < widthA) or (
#                             (i < widthA) and (i + R < widthA))):
#                         count += 1
#                     if (j + R - R / math.sqrt(3) / 2 < lengthB) and (i < widthA):
#                         count += 1
#                     j += 2 * R
#             row += 1
#             i += R * math.sqrt(3)
#         return count
#     else:
#         row = 1
#         i = R / 2 - 5 * r / 8
#         while widthA - i + R > 0:
#             if row % 2 == 1:
#                 j = R * math.sqrt(2) / 2 - r / 2
#                 while lengthB - j + R > 0:
#                     count+=1
#                     if (((j > lengthB) and (j + (R * math.sqrt(3) + r / 2) / 2 - 3 * r / 4) < lengthB) or (
#                             (j < lengthB) and (j + (R * math.sqrt(3) + r / 2) / 2 - 3 * r / 4) < lengthB)) and (((i > widthA) and (i + R - 3 * r / 4 < widthA)) or (
#                             (i < widthA) and (i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 - r) < widthA)):
#                         count += 1
#                     if (((j > lengthB) and (j - 3 * r / 4 < lengthB)) or (
#                             (j < lengthB) and (j - 3 * r / 4 < lengthB))) and (i + R < widthA):
#                         count += 1
#                     j += R * math.sqrt(3) + r / 2
#             else:
#                 j = R * math.sqrt(2) / 2 - r / 2 - (R * math.sqrt(3) + r / 2) / 2
#                 while lengthB - j + R > 0:
#                     count += 1
#                     if (j - R > 0) and (((j > lengthB) and (j - 3 * r / 4) < lengthB) or (
#                             (j < lengthB) and (j - r / 2) < lengthB)) and (
#                             ((i > widthA) and (i + R - r / 2) < widthA) or ((i < widthA) and (i + R < widthA))):
#                         count += 1
#                     if (((j > lengthB) and (j + (R * math.sqrt(3) + r / 2) / 2 - 3 * r / 4 < lengthB)) or (
#                             (j < lengthB) and (j + (R * math.sqrt(3) + r / 2) / 2 - 3 * r / 4 < lengthB))) and (((i < widthA) and ( i + ((R * math.sqrt(3) + r / 2) * math.sqrt( 3) / 2) / 2 - 3 * r / 4 < widthA)) or (( i > widthA) and (i + ((R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2) / 2 - 3 * r / 4) < widthA)):
#                         count += 1
#                     j += R * math.sqrt(3) + r / 2
#             row += 1
#             i += (R * math.sqrt(3) + r / 2) * math.sqrt(3) / 2
#         return count
#
# def countHexagonYTwo():
#     count = 0
#     if r >= R / math.sqrt(3):
#         row = 1
#         i = R / 2 - R / math.sqrt(3)
#         while lengthB - i + R * math.sqrt(3) - R * math.sqrt(3) / 2 > 0:
#             if row % 2 == 1:
#                 j = R * math.sqrt(2) / 2 - R / math.sqrt(3) / 2
#                 while widthA - j + R * math.sqrt(3) - R * math.sqrt(3) / 2 > 0:
#                     count+=1
#                     if (((j > widthA) and (j + R - R / math.sqrt(3) / 2) < widthA) or (
#                             (j < widthA) and (j + R - R / math.sqrt(3)) < widthA)) and ((((i > lengthB) and (i + R * math.sqrt(3) / 2 - R / math.sqrt(3) / 2)) < lengthB) or ((i < lengthB) and ( i + R * math.sqrt(3) / 2 - R / math.sqrt(3) / 2 < lengthB))):
#                         count += 1
#                     if (((j > widthA) and (j - R / math.sqrt(3) / 2 < widthA)) or ((j < widthA) and (j - R / math.sqrt(3) / 2 < widthA))) and (i + R < lengthB):
#                         count += 1
#                     j += 2 * R
#             else:
#                 j = R * math.sqrt(2) / 2 - 2 * R / 2 - R / math.sqrt(3) / 2
#                 while widthA - j + R * math.sqrt(3) - R * math.sqrt(3) / 2 > 0:
#                     count += 1
#                     if (j - R > 0) and (((j > widthA) and (j - R - R / math.sqrt(3) / 2) < widthA) or (
#                             (j < widthA) and (j - R / math.sqrt(3) / 2) < widthA)) and (
#                             ((i > lengthB) and (i + R - R / math.sqrt(3) / 2) < lengthB) or (
#                             (i < lengthB) and (i + R < lengthB))):
#                         count += 1
#                     if (((i < lengthB) and (i + R - R * math.sqrt(3) / 2 < lengthB)) or (i > lengthB) and (
#                             i + R - R * math.sqrt(3) / 2 < lengthB)) and (j + R - R / math.sqrt(3) / 2 < widthA):
#                         count += 1
#                     j += 2 * R
#             row += 1
#             i += R * math.sqrt(3)
#         return count
#     else:
#         row = 1
#         i = R / 2 - 3*r / 4
#         while lengthB - i + R > 0:
#             if row % 2 == 1:
#                 j = R*math.sqrt(2)/2 - r/2
#                 while widthA - j + R > 0:
#                     count+=1
#                     if (((j > widthA) and (j + R - 3*r/4) < widthA) or ((j < widthA) and (j + (R*math.sqrt(3) + r/2)/2 - 3*r/4) < widthA)) and (((i > lengthB) and (i + R - r/2) < lengthB) or ((i < lengthB) and (i + ((R*math.sqrt(3) + r/2)*math.sqrt(3)/2)/2 - 3*r/4 < lengthB))):
#                         count += 1
#                     if (((j > widthA) and (j - r/2 < widthA)) or ((j<widthA) and (j - r/2 < widthA))) and (i + R < lengthB):
#                         count += 1
#                     j += R*math.sqrt(3) + r/2
#             else:
#                 j = R*math.sqrt(2)/2 - r/2 - (R*math.sqrt(3)+r/2)/2
#                 while widthA - j + R > 0:
#                     count += 1
#                     if (j - R > 0) and (((j > widthA) and (j - 3*r/4) < widthA) or ((j < widthA) and (j - r/2 / 2) < widthA)) and (((i > lengthB) and (i + R - r/2 / 2) < lengthB) or ((i < lengthB) and (i + R < lengthB))):
#                         count += 1
#                     if (((i<lengthB) and (i + ((R*math.sqrt(3) + r/2)*math.sqrt(3)/2)/2 - r < lengthB)) or (i>lengthB) and (i + ((R*math.sqrt(3) + r/2)*math.sqrt(3)/2)/2 - 3*r/4 < lengthB)) and (j + (R*math.sqrt(3) + r/2)/2 - r/2 < widthA):
#                         count += 1
#                     j += R*math.sqrt(3) + r/2
#             row += 1
#             i += (R*math.sqrt(3) + r/2)*math.sqrt(3)/2
#         return count
#
# def hexagonXTwo():
#     plt.title('Гексагональное покрытие', fontsize=16, fontname='Times New Roman')
#     if r >= R / math.sqrt(3):
#         row = 1
#         i = R/2 - R/math.sqrt(3)
#         while widthA-i+R * math.sqrt(3)-R*math.sqrt(3)/2 > 0:
#             if row%2==1:
#                 j = R*math.sqrt(2)/2 - R/math.sqrt(3)/2
#                 while lengthB-j+R*math.sqrt(3)-R*math.sqrt(3)/2 > 0:
#                     circle = Circle((j, i), R, edgecolor='black', facecolor='none')
#                     ax.scatter(j, i, c='black', s=1)
#                     ax.add_patch(circle)
#                     if (((j > lengthB) and (j + R - R/math.sqrt(3)/2) < lengthB) or (
#                             (j < lengthB) and (j + R - R/math.sqrt(3)) < lengthB)) and ((
#                             ((i > widthA) and (i + R - R/math.sqrt(3)/2)) < widthA) or (
#                             (i < widthA) and (i + R - R/math.sqrt(3)/2 < widthA))):
#                         circleMinCenter = Circle((j+R, i + (R/math.sqrt(3))), r,edgecolor='black', facecolor='none')
#                         ax.add_patch(circleMinCenter)
#                     if (j - R/math.sqrt(3)/2 < lengthB) and (i + R < widthA):
#                         circleMinUp = Circle((j, i + R + (R/math.sqrt(3))/2), r,edgecolor='black', facecolor='none')
#                         ax.add_patch(circleMinUp)
#                     j += 2*R
#             else:
#                 j = R*math.sqrt(2)/2 - 2*R / 2 - R/math.sqrt(3)/2
#                 while lengthB-j+R*math.sqrt(3)-R*math.sqrt(3)/2 > 0:
#                     circle = Circle((j, i), R, edgecolor='black', facecolor='none')
#                     ax.scatter(j, i, c='black', s=1)
#                     ax.add_patch(circle)
#                     if (j-R > 0) and (((j > lengthB) and (j- R/math.sqrt(3)) < lengthB) or ((j < lengthB) and (j - R/math.sqrt(3)/2) < lengthB)) and (((i > widthA) and (i + R - R/math.sqrt(3)/2) < widthA) or ((i < widthA) and (i + R < widthA))):
#                         circleMinUp = Circle((j, i + R + (R/math.sqrt(3))/2), r, edgecolor='black', facecolor='none')
#                         ax.add_patch(circleMinUp)
#                     if (j + R - R/math.sqrt(3)/2 < lengthB) and (i < widthA):
#                         circleMinCenter = Circle((j+R, i + (R/math.sqrt(3))), r, edgecolor='black', facecolor='none')
#                         ax.add_patch(circleMinCenter)
#                     j += 2*R
#             row+=1
#             i += R*math.sqrt(3)
#         legend_elements = [Line2D([0], [0], marker='o', color='w', label='n = {value}'.format(value=countHexagonXTwo()), markerfacecolor='black', markersize=4)]
#         plt.legend(title='Количество кругов:', handles=legend_elements, prop={"family": "Times New Roman", "size": 12})
#
#     else:
#         row = 1
#         i = R/2 - 5*r/8
#         while widthA-i+R > 0:
#             if row%2==1:
#                 j = R*math.sqrt(2)/2 - r/2
#                 while lengthB-j+R > 0:
#                     circle = Circle((j, i), R, edgecolor='black', facecolor='none')
#                     ax.scatter(j, i, c='black', s=1)
#                     ax.add_patch(circle)
#                     if (((j > lengthB) and (j + (R*math.sqrt(3) + r/2)/2 - 3*r/4) < lengthB) or ((j < lengthB) and (j + (R*math.sqrt(3) + r/2)/2 - 3*r/4) < lengthB)) and (((i > widthA) and (i + R - 3*r/4 < widthA)) or ((i < widthA) and (i + ((R*math.sqrt(3) + r/2)*math.sqrt(3)/2)/2 - r) < widthA)):
#                         circleMinCenter = Circle((j+(R*math.sqrt(3) + r/2)/2, i + ((R*math.sqrt(3) + r/2)*math.sqrt(3)/2)/2 - 3*r/4), r, edgecolor='black', facecolor='none')
#                         ax.add_patch(circleMinCenter)
#                     if (((j>lengthB)and (j - 3*r/4 < lengthB)) or ((j<lengthB)and (j - 3*r/4 < lengthB))) and (i + R < widthA):
#                         circleMinUp = Circle((j, i + R + r/2), r, edgecolor='black', facecolor='none')
#                         ax.add_patch(circleMinUp)
#                     j += R*math.sqrt(3) + r/2
#             else:
#                 j = R*math.sqrt(2)/2 - r/2- (R*math.sqrt(3)+r/2)/2
#                 while lengthB-j+R > 0:
#                     circle = Circle((j, i), R, edgecolor='black', facecolor='none')
#                     ax.scatter(j, i, c='black', s=1)
#                     ax.add_patch(circle)
#                     if (j-R > 0) and (((j > lengthB) and (j - 3*r/4) < lengthB) or ((j < lengthB) and (j - r/2) < lengthB)) and (((i > widthA) and (i + R - r/2) < widthA) or ((i < widthA) and (i + R < widthA))):
#                         circleMinUp = Circle((j, i + R + r/2), r, edgecolor='black', facecolor='none')
#                         ax.add_patch(circleMinUp)
#                     if (((j>lengthB)and (j +(R*math.sqrt(3) + r/2)/2 - 3*r/4 < lengthB)) or ((j<lengthB) and (j + (R*math.sqrt(3) + r/2)/2 - 3*r/4 < lengthB))) and (((i<widthA) and (i + ((R*math.sqrt(3) + r/2)*math.sqrt(3)/2)/2 - 3*r/4 < widthA)) or ((i>widthA) and (i + ((R*math.sqrt(3) + r/2)*math.sqrt(3)/2)/2 - 3*r/4)<widthA)):
#                         circleMinCenter = Circle((j+(R*math.sqrt(3) + r/2)/2, i + ((R*math.sqrt(3) + r/2)*math.sqrt(3)/2)/2 - 3*r/4), r, edgecolor='black', facecolor='none')
#                         ax.add_patch(circleMinCenter)
#                     j += R*math.sqrt(3) + r/2
#             row+=1
#             i += (R*math.sqrt(3) + r/2)*math.sqrt(3)/2
#         legend_elements = [Line2D([0], [0], marker='o', color='w', label='n = {value}'.format(value=countHexagonXTwo()), markerfacecolor='black', markersize=4)]
#         plt.legend(title='Количество кругов:', handles=legend_elements, prop={"family": "Times New Roman", "size": 12})
#
#
# def hexagonYTwo():
#     plt.title('Гексагональное покрытие', fontsize=16, fontname='Times New Roman')
#     if r >= R/math.sqrt(3):
#         row = 1
#         i = R/2 - R/math.sqrt(3)
#         while lengthB-i+R * math.sqrt(3)-R*math.sqrt(3)/2 > 0:
#             if row%2==1:
#                 j = R*math.sqrt(2)/2 - R/math.sqrt(3)/2
#                 while widthA-j+R*math.sqrt(3)-R*math.sqrt(3)/2 > 0:
#                     circle = Circle((i, j), R, edgecolor='black', facecolor='none')
#                     ax.scatter(i, j, c='black', s=1)
#                     ax.add_patch(circle)
#                     if (((j > widthA) and (j + R - R/math.sqrt(3)/2) < widthA) or (
#                             (j < widthA) and (j + R - R/math.sqrt(3)) < widthA)) and ((
#                             ((i > lengthB) and (i + R*math.sqrt(3)/2 - R/math.sqrt(3)/2)) < lengthB) or (
#                             (i < lengthB) and (i + R*math.sqrt(3)/2 - R/math.sqrt(3)/2 < lengthB))):
#                         circleMinCenter = Circle((i + (R/math.sqrt(3)), j+R), r,edgecolor='black', facecolor='none')
#                         ax.add_patch(circleMinCenter)
#                     if (((j > widthA) and (j - R/math.sqrt(3)/ 2 < widthA)) or ((j < widthA) and (j - R/math.sqrt(3)/ 2 < widthA))) and (i + R < lengthB):
#                         circleMinUp = Circle((i + R + (R/math.sqrt(3))/2, j), r,edgecolor='black', facecolor='none')
#                         ax.add_patch(circleMinUp)
#                     j += 2*R
#             else:
#                 j = R*math.sqrt(2)/2 - 2*R / 2 - R/math.sqrt(3)/2
#                 while widthA-j+R*math.sqrt(3)-R*math.sqrt(3)/2 > 0:
#                     circle = Circle((i, j), R, edgecolor='black', facecolor='none')
#                     ax.scatter(i, j, c='black', s=1)
#                     ax.add_patch(circle)
#                     if (j-R > 0) and (((j > widthA) and (j - R - R/math.sqrt(3)/2) < widthA) or ((j < widthA) and (j - R/math.sqrt(3)/2) < widthA)) and (((i > lengthB) and (i + R - R/math.sqrt(3)/2) < lengthB) or ((i < lengthB) and (i + R < lengthB))):
#                         circleMinUp = Circle((i + R + (R/math.sqrt(3))/2,j), r, edgecolor='black', facecolor='none')
#                         ax.add_patch(circleMinUp)
#                     if (((i < lengthB) and (i + R - R*math.sqrt(3)/2 < lengthB)) or (i > lengthB) and (i + R - R*math.sqrt(3)/2 < lengthB)) and (j + R - R/math.sqrt(3)/2 < widthA):
#                         circleMinCenter = Circle((i + (R/math.sqrt(3)), j + R), r, edgecolor='black', facecolor='none')
#                         ax.add_patch(circleMinCenter)
#                     j += 2*R
#             row+=1
#             i += R*math.sqrt(3)
#         legend_elements = [Line2D([0], [0], marker='o', color='w', label='n = {value}'.format(value=countHexagonYTwo()), markerfacecolor='black', markersize=4)]
#         plt.legend(title='Количество кругов:', handles=legend_elements, prop={"family": "Times New Roman", "size": 12})
#     else:
#         row = 1
#         i = R / 2 - 5*r / 8
#         while lengthB - i + R > 0:
#             if row % 2 == 1:
#                 j = R*math.sqrt(2)/2 - r/2
#                 while widthA - j + R > 0:
#                     circle = Circle((i, j), R, edgecolor='black', facecolor='none')
#                     ax.scatter(i, j, c='black', s=1)
#                     ax.add_patch(circle)
#                     if (((j > widthA) and (j + R - 3*r/4) < widthA) or ((j < widthA) and (j + (R*math.sqrt(3) + r/2)/2 - 3*r/4) < widthA)) and (((i > lengthB) and (i + R - r/2) < lengthB) or ((i < lengthB) and (i + ((R*math.sqrt(3) + r/2)*math.sqrt(3)/2)/2 - 3*r/4 < lengthB))):
#                         circleMinCenter = Circle((i + ((R*math.sqrt(3) + r/2)*math.sqrt(3)/2)/2-r, j + (R*math.sqrt(3) + r/2)/2), r, edgecolor='black',facecolor='none')
#                         ax.add_patch(circleMinCenter)
#                     if (((j > widthA) and (j - r/2 < widthA)) or ((j<widthA) and (j - r/2 < widthA))) and (i + R < lengthB):
#                         circleMinUp = Circle((i + ((R*math.sqrt(3) + r/2)*math.sqrt(3)/2)/2 + r, j), r, edgecolor='black',facecolor='none')
#                         ax.add_patch(circleMinUp)
#                     j += R*math.sqrt(3) + r/2
#             else:
#                 j = R*math.sqrt(2)/2 - r/2 - (R*math.sqrt(3)+r/2)/2
#                 while widthA - j + R > 0:
#                     circle = Circle((i, j), R, edgecolor='black', facecolor='none')
#                     ax.scatter(i, j, c='black', s=1)
#                     ax.add_patch(circle)
#                     if (j - R > 0) and (((j > widthA) and (j - 3*r/4) < widthA) or ((j < widthA) and (j - r/2 / 2) < widthA)) and (((i > lengthB) and (i + R - r/2 / 2) < lengthB) or ((i < lengthB) and (i + R < lengthB))):
#                         circleMinUp = Circle((i + ((R*math.sqrt(3) + r/2)*math.sqrt(3)/2)/2 + r, j), r, edgecolor='black',facecolor='none')
#                         ax.add_patch(circleMinUp)
#                     if (((i<lengthB) and (i + ((R*math.sqrt(3) + r/2)*math.sqrt(3)/2)/2 - r < lengthB)) or (i>lengthB) and (i + ((R*math.sqrt(3) + r/2)*math.sqrt(3)/2)/2 - 3*r/4 < lengthB)) and (j + (R*math.sqrt(3) + r/2)/2 - r/2 < widthA):
#                         circleMinCenter = Circle((i + ((R*math.sqrt(3) + r/2)*math.sqrt(3)/2)/2 - r, j + (R*math.sqrt(3) + r/2)/2), r, edgecolor='black',facecolor='none')
#                         ax.add_patch(circleMinCenter)
#                     j += R*math.sqrt(3) + r/2
#             row += 1
#             i += (R*math.sqrt(3) + r/2)*math.sqrt(3)/2
#             legend_elements = [Line2D([0], [0], marker='o', color='w', label='n = {value}'.format(value=countHexagonYTwo()),markerfacecolor='black', markersize=4)]
#             plt.legend(title='Количество кругов:', handles=legend_elements, prop={"family": "Times New Roman", "size": 12})
#
#
# if check == '1':
#     square()
# elif check == '2':
#     if countHexagonX() > countHexagonY():
#         hexagonY()
#         print('Количество кругов при X:', countHexagonX(), 'и при Y:', countHexagonY())
#     else:
#         hexagonX()
#         print('Количество кругов при X:', countHexagonX(), 'и при Y:', countHexagonY())
# elif check == '3':
#     squareTwoX()
# elif check == '4':
#     # hexagonXTwo()
#     if countHexagonXTwo() > countHexagonYTwo():
#         hexagonYTwo()
#         print('Количество кругов для одного радиуса при X:', countHexagonX(), 'и при Y:', countHexagonY())
#         print('Количество кругов для двух радиусов при X:', countHexagonXTwo(), 'и при Y:', countHexagonYTwo())
#     else:
#         hexagonXTwo()
#         print('Количество кругов для одного радиуса при X:', countHexagonX(), 'и при Y:', countHexagonY())
#         print('Количество кругов для двух радиусов при X:', countHexagonXTwo(), 'и при Y:', countHexagonYTwo())
#
# plt.savefig('output.png')
# plt.show()
