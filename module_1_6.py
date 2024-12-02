my_dict = {'Vlad': 1979, 'Vika':1988, 'Kolya':1996}
print(my_dict)
print(my_dict['Vlad'])
my_dict['Lena']=1993
print(my_dict)
my_dict.update({'Oleg':1965, 'Dima':1985})
del my_dict['Vlad']
print(my_dict.get('Vlad'))
print(my_dict)

my_set={'Vlad', 45, 1979,2.5,'Vlad', 2.5}
print(my_set)
my_set.update({"Vika", 36})
my_set.discard(2.5)
print(my_set)
