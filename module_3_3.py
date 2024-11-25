def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print(print_params)
print_params(b = 25)
print_params(c = [1,2,3])
values_list=[[1,2,3], 'Urban', 3]
print_params(*values_list)
values_dict={'a': [11,12,13], 'b': 'Hello world', 'c': 55}
print_params(**values_dict)
values_list_2=['surprise', 777]
print_params(*values_list_2, 42)