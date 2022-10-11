def input_numbers(count):
    variables = ['X', 'Y', 'Z']
    a = []
    for i in range(count):
        a.append(input(f'Введите значение {variables[i]}: '))
    return a
def is_predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result
equality = input_numbers(3)
if is_predicate(equality) == True:
    print('Утверждение истинно.')
else:
    print('Утверждение ложно.')