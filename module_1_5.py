immutable_var_tuple =(1,2,3,'кортеж')
print(immutable_var_tuple)
#immutable_var_tuple [0]=2 #TypeError: 'tuple' object does not support item assignment
                            #кортеж является неизменяемым объектом
mutable_list=[1,2,3,'список']
mutable_list[3]="list"
print(mutable_list)
