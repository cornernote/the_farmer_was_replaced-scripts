import movement
import targets

def farm():
	while continue_condition():
		clear()
		change_hat(Hats.Dinosaur_Hat)
		pos = measure()
		while pos:
			if movement.snake_to(pos):
				pos = measure()
			else:
				if not move(North):
					if not move(East):
						if not move(South):
							if not move(West):
								break
		change_hat(Hats.Gold_Hat)

def continue_condition():
	if __name__ == '__main__':
		return True
	return targets.want(Items.Bone)

if __name__ == '__main__':
	farm()
