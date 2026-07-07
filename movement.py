def move_to(pos):
	xDist, yDist = get_pos_x() - pos[0], get_pos_y() - pos[1]
	halfWorldSize = get_world_size() / 2
	while get_pos_x() != pos[0]:
		if xDist >= halfWorldSize or (-halfWorldSize <= xDist and xDist < 0):
			move(East)
		else:
			move(West)
	while get_pos_y() != pos[1]:
		if yDist >= halfWorldSize or (-halfWorldSize <= yDist and yDist < 0):
			move(North)
		else:
			move(South)

def snake_to(pos):
	while get_pos_x() != pos[0]:
		if not snake_to_x(pos):
			if not snake_to_y(pos):
				return False
	while get_pos_y() != pos[1]:
		if not snake_to_y(pos):
			if not snake_to_x(pos):
				return False
	return True

def snake_to_x(pos):
	if get_pos_x() < pos[0]:
		if not move(East):
			return False
	else:
		if not move(West):
			return False
	return True

def snake_to_y(pos):
	if get_pos_y() < pos[1]:
		if not move(North):
			return False
	else:
		if not move(South):
			return False
	return True