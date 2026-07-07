# usage:
# items = measure.get_items()
# quick_print(measure.get_change(items))

ITEMLIST = {
	'Hay': Items.Hay,
	'Wood': Items.Wood,
	'Carrot': Items.Carrot,
	'Pumpkin': Items.Pumpkin,
	'Cactus': Items.Cactus,
	'Bone': Items.Bone,
	'Weird_Substance': Items.Weird_Substance,
	'Gold': Items.Gold,
	# 'Water': Items.Water,
	# 'Fertilizer': Items.Fertilizer,
	# 'Power': Items.Power,
}

def get_items():
	items = {}
	for item in ITEMLIST:
		items[item] = num_items(ITEMLIST[item])
	return items

def get_change(items):
	changes = {}
	for item in ITEMLIST:
		change = num_items(ITEMLIST[item]) - items[item]
		if change != 0:
			changes[item] = change
	return changes