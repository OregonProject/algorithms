""" The rot13 algorithm takes a letter from the alphabet
and replaces it with the complimentary letter 13 places in front of it """

from string import ascii_lowercase as al

letters = {x:i for i, x in enumerate(al, 1)}

def rot13():

	user_input = str(input('What is your rot13 phrase?: '))

	phrase = list(str(user_input))
	print(phrase)
	encrypted_phrase = []

	try:
		for letter in phrase:
			if letters[letter.lower()].isalpha() and letters[letters.lower()] <= 13:
				letter_index = letters.get(letter.lower())
				letter = list(letters.keys())[list(letters.values()).index(letter_index + 13)]
				encrypted_phrase.append(letter)
			elif letters[letter.lower()].isalpha() and letters[letters.lower()] > 13:
				letter_index = letters.get(letter.lower())
				letter = list(letters.keys())[list(letters.values()).index(letter_index - 13)]
				encrypted_phrase.append(letter)
			else:
				# anything else, such as numbers or characters
				encrypted_phrase.append(letter)
	except Exception as e:
		print(e)

	print(encrypted_phrase)
	rot13 = ''.join(encrypted_phrase)
	print(rot13)

rot13()