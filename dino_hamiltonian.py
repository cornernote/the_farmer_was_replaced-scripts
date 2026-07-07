import targets

APPLE = None
DONE = False

def farm():
	while True or targets.want(Items.Bone):
		if not run_once():
			break

def run_once():
	global APPLE
	global DONE

	size = get_world_size()
	if size % 2 != 0:
		quick_print("dino_hamiltonian needs even world size")
		return False

	clear()
	change_hat(Hats.Dinosaur_Hat)
	APPLE = measure()
	DONE = False
	check_apple()

	while not DONE:
		if not move_next_on_cycle():
			DONE = True

	change_hat(Hats.Gold_Hat)
	return True

def move_next_on_cycle():
	x = get_pos_x()
	y = get_pos_y()
	size = get_world_size()

	if y % 2 == 0:
		if x < size - 1:
			return safe_move(East)
		return safe_move(North)

	if x > 0:
		return safe_move(West)
	return safe_move(North)

def safe_move(direction):
	global DONE

	if not move(direction):
		DONE = True
		return False

	check_apple()
	return True

def check_apple():
	global APPLE
	global DONE

	while APPLE and get_pos_x() == APPLE[0] and get_pos_y() == APPLE[1]:
		APPLE = measure()
		if not APPLE:
			DONE = True
			return

def path_index(x, y):
	size = get_world_size()
	if y % 2 == 0:
		return y * size + x
	return y * size + (size - 1 - x)

if __name__ == '__main__':
	farm()
