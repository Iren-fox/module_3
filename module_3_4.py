def single_root_words (root_words, *other_words):
	same_words = []
	for i in range (len (other_words)):
		other_words_reg = other_words[i].lower ()
		root_words_reg = root_words.lower ()
		if root_words_reg in other_words_reg or other_words_reg in root_words_reg:
			same_words.append (other_words[i])
		else:
			continue	
	return same_words
	
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('лес', 'Лесной', 'ЛесНичиЙ', 'перелесок', 'сорока')
result4 = single_root_words('кортеж', 'корт', 'кортик', 'алфавит')
print (result1)
print (result2)
print (result3)
print (result4)