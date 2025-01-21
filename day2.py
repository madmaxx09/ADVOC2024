def get_safe_reports(reports):
	total_safe = 0
	max_vals = [1, 2, 3]
	for rereport in reports:
		for idx in range(len(rereport)):
			report = rereport[:idx] + rereport[idx + 1:]
			#remove all reports with == levels (unsafe)
			if len(set(report)) != len(report):
				continue
			
			increasing = 2 #check if report is going up or down
			safe = 1 #will be set to 0 if unsafe
			#print(report)
			prev = report[0]
			for level in report[1:]:
				if abs(prev - level) not in max_vals:
					safe = 0
					break #because unsafe (increase or decrease > 3)
				if level - prev > 0 and increasing == 2:
					increasing = 1
				elif level - prev < 0 and increasing == 2:
					increasing = 0
				elif level - prev > 0 and increasing == 0:
					safe = 0
					break
				elif level - prev < 0 and increasing == 1:
					safe = 0
					break
				prev = level
			#print(safe)
			if safe == 1:
				total_safe += safe
				break
	return total_safe

with open('day2.txt', 'r') as file:
	reports = []
	for line in file:
		levels = [int(digit) for digit in line.split()]
		reports.append(levels)

result = get_safe_reports(reports)

print(result)
