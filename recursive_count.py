def count(arr):
	if not arr:
		return 0
	else:
		arr.pop(0)
		return 1 + count(arr)




