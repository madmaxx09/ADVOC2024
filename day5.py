#this looks very much like a graph problem
#this might also be solved with sets of tuples
import re #regex
from collections import defaultdict, deque


def sort_and_give(rules, page):
	my_rules = []

	for a, b in rules:
		if not (a in page and b in page):
			continue
		my_rules.append((a, b))

	indeg = defaultdict(int)
	for a, b in my_rules:
		indeg[b] += 1
	sorted_page = []
	while len(sorted_page) < len(page):
		for num in page:
			if num in sorted_page:
				continue
			if indeg[num] <= 0:
				sorted_page.append(num)
				for a, b in my_rules:
					if a == num:
						indeg[b] -= 1
	return sorted_page[(len(sorted_page) - 1) // 2]

def process_wrong(set_of_rules, wrong_pages):
	total = 0

	for page in wrong_pages:
		total += sort_and_give(set_of_rules, page)
	return total



def get_total(ordering_rule, page_to_produce):
	set_of_rules = set()
	for rule in ordering_rule:
		rule = tuple(rule)
		if rule not in set_of_rules:
			set_of_rules.add(rule)
	
	total = 0
	wrong_pages = []
	for page in page_to_produce:
		for idx in range(1, len(page)):
			if tuple((page[idx - 1], page[idx])) not in set_of_rules:
				wrong_pages.append(page)#build the list of incorrect pages for p2
				break
			if idx == len(page) - 1:
				total += page[(len(page) - 1) // 2]
	return process_wrong(set_of_rules, wrong_pages) #part2 answer
	#return total #part1 answer

#part2 if each num in the page and another in the page are in the set than it could be ordered correctly	

with open('day5.txt', 'r') as file:
	ordering_rule = []
	page_to_produce = []
	for line in file:
		line = line.rstrip()
		if re.fullmatch(r"\d{2}\|\d{2}", line):
			ordering_rule.append([int(number)for number in line.split("|")])
		elif line == '':
			continue
		else:
			page_to_produce.append([int(number) for number in line.split(",")])
	

result = get_total(ordering_rule, page_to_produce)

print(result)


# print(ordering_rule)
# print(page_to_produce)