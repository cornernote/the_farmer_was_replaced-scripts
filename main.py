import targets
import maze_drones
import poly_drones
import sunflower
import pumpkin
import cactus
import dinosaur

JOBS = [
	{'name': 'poly_drones', 'farm': poly_drones.farm, 'items': [Items.Hay, Items.Wood, Items.Carrot]},
	{'name': 'sunflower', 'farm': sunflower.farm, 'items': [Items.Power]},
	{'name': 'pumpkin', 'farm': pumpkin.farm, 'items': [Items.Pumpkin]},
	{'name': 'cactus', 'farm': cactus.farm, 'items': [Items.Cactus]},
	{'name': 'dinosaur', 'farm': dinosaur.farm, 'items': [Items.Bone]},
	{'name': 'maze_drones', 'farm': maze_drones.farm, 'items': [Items.Gold]},
]

def select_job():
	for job in JOBS:
		for item in job['items']:
			if targets.need(item):
				return job
	return JOBS[5]

while True:
	job = select_job()
	quick_print(job['name'])
	job['farm']()
