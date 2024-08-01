def print_params (a = 1, b  = 'строка', c = True):
	print (a, b, c)
	
print ('1. Функция с параметрами по умолчанию')
print_params (45, 'test', False)
print_params ()
print_params (23)
print ()
print_params (b = 25)
print ('Работает')
print ()
print_params (c = [1, 2, 3])
print ('Работает')
print ()

values_list = ['Среда', True, [4, 3, 2]]
values_dict = {'a': 44, 'b': 0.5, 'c': 'проверка'}
print ('2. Распаковка параметров')
print ('Распаковка списка:')
print_params (*values_list)
print ()
print ('Распаковка словаря:')
print_params (**values_dict)
print ()

values_list_2 = ['August', 567]
print ('3. Распаковка + отдельные параметры')
print_params (*values_list_2, 42)
print ('Работает')