def count_xmas(grid):
	rows, cols = len(grid), len(grid[0])
	total_xmas = 0

	def find_xmas(row, col):
		total = 0
		if row - 3 >= 0:#left
			if [grid[row - 3][col], grid[row - 2][col], grid[row - 1][col], grid[row][col]] == ['S', 'A', 'M', 'X']:
				total += 1
		if col - 3 >= 0:#up
			if [grid[row][col - 3], grid[row][col - 2], grid[row][col - 1], grid[row][col]] == ['S', 'A', 'M', 'X']:
				total += 1
		if col - 3 >= 0 and row - 3 >= 0:#left/up
			if [grid[row - 3][col - 3], grid[row - 2][col - 2], grid[row - 1][col - 1], grid[row][col]] == ['S', 'A', 'M', 'X']:
				total += 1
		if col - 3 >= 0 and row + 3 < rows:#right/up
			if [grid[row + 3][col - 3], grid[row + 2][col - 2], grid[row + 1][col - 1], grid[row][col]] == ['S', 'A', 'M', 'X']:
				total += 1
		if row + 3 < rows:#right
			if [grid[row + 3][col], grid[row + 2][col], grid[row + 1][col], grid[row][col]] == ['S', 'A', 'M', 'X']:
				total += 1
		if col + 3 < cols:#down
			if [grid[row][col + 3], grid[row][col + 2], grid[row][col + 1], grid[row][col]] == ['S', 'A', 'M', 'X']:
				total += 1
		if col + 3 < cols and row - 3 >= 0:#left/down
			if [grid[row - 3][col + 3], grid[row - 2][col + 2], grid[row - 1][col + 1], grid[row][col]] == ['S', 'A', 'M', 'X']:
				total += 1
		if col + 3 < cols and row + 3 < rows:#right/down
			if [grid[row + 3][col + 3], grid[row + 2][col + 2], grid[row + 1][col + 1], grid[row][col]] == ['S', 'A', 'M', 'X']:
				total += 1

		return total

	def find_X_MAS(row, col):
		n_mas = 0
		#actually only 2 diag to lookup
		both_sides = [['M', 'A', 'S'], ['S', 'A', 'M']]
		if col - 1 >= 0 and row - 1 >= 0 and col + 1 < cols and row + 1 < rows:
			if [grid[row - 1][col - 1], grid[row][col], grid[row + 1][col + 1]] in both_sides:#\
				n_mas += 1
			if [grid[row - 1][col + 1], grid[row][col], grid[row + 1][col - 1]] in both_sides:#/
				n_mas += 1
		if n_mas == 2:
			return 1
		return 0

	for row in range(rows):
		for col in range(cols):
			# if grid[row][col] == 'X': #SOLUTION PART 1
			# 	total_xmas += find_xmas(row, col)
			if grid[row][col] == 'A': #SOLUTION PART 2
				total_xmas += find_X_MAS(row, col)

	return total_xmas





with open('day4.txt', 'r') as file:
	grid = []
	for line in file:
		line = line.rstrip()
		grid.append([char for char in line])

result = count_xmas(grid)
print(result)
