MILLION = 1000000
BILLION = MILLION*1000
TARGETS = {
	Items.Hay: [BILLION, BILLION + 100*MILLION],
	Items.Wood: [10*BILLION, 11*BILLION],
	Items.Carrot: [BILLION, BILLION + 100*MILLION],
	Items.Pumpkin: [BILLION, BILLION + 100*MILLION],
	Items.Cactus: [BILLION, BILLION + 100*MILLION],
	Items.Bone: [100000, MILLION],
	Items.Power: [100000, MILLION],
	Items.Gold: [50*MILLION, 100*BILLION],
}

def need(item):
	return num_items(item) < TARGETS[item][0]

def want(item):
	return num_items(item) < TARGETS[item][1]
