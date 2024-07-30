calls = 0

def count_calls () :
		global calls
		calls += 1

def string_info (string):
	count_calls ()
	len_ = len (string)
	upper_ = string.upper ()
	lower_ = string.lower ()
	print (len_ , upper_, lower_)
	

def is_contains (string , list_to_search) :
	count_calls ()
	cond = False
	for i in list_to_search:
		x = i.lower ()
		y = string.lower ()
		if x == y:
			cond = True
			break
		else:
			cond = False
	print (cond)
	
	
string_info ('Urban')
is_contains ('hi', ['what', 'monday', 'sun'])

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)