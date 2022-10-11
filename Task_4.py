def check_for_input_error(a):
    while True:
        try:        
            a = int(input('Введите номер четверти: '))
        except ValueError:
            print('Ошибка - введено не числовое значение!')
            continue
        if  a < 1 or a > 4:
            print('Номер четверти должен быть в диапазоне от 1 до 4!')
            continue
        break
    return a
def find_range(a):
    if a == 1:
        print('Диапазон по оси Х: от 1 до 10; Диапазон по оси Y: от 1 до 10')
    elif a == 2:
        print('Диапазон по оси Х: от -10 до -1; Диапазон по оси Y: от 1 до 10')
    elif a == 3:
        print('Диапазон по оси Х: от -10 до -1; Диапазон по оси Y: от -10 до -1')    
    else:
        print('Диапазон по оси Х: от 1 до 10; Диапазон по оси Y: от -10 до -1')   
q = None
q = check_for_input_error(q)
find_range(q)