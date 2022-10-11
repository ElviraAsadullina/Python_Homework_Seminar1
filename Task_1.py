def is_number_check(text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{text}'))
            is_OK = True
        except ValueError:
            print('Введенное значение не получается соотнести с днем недели!')
    return number
def is_weekend_check(number):
    if 6 <= number <= 7:
        print('Да')
    elif 0 < number < 6:
        print('Нет')
    else:
        print('Введенное число не получается соотнести с днем недели!')
d = is_number_check('Введите цифру от 1 до 7: ')
is_weekend_check(d)