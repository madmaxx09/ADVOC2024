from collections import Counter

def find_similarity(left_list, right_list):
	count = Counter(right_list)
	sim_score = 0
	for num in left_list:
		if num in count:
			sim_score += num * count[num]
	return sim_score

def find_total_dist(left_list, right_list):
	left_list.sort()
	right_list.sort()
	total = 0
	for idx in range(len(left_list)):
		total += abs(right_list[idx] - left_list[idx])
	
	return total

with open('day1.txt', 'r') as file:
	list1, list2, = [], []

	for line in file:
		line.strip()
		test = line.split()
		list1.append(int(test[0]))
		list2.append(int(test[1]))
	
result = find_similarity(list1, list2)
print(result)