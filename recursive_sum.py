def sum(arr):
	if not arr:
		return 0
	else:
		first = arr.pop(0)
		return first + sum(arr)

nums = list(range(1,100))
print(sum(nums))