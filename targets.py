MILLION = 1000000
BILLION = MILLION*1000
TARGETS = {
	Items.Hay: [BILLION, BILLION + 100*MILLION],
	Items.Wood: [10*BILLION, 11*BILLION],
	Items.Carrot: [BILLION, BILLION + 100*MILLION],
	Items.Pumpkin: [200*MILLION, 200*MILLION],
	Items.Cactus: [33554432, 33554432],
	Items.Bone: [100000, MILLION],
	Items.Power: [100000, 100000],
	Items.Gold: [50*MILLION, 100*BILLION],
}

def need(item):
	return num_items(item) < TARGETS[item][0]

def want(item):
	return num_items(item) < TARGETS[item][1]
