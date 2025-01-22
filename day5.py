#this looks very much like a graph problem
#this might also be solved with sets of tuples
import re #regex

def get_total(ordering_rule, page_to_produce):
	set_of_rules = set()
	for rule in ordering_rule:
		rule = tuple(rule)
		if rule not in set_of_rules:
			set_of_rules.add(rule)
	
	total = 0

	for page in page_to_produce:
		for idx in range(1, len(page)):
			if tuple((page[idx - 1], page[idx])) not in set_of_rules:
				break
			if idx == len(page) - 1:
				total += page[(len(page) - 1) // 2]
	return total

	

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