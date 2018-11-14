def minus_dupes(dupe_list):
	dupe_list = set(dupe_list)
	for item in dupe_list:
		print(item, end=" ")

def minus_dupesV2(dupe_list):
	deduped_list = []

	for item in dupe_list:
		if item not in deduped_list:
			deduped_list.append(item)
	
	for item in deduped_list: 
		print(item, end=" ")

fav_toppings = ["bacon", "tomato", "bacon", "pepperoni", "pepperoni", "peppers", "onion"]
print("First way (v1): ")
minus_dupes(fav_toppings)

print("\nSecond way (v2): ")
minus_dupesV2(fav_toppings)

print("\n")
