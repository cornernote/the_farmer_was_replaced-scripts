MILLION = 1000000
BILLION = MILLION*1000
TARGETS = {
	Items.Hay: [BILLION, 1.1*BILLION],
	Items.Wood: [BILLION, 1.1*BILLION],
	Items.Carrot: [BILLION, 1.1*BILLION],
	Items.Pumpkin: [BILLION, 1.1*BILLION],
	Items.Cactus: [BILLION, 1.1*BILLION],
	Items.Bone: [MILLION/10, MILLION],
	Items.Power: [MILLION/10, MILLION],
	Items.Gold: [50*MILLION, 100*MILLION],
}

def need(item):
	return num_items(item) < TARGETS[item][0]

def want(item):
	return num_items(item) < TARGETS[item][1]