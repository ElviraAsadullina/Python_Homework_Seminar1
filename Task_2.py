for x in range(10):
    for y in range(10):
        for z in range(10):
            if (not(x or y or z)) == (not x and not y and not z):
                print(f'{x} {y} {z} -> Утверждение ИСТИННО')
            else:
                print(f'{x} {y} {z} -> Утверждение ЛОЖНО')