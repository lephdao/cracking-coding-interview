import heapq

def sort_list(almost_sorted_list, m):
    min_heap, result = [], []
    for elem in almost_sorted_list[:m]:
        heapq.heappush(min_heap, elem)

    for elem in almost_sorted_list[m:]:
        heapq.heappush(min_heap, elem)
        result.append(heapq.heappop(min_heap))

    for i in range(len(min_heap)):
        result.append(heapq.heappop(min_heap))

    return result

l1 = [3, 2, 1, 4, 6, 5]
print(l1)
print(sort_list(l1, 3))
l2 = [6, 5, 3, 2, 8, 10, 9]
print(l2)
print(sort_list(l2, 3))
l3 = [10, 9, 8, 7, 4, 70, 60, 50]
print(l3)
print(sort_list(l3, 4))