import targets

def farm():
	clear()
	while targets.want(Items.Gold):
		if plant_maze(get_world_size()):
			solve_maze()

def maze_cost(size):
	return size * 2**(num_unlocked(Unlocks.Mazes) - 1)

def plant_maze(size):
	plant(Entities.Bush)
	return use_item(Items.Weird_Substance, maze_cost(size))

def solve_maze():
	directions = [North, East, South, West]
	direction = 0
	while get_entity_type() != Entities.Treasure:
		left = (direction - 1) % 4
		right = (direction + 1) % 4
		if move(directions[left]):
			direction = left
		elif not move(directions[direction]):
			direction = right
	harvest()

if __name__ == '__main__':
	farm()