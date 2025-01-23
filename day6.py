#one step or 90 degrees right if obs in front
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def find_start(grid, rows, cols):
	for row in range(rows):
		for col in range(cols):
			if grid[row][col] == '^':
				return row, col
	return 0, 0

def fill_path(r, c, current_direction, rows, cols):
	path = set()
	while 1:
		if r + directions[current_direction][0] < 0 or r + directions[current_direction][0] >= rows or c + directions[current_direction][1] < 0 or c + directions[current_direction][1] >= cols:
			path.add((r, c))
			break
		if grid[r + directions[current_direction][0]][c + directions[current_direction][1]] == '#':
			current_direction = (current_direction + 1) % 4
		path.add((r, c))
		r = r + directions[current_direction][0]
		c = c + directions[current_direction][1]
	return path


def resolve_part2(grid):
	rows, cols = len(grid), len(grid[0])
	start_row, start_col = find_start(grid, rows, cols)
	path = fill_path(start_row, start_col, 0, rows, cols)
	obs = 0

	def test_loop(ini_r, ini_c):	
		grid[ini_r][ini_c] = '#'
		visited = set()
		di = 0
		r = start_row
		c = start_col
		while 1:
			if (r, c, di) in visited:
				grid[ini_r][ini_c] = '.'
				return True
			visited.add((r, c, di))

			next_r = r + directions[di][0]
			next_c = c + directions[di][1]

			if not (0 <= next_r < rows and 0 <=  next_c < cols):
				grid[ini_r][ini_c] = '.'
				return False
			if grid[next_r][next_c] == '#':
				di = (di + 1) % 4
			else:
				r = next_r
				c = next_c				

	for r, c in path:
		#print(r, c)
		obs += test_loop(r, c)

	return obs


def	resolve_day6(grid):
	rows, cols = len(grid), len(grid[0])
	start_row, start_col = find_start(grid, rows, cols)
	visited = set()
	current_direction = 0

	def travel(r, c, current_direction):
		while 1:
			if r + directions[current_direction][0] < 0 or r + directions[current_direction][0] >= rows or c + directions[current_direction][1] < 0 or c + directions[current_direction][1] >= cols:
				visited.add((r, c))
				break
			if grid[r + directions[current_direction][0]][c + directions[current_direction][1]] == '#':
				current_direction = (current_direction + 1) % 4
			visited.add((r, c))
			r = r + directions[current_direction][0]
			c = c + directions[current_direction][1]

	travel(start_row, start_col, current_direction)
	return len(visited)


with open('day6.txt', 'r') as file:
	grid = []

	for line in file:
		line = line.rstrip()
		grid.append([char for char in line])


result = resolve_day6(grid)
print (f"result part 1: {result}")
result2 = resolve_part2(grid)

print (f"result part 2: {result2}")


