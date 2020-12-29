# runtime for merge sort is O(nlogn)
# logn is splitting part and n is merging part 

def merge_sort(list):

	# Splitting list into smaller lists
	if (len(list)) > 1:
		mid = len(list) // 2
		left = list[:mid]
		right = list[mid:]

		print(left)
		print(right)

		merge_sort(left)
		merge_sort(right)


		# Merge 2 sorted lists
		current = 0
		p1 = 0
		p2 = 0

		while p1 < len(left) and p2 < len(right):
			if left[p1] <= right[p2]:
				list[current] = left[p1]
				p1 = p1 + 1
			else: 
				list[current] = right[p2]
				p2 = p2 + 1
			current = current + 1

		# copy the rest
		while p1 < len(left):
			list[current] = left[p1]
			current = current + 1
			p1 = p1 + 1
		while p2 < len(right):
			list[current] = right[p2]
			current = current + 1
			p2 = p2 + 1

	return list

list = [4,17,2,9,5,1,8,9,15]
print(list)
merge_sort(list)
print(list)