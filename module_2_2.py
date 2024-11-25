fisrt, second, third =int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: '))
if fisrt == second == third:
    print(3)
elif fisrt==second or fisrt==third or second==third:
    print(2)
else: print(0)