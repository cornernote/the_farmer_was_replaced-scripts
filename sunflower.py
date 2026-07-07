import farming
import targets
import movement
import drones

def farm():
	clear()
	while targets.want(Items.Power):
		world = plant_farm()
		harvest_farm(world)

def plant_farm():
	tasks = []
	for y in range(get_world_size()):
		tasks.append({'id': y, 'method': plant_row, 'param': y})
	return drones.process_tasks(tasks)

def plant_row(y):
	measures = []
	for x in range(get_world_size()):
		movement.move_to([x, y])
		if get_entity_type() != Entities.Sunflower:
			farming.replace_with(Entities.Sunflower)
		measures.append(measure())
	return measures

def harvest_farm(world):
	harvestList = get_harvest_list(world)
	for petalCount in harvestList:
		tasks = []
		for row in harvestList[petalCount]:
			tasks.append({'method': harvest_row, 'param': row})
		drones.process_tasks(tasks)

def harvest_row(row):
	for pos in row:
		movement.move_to(pos)
		while not can_harvest():
			pass
		harvest()

def get_harvest_list(world):
	harvestList = make_petal_buckets()
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			petalsInCell = world[y][x]
			harvestList[petalsInCell][y].append([x, y])
	return harvestList

def make_petal_buckets():
	buckets = {}
	for petals in range(15, 6, -1):
		buckets[petals] = []
		for _y in range(get_world_size()):
			buckets[petals].append([])
	return buckets

if __name__ == '__main__':
	farm()