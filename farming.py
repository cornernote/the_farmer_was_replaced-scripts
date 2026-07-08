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

def random_hat():
	# hats = []
	# for i in Hats:
		# hats.append(i)
	hats = [
		Hats.Brown_Hat,
		Hats.Cactus_Hat,
		Hats.Carrot_Hat,
		Hats.Dinosaur_Hat,
		Hats.Gold_Hat,
		Hats.Gold_Trophy_Hat,
		Hats.Golden_Cactus_Hat,
		Hats.Golden_Carrot_Hat,
		Hats.Golden_Gold_Hat,
		Hats.Golden_Pumpkin_Hat,
		Hats.Golden_Sunflower_Hat,
		Hats.Golden_Tree_Hat,
		Hats.Gray_Hat,
		Hats.Green_Hat,
		Hats.Pumpkin_Hat,
		Hats.Purple_Hat,
		Hats.Silver_Trophy_Hat,
		Hats.Straw_Hat,
		Hats.Sunflower_Hat,
		Hats.The_Farmers_Remains,
		Hats.Top_Hat,
		Hats.Traffic_Cone,
		Hats.Traffic_Cone_Stack,
		Hats.Tree_Hat,
		Hats.Wizard_Hat,
		Hats.Wood_Trophy_Hat,
	]
	change_hat(hats[random() * len(hats) // 1])
