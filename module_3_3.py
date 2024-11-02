def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    print()
print_params()
print_params(b=25)
print_params(c=[1,2,3])
print_params(b = 25, c =[1, 2, 3])
values_list = [5, 4, 1996]
values_dict = {'a': 11, 'b': 8, 'c': 1995}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [28, 'good']
print_params(*values_list_2, 42)
