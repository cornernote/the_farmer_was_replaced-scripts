import targets

def farm():
	clear()
	while targets.want(Items.Gold):
		plant_maze()
		solve_maze()

def plant_maze(size = get_world_size()):
	plant(Entities.Bush)
	n_substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, n_substance)

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