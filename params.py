# 1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(3, 'Привет', 0.5)
print_params(a=10, b='Привет')
print_params(b='Hello', c= 'world!')
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

# 2
values_list = [0.5, 55, 'SKY']
values_dict = {'a': 99, 'b': 'Ok', 'c': False}
print_params(*values_list)
print_params(**values_dict)

#3
values_list_2 = ['Sun', 55]
print_params(*values_list_2, 42)