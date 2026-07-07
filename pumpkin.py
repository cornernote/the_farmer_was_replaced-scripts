import movement
import targets
import farming
import drones

def farm():
	clear()
	while targets.want(Items.Pumpkin):
		plant_farm()
		harvest()

def plant_farm():
	tasks = []
	for y in range(get_world_size()):
		tasks.append({'method': plant_row_forever, 'param': y})
	drones.process_tasks(tasks, True)

def plant_row_forever(y):
	while targets.want(Items.Pumpkin):
		plant_row(y)
		movement.move_to([0, y])
		if get_entity_type() == Entities.Pumpkin and measure() == measure(West):
			harvest()

def plant_row(y):
	pumpkinCount = 0
	pumpkins = []
	for x in range(get_world_size()):
		pumpkins.append(None)

	while pumpkinCount < get_world_size():
		for x in range(get_world_size()):
			if pumpkins[x] != Entities.Pumpkin:
				movement.move_to([x, y])
				if get_entity_type() != Entities.Pumpkin:
					farming.replace_with(Entities.Pumpkin)
					pumpkins[x] = Entities.Dead_Pumpkin
				if get_entity_type() == Entities.Pumpkin and can_harvest():
					pumpkinCount = pumpkinCount + 1
					pumpkins[x] = Entities.Pumpkin

if __name__ == '__main__':
	farm()