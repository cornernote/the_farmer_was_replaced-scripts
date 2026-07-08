import targets

APPLE = None
DONE = False
START = (0, 15)
DIRECTIONS = "ESWSSENESENNWNEESENEESWSESWWNWSSSENEESWSESWWNWSWWNENNWSWNWSSESWSSENEESWSESWWNWSSESWSSENESENNWNEEESWSSENESENNWNENNWSWWNENWNEESENESENEESWSESWWNWSSESWSSENESENNWNEEESWSSENESENNWNENNWSWWNENWNEESENNWNENNWSWNWSSESWWNWSWWNENWNEESENNNWSWWNENWNEESENEESWSSENESENNWNEEESWSSENESENNWNEESENEESWSESWWNWSSSENEESWSESWWNWSWWNENNWSWNWSSESWSSENEESWSESWWNWSSESWSSENESENNWNEEESWSSENESENNWNENNWSWWNENWNEESENESENEESWSESWWNWSSESWSSENESENNWNEEESWSSENESENNWNENNWSWWNENWNEESENNWNENNWSWNWSSESWWNWSWWNENWNEESENNNWSWWNENWNEESENEESWSSENESENNWNENWNENNWSWNWSSESWWNWSWWNENWNEESENNNWSWWNENWNEESENEESWSSENESENNWNENNWSWWNENWNEESENNWNENNWSWNWSSESWWWNENNWSWNWSSESWSSENEESWSESWWNWSWNWSWWNENWNEESENNWNENNWSWNWSSESWWWNENNWSWNWSSESWSSENEESWSESWWNWSSESWSSENESENNWNEESENEESWSESWWNWSSSENEESWSESWWNWSWWNENNWSWNWSSESWWWNENNWSWNWSSESWWNWSWWNENWNEESENNNWSWWNENWNEESENEESWSSENESENNWNENNWSWWNENWNEESENNWNENNWSWNWSSESWWWNENNWSWNWSSESWSSENEESWSESWWNWSWNWSWWNENWNEESENNWNENNWSWNWSSESWWWNENNWSWNWSSESWSSENEESWSESWWNWSSESWSSENESENNWNEESENEESWSESWWNWSSSENEESWSESWWNWSWWNENNWSWNWSSESWS"

def farm():
	clear()
	while continue_condition():
		if not run_once():
			break

def run_once():
	global APPLE
	global DONE

	size = get_world_size()
	if size != 32:
		quick_print("dino_fractal needs 32x32")
		return False

	clear()
	move_to_start(START)
	change_hat(Hats.Dinosaur_Hat)

	APPLE = measure()
	DONE = False
	check_apple()

	index = 0
	while APPLE and not DONE:
		if not move_direction(DIRECTIONS[index]):
			DONE = True
		index = (index + 1) % len(DIRECTIONS)

	change_hat(Hats.Gold_Hat)
	return True

def move_direction(command):
	if command == "E":
		return safe_move(East)
	if command == "W":
		return safe_move(West)
	if command == "N":
		return safe_move(North)
	if command == "S":
		return safe_move(South)

	quick_print("dino_fractal bad direction")
	return False

def move_to_start(pos):
	while get_pos_x() < pos[0]:
		move(East)
	while get_pos_x() > pos[0]:
		move(West)
	while get_pos_y() < pos[1]:
		move(North)
	while get_pos_y() > pos[1]:
		move(South)

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

def continue_condition():
	if __name__ == '__main__':
		return True
	return targets.want(Items.Bone)

if __name__ == '__main__':
	farm()
