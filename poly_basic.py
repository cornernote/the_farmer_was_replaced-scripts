import movement
import targets
import farming

PLANTLIST = {
	Entities.Grass: Items.Hay,
	Entities.Carrot: Items.Carrot,
	Entities.Tree: Items.Wood,
}

def farm():
	clear()
	world = get_world(get_world_size(), Entities.Grass)
	while targets.want(Items.Hay) or targets.want(Items.Wood) or targets.want(Items.Carrot):
		farm_poly([3, 3], world)

def farm_poly(pos, world):
	entity = get_entity()
	movement.move_to(pos)
	farming.replace_with(entity)
	if (entity == Entities.Tree or entity == Entities.Carrot) and num_items(Items.Fertilizer) > 30:
		use_item(Items.Fertilizer)
	companion = get_companion()
	if companion:
		if world[companion[1][0]][companion[1][1]] != companion[0]:
			world[companion[1][0]][companion[1][1]] = companion[0]
			movement.move_to(companion[1])
			farming.replace_with(companion[0])
			movement.move_to(pos)
		farming.wait_for_harvest()

def get_world(size, element):
	grid = []
	for _x in range(size):
		row = []
		for _y in range(size):
			row.append(element)
		grid.append(row)
	return grid

def get_entity():
	for entity in PLANTLIST:
		if targets.want(PLANTLIST[entity]):
			return entity

def get_entity_old():
	if num_items(Items.Hay) < num_items(Items.Wood):
		return Entities.Grass
	if num_items(Items.Wood) < num_items(Items.Carrot):
		return Entities.Tree
	return Entities.Carrot
		

if __name__ == '__main__':
	farm()