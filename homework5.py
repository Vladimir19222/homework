immutable_var = 5,6, True, 'apple'
print('кортеж immutable_var:',immutable_var)
print(immutable_var[0],immutable_var[1],immutable_var[2],immutable_var[3])
print("типы элементов:")
print(type(immutable_var[0]))
print(type(immutable_var[1]))
print(type(immutable_var[2]))
print(type(immutable_var[3]))
mutable_list = [7, 8, 'horse', 'peach', True]
print('список mutable_list:',mutable_list)
mutable_list[0] = 'appel'# изменяем значения некоторых элементов списка
mutable_list[1] = False
mutable_list[2] = 9
mutable_list.append('banana')# добавляем в конец списка
print('список mutable_list после изменения',mutable_list)
message = 'объект «кортеж» не поддерживает назначение элементов'
print('если пытаюсь изменить элемент кортежа, например, immutable_var[1] = 10,то получаю сообщение:', message)
#immutable_var[1] = 10