def is_palindrome(word):

	backwards = []
	# Reverses the word, then grabs each letter and appends it to the list
	for letter in reversed(word):
		backwards.append(letter)

	# Turns the list of characters into a single string/word
	backwards_word = "".join(backwards)

	if backwards_word.lower() == word.lower():
		return True
	else:
		return False

# Test function
print(is_palindrome("Racecar"))
print(is_palindrome("mike"))
