def find_quarter (x, y):
    if x > 0:
        if y > 0:
            print('Точка расположена в I четверти.')
        else:
            print('Точка расположена в IV четверти.')
    else:
        if y > 0:
            print('Точка расположена во II четверти.')
        else:
            print('Точка расположена в III четверти.')
def check_for_zero(a, b):
    while True:
        try:        
            a = float(input('Введите координату точки по оси X: '))
            b = float(input('Введите координату точки по оси Y: '))
        except ValueError:
            print('Ошибка - введено не числовое значение!')
            continue
        if a == 0 or b == 0:
            print('Значение координаты должно быть отлично от нуля!')
            continue
        break
    return a, b
a, b = None, None
a, b = check_for_zero(a, b)
find_quarter (a, b)