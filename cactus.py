import movement
import targets
import farming
import drones

def farm():
	clear()
	while targets.want(Items.Cactus):
		world = plant_farm()
		sort_farm(world)
		harvest_sorted()

def plant_farm():
	tasks = []
	for y in range(get_world_size()):
		tasks.append({'id':y, 'method': plant_row, 'param': y})
	return drones.process_tasks(tasks, True)

def plant_row(y):
	measures = []
	for x in range(get_world_size()):
		movement.move_to([x, y])
		farming.replace_with(Entities.Cactus)
		measures.append(measure())
	return measures

def sort_farm(world):
	world = sort_rows(world)
	sort_cols(world)

def sort_rows(world):
	tasks = []
	for y in range(get_world_size()):
		tasks.append({'id': y, 'method': sort_row, 'param': {'y': y, 'world': world}})
	return drones.process_tasks(tasks, True)

def sort_row(param):
	y = param['y']
	world = param['world']
	size = get_world_size()
	low = 0
	high = size - 1

	movement.move_to([low, y])

	while low < high:
		swapped = False
		for x in range(low, high):
			if world[y][x] > world[y][x + 1]:
				swap(East)
				swap_model(world, x, y, x + 1, y)
				swapped = True
			move(East)
		if not swapped:
			break

		high -= 1
		move(West)
		swapped = False
		for x in range(high, low, -1):
			if world[y][x - 1] > world[y][x]:
				swap(West)
				swap_model(world, x, y, x - 1, y)
				swapped = True
			move(West)
		if not swapped:
			break

		low += 1
		if low < high:
			move(East)

	return world[y]

def sort_cols(world):
	tasks = []
	for x in range(get_world_size()):
		tasks.append({'id': x, 'method': sort_col, 'param': {'x': x, 'world': world}})
	return drones.process_tasks(tasks, True)

def sort_col(param):
	x = param['x']
	world = param['world']
	size = get_world_size()
	low = 0
	high = size - 1

	movement.move_to([x, low])

	while low < high:
		swapped = False
		for y in range(low, high):
			if world[y][x] > world[y + 1][x]:
				swap(North)
				swap_model(world, x, y, x, y + 1)
				swapped = True
			move(North)
		if not swapped:
			break

		high -= 1
		move(South)
		swapped = False
		for y in range(high, low, -1):
			if world[y - 1][x] > world[y][x]:
				swap(South)
				swap_model(world, x, y, x, y - 1)
				swapped = True
			move(South)
		if not swapped:
			break

		low += 1
		if low < high:
			move(North)

def swap_model(world, x1, y1, x2, y2):
	old = world[y1][x1]
	world[y1][x1] = world[y2][x2]
	world[y2][x2] = old

def harvest_sorted():
	movement.move_to([0, 0])
	while not can_harvest():
		pass
	harvest()

if __name__ == '__main__':
	farm()