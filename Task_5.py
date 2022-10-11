def check_for_input_error(a1, b1, a2, b2):
    while True:
        try:        
            a1 = float(input('Введите координату первой точки по оси X: '))
            b1 = float(input('Введите координату первой точки по оси Y: '))
            a2 = float(input('Введите координату второй точки по оси X: '))
            b2 = float(input('Введите координату второй точки по оси Y: '))
        except ValueError:
            print('Ошибка - введено не числовое значение!')
            continue
        return a1, b1, a2, b2
x1, y1, x2, y2 = None, None, None, None
x1, y1, x2, y2 = check_for_input_error(x1, y1, x2, y2)
from math import hypot
print(f'Расстояние между указанными точками равно {hypot(x2 - x1, y2 - y1):.2f}')