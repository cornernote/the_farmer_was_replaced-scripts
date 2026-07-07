import maze_basic
import movement
import targets

def farm():
	clear()
	size, centers = get_maze_positions()
	for center in centers:
		if not spawn_drone(drone_farm, size, center):
			drone_farm(size, center)

def drone_farm(size, pos = [0, 0]):
	if not size:
		size = get_world_size()
	started = False
	while targets.want(Items.Gold):
		movement.move_to(pos)
		if not started:
			started = True
			do_a_flip()
		maze_basic.plant_maze(size)
		maze_basic.solve_maze()

def get_maze_positions():
	worldSize = get_world_size()
	maxDrones = max_drones()
	mazesPerRow = calculate_mazes_per_row(maxDrones)
	mazeSize = worldSize // mazesPerRow
	halfMazeSize = mazeSize // 2

	centers = []
	for x in range(mazesPerRow):
		for y in range(mazesPerRow):
			offset = worldSize // mazesPerRow
			centers.append([offset * x + halfMazeSize, offset * y + halfMazeSize])

	return mazeSize, centers[:maxDrones][::-1]

def calculate_mazes_per_row(maxDrones):
	mazesPerRow = 1
	for square in [4, 9, 16, 25, 36]:
		mazesPerRow = square ** 0.5
		if square >= maxDrones:
			break
	return mazesPerRow

if __name__ == '__main__':
	farm()