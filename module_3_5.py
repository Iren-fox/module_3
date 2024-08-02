def get_miltiplied_digits (number):
	str_number = str(number)
	first = int(str_number[0])
	if len(str_number) <= 1:
		return first
	else:
		return first*get_miltiplied_digits(int(str_number[1:]))
	
number = 40203
print (f'Произведение цифр числа {number} равно:' , get_miltiplied_digits (number))


	

