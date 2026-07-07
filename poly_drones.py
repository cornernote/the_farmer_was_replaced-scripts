import poly_basic
import targets
import drones

def farm():
	clear()
	tasks = []
	for center in get_poly_positions():
		tasks.append({'method': drone_farm, 'param': center})
	drones.process_tasks(tasks)

def drone_farm(pos):
	world = poly_basic.get_world(get_world_size(), Entities.Grass)
	while targets.want(Items.Hay) or targets.want(Items.Wood) or targets.want(Items.Carrot):
		poly_basic.farm_poly(pos, world)

def get_poly_positions():
	worldSize = get_world_size()
	maxDrones = max_drones()
	step = 4
	bandHeight = step * 2

	centers = []
	baseY = 0

	while baseY < worldSize and len(centers) < maxDrones:
		x = 0
		slot = 0

		while x < worldSize and len(centers) < maxDrones:
			y = baseY
			if slot % 2 == 1:
				y = baseY + step

			if y < worldSize:
				centers.append([x, y])

			x = x + step
			slot = slot + 1

		baseY = baseY + bandHeight

	return centers

if __name__ == '__main__':
	farm()