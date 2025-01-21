def count_xmas(grid):
	rows, cols = len(grid), len(grid[0])
	print (rows, cols)







with open('day4.txt', 'r') as file:
	grid = []
	for line in file:
		line = line.rstrip()
		grid.append([char for char in line])

count_xmas(grid)