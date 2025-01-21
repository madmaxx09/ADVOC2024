def get_total(text):
	total = 0

	multiples = [[] for _ in range(2)]
	do = True
	for line in text:
		state = 0
		for idx, char in enumerate(line):
			if line[idx:idx + 4] == "do()":
				do = True
			elif line[idx:idx + 7] == "don't()":
				do = False
			elif not do:
				continue
			elif char == 'm' and state == 0:
				state = 1
			elif char == 'u' and state == 1:
				state = 2
			elif char == 'l' and state == 2:
				state = 3
			elif char == '(' and state == 3:
				state = 4
			elif char.isdigit() and (state == 4 or state == 5):
				state = 5
				multiples[0].append(char)
			elif char == ',' and state == 5:
				state = 6
			elif char.isdigit() and (state == 6 or state == 7):
				state = 7
				multiples[1].append(char)
			elif char == ')' and state == 7:
				state = 0
				total += int("".join(str(digit) for digit in multiples[0])) * int("".join(str(digit) for digit in multiples[1]))
				multiples = [[] for _ in range(2)]
			else:
				state = 0
				multiples = [[] for _ in range(2)]
	return total

		

with open('day3.txt', 'r') as file:
	text = []
	for line in file:
		text.append(line)

result = get_total(text)
print(result)