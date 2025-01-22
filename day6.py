#one step or 90 degrees right if obs in front
UP = [-1, 0]
RIGHT = [0, 1]
DOWN = [1, 0]
LEFT = [0, -1]


def find_start(grid, rows, cols):
	for row in range(rows):
		for col in range(cols):
			if grid[row][col] == '^':
				return row, col
	return 0, 0
	

def	resolve_day6(grid):
	rows, cols = len(grid), len(grid[0])
	start_row, start_col = find_start(grid, rows, cols)
	visited = set()
	current_direction = UP
	print(rows, cols)
	print(current_direction[0], current_direction[1])
	print(start_row, start_col)

	def travel(r, c, current_direction):#changer ça en while 1
		print(r, c)
		while 1:
			#print(grid[r][c])
			if r + current_direction[0] < 0 or r + current_direction[0] >= rows or c + current_direction[1] < 0 or c + current_direction[1] >= cols:
				print("exit")
				print(current_direction)
				visited.add((r, c))
				break
			if grid[r + current_direction[0]][c + current_direction[1]] == '#':
				if current_direction == UP:
					current_direction = RIGHT
				elif current_direction == RIGHT:
					current_direction = DOWN
				elif current_direction == DOWN:
					current_direction = LEFT
				elif current_direction == LEFT:
					current_direction = UP
			visited.add((r, c))
			r = r + current_direction[0]
			c = c + current_direction[1]

	travel(start_row, start_col, current_direction)
	return len(visited)


with open('day6.txt', 'r') as file:
	grid = []

	for line in file:
		line = line.rstrip()
		grid.append([char for char in line])

result = resolve_day6(grid)

print (result)

