def binary_search(lst,item):

	start_index = 0
	end_index = len(lst) - 1
	found = False

	while start_index <= end_index and not found:

		middle_index = (start_index + end_index) // 2
		guess = lst[middle_index]

		if guess == item:
			return ("Found item - index: " + str(middle_index))
		elif guess > item:
			end_index = (middle_index - 1)
		else:
			start_index = (middle_index + 1)

	return None

print(binary_search([1,2,3,5,72,84,109,120],120))
