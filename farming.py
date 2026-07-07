def replace_with(entity):
	if get_entity_type() != entity:
		ensure_harvest()
		ensure_till(entity)
		ensure_water()
		if entity != Entities.Grass:
			plant(entity)
	else:
		ensure_water()

def ensure_harvest():
	if can_harvest() or get_entity_type() == Entities.Dead_Pumpkin:
		harvest()

def ensure_till(entity):
	if get_ground_type() != Grounds.Soil:
		if (entity == Entities.Carrot or entity == Entities.Pumpkin or entity == Entities.Sunflower or entity == Entities.Cactus):
			till()
	else:
		if get_ground_type() != Grounds.Grassland:
			if entity == Entities.Grass:
				till()

def ensure_water():
	if get_ground_type() == Grounds.Soil and get_water() < 0.5 and num_items(Items.Water) > 0:
		use_item(Items.Water)