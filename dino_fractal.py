import targets

APPLE = None
DONE = False
BODY = []
START = (0, 15)
DIRECTIONS = "ESWSSENESENNWNEESENEESWSESWWNWSSSENEESWSESWWNWSWWNENNWSWNWSSESWSSENEESWSESWWNWSSESWSSENESENNWNEEESWSSENESENNWNENNWSWWNENWNEESENESENEESWSESWWNWSSESWSSENESENNWNEEESWSSENESENNWNENNWSWWNENWNEESENNWNENNWSWNWSSESWWNWSWWNENWNEESENNNWSWWNENWNEESENEESWSSENESENNWNEEESWSSENESENNWNEESENEESWSESWWNWSSSENEESWSESWWNWSWWNENNWSWNWSSESWSSENEESWSESWWNWSSESWSSENESENNWNEEESWSSENESENNWNENNWSWWNENWNEESENESENEESWSESWWNWSSESWSSENESENNWNEEESWSSENESENNWNENNWSWWNENWNEESENNWNENNWSWNWSSESWWNWSWWNENWNEESENNNWSWWNENWNEESENEESWSSENESENNWNENWNENNWSWNWSSESWWNWSWWNENWNEESENNNWSWWNENWNEESENEESWSSENESENNWNENNWSWWNENWNEESENNWNENNWSWNWSSESWWWNENNWSWNWSSESWSSENEESWSESWWNWSWNWSWWNENWNEESENNWNENNWSWNWSSESWWWNENNWSWNWSSESWSSENEESWSESWWNWSSESWSSENESENNWNEESENEESWSESWWNWSSSENEESWSESWWNWSWWNENNWSWNWSSESWWWNENNWSWNWSSESWWNWSWWNENWNEESENNNWSWWNENWNEESENEESWSSENESENNWNENNWSWWNENWNEESENNWNENNWSWNWSSESWWWNENNWSWNWSSESWSSENEESWSESWWNWSWNWSWWNENWNEESENNWNENNWSWNWSSESWWWNENNWSWNWSSESWSSENEESWSESWWNWSSESWSSENESENNWNEESENEESWSESWWNWSSSENEESWSESWWNWSWWNENNWSWNWSSESWS"
ENABLE_SHORTCUTS = True
SHORTCUT_MIN_SHORT = 4
SHORTCUT_MIN_MEDIUM = 8
SHORTCUT_MIN_LONG = 16
INDEX_BY_Y = [
	[85, 86, 89, 90, 101, 102, 105, 106, 149, 150, 153, 154, 165, 166, 169, 170, 341, 342, 345, 346, 357, 358, 361, 362, 405, 406, 409, 410, 421, 422, 425, 426],
	[84, 87, 88, 91, 100, 103, 104, 107, 148, 151, 152, 155, 164, 167, 168, 171, 340, 343, 344, 347, 356, 359, 360, 363, 404, 407, 408, 411, 420, 423, 424, 427],
	[83, 82, 93, 92, 99, 98, 109, 108, 147, 146, 157, 156, 163, 162, 173, 172, 339, 338, 349, 348, 355, 354, 365, 364, 403, 402, 413, 412, 419, 418, 429, 428],
	[80, 81, 94, 95, 96, 97, 110, 111, 144, 145, 158, 159, 160, 161, 174, 175, 336, 337, 350, 351, 352, 353, 366, 367, 400, 401, 414, 415, 416, 417, 430, 431],
	[79, 76, 75, 74, 117, 116, 115, 112, 143, 140, 139, 138, 181, 180, 179, 176, 335, 332, 331, 330, 373, 372, 371, 368, 399, 396, 395, 394, 437, 436, 435, 432],
	[78, 77, 72, 73, 118, 119, 114, 113, 142, 141, 136, 137, 182, 183, 178, 177, 334, 333, 328, 329, 374, 375, 370, 369, 398, 397, 392, 393, 438, 439, 434, 433],
	[65, 66, 71, 70, 121, 120, 125, 126, 129, 130, 135, 134, 185, 184, 189, 190, 321, 322, 327, 326, 377, 376, 381, 382, 385, 386, 391, 390, 441, 440, 445, 446],
	[64, 67, 68, 69, 122, 123, 124, 127, 128, 131, 132, 133, 186, 187, 188, 191, 320, 323, 324, 325, 378, 379, 380, 383, 384, 387, 388, 389, 442, 443, 444, 447],
	[63, 62, 49, 48, 47, 44, 43, 42, 213, 212, 211, 208, 207, 206, 193, 192, 319, 318, 305, 304, 303, 300, 299, 298, 469, 468, 467, 464, 463, 462, 449, 448],
	[60, 61, 50, 51, 46, 45, 40, 41, 214, 215, 210, 209, 204, 205, 194, 195, 316, 317, 306, 307, 302, 301, 296, 297, 470, 471, 466, 465, 460, 461, 450, 451],
	[59, 56, 55, 52, 33, 34, 39, 38, 217, 216, 221, 222, 203, 200, 199, 196, 315, 312, 311, 308, 289, 290, 295, 294, 473, 472, 477, 478, 459, 456, 455, 452],
	[58, 57, 54, 53, 32, 35, 36, 37, 218, 219, 220, 223, 202, 201, 198, 197, 314, 313, 310, 309, 288, 291, 292, 293, 474, 475, 476, 479, 458, 457, 454, 453],
	[5, 6, 9, 10, 31, 28, 27, 26, 229, 228, 227, 224, 245, 246, 249, 250, 261, 262, 265, 266, 287, 284, 283, 282, 485, 484, 483, 480, 501, 502, 505, 506],
	[4, 7, 8, 11, 30, 29, 24, 25, 230, 231, 226, 225, 244, 247, 248, 251, 260, 263, 264, 267, 286, 285, 280, 281, 486, 487, 482, 481, 500, 503, 504, 507],
	[3, 2, 13, 12, 17, 18, 23, 22, 233, 232, 237, 238, 243, 242, 253, 252, 259, 258, 269, 268, 273, 274, 279, 278, 489, 488, 493, 494, 499, 498, 509, 508],
	[0, 1, 14, 15, 16, 19, 20, 21, 234, 235, 236, 239, 240, 241, 254, 255, 256, 257, 270, 271, 272, 275, 276, 277, 490, 491, 492, 495, 496, 497, 510, 511],
	[1023, 1022, 1009, 1008, 1007, 1004, 1003, 1002, 789, 788, 787, 784, 783, 782, 769, 768, 767, 766, 753, 752, 751, 748, 747, 746, 533, 532, 531, 528, 527, 526, 513, 512],
	[1020, 1021, 1010, 1011, 1006, 1005, 1000, 1001, 790, 791, 786, 785, 780, 781, 770, 771, 764, 765, 754, 755, 750, 749, 744, 745, 534, 535, 530, 529, 524, 525, 514, 515],
	[1019, 1016, 1015, 1012, 993, 994, 999, 998, 793, 792, 797, 798, 779, 776, 775, 772, 763, 760, 759, 756, 737, 738, 743, 742, 537, 536, 541, 542, 523, 520, 519, 516],
	[1018, 1017, 1014, 1013, 992, 995, 996, 997, 794, 795, 796, 799, 778, 777, 774, 773, 762, 761, 758, 757, 736, 739, 740, 741, 538, 539, 540, 543, 522, 521, 518, 517],
	[965, 966, 969, 970, 991, 988, 987, 986, 805, 804, 803, 800, 821, 822, 825, 826, 709, 710, 713, 714, 735, 732, 731, 730, 549, 548, 547, 544, 565, 566, 569, 570],
	[964, 967, 968, 971, 990, 989, 984, 985, 806, 807, 802, 801, 820, 823, 824, 827, 708, 711, 712, 715, 734, 733, 728, 729, 550, 551, 546, 545, 564, 567, 568, 571],
	[963, 962, 973, 972, 977, 978, 983, 982, 809, 808, 813, 814, 819, 818, 829, 828, 707, 706, 717, 716, 721, 722, 727, 726, 553, 552, 557, 558, 563, 562, 573, 572],
	[960, 961, 974, 975, 976, 979, 980, 981, 810, 811, 812, 815, 816, 817, 830, 831, 704, 705, 718, 719, 720, 723, 724, 725, 554, 555, 556, 559, 560, 561, 574, 575],
	[959, 956, 955, 954, 901, 900, 899, 896, 895, 892, 891, 890, 837, 836, 835, 832, 703, 700, 699, 698, 645, 644, 643, 640, 639, 636, 635, 634, 581, 580, 579, 576],
	[958, 957, 952, 953, 902, 903, 898, 897, 894, 893, 888, 889, 838, 839, 834, 833, 702, 701, 696, 697, 646, 647, 642, 641, 638, 637, 632, 633, 582, 583, 578, 577],
	[945, 946, 951, 950, 905, 904, 909, 910, 881, 882, 887, 886, 841, 840, 845, 846, 689, 690, 695, 694, 649, 648, 653, 654, 625, 626, 631, 630, 585, 584, 589, 590],
	[944, 947, 948, 949, 906, 907, 908, 911, 880, 883, 884, 885, 842, 843, 844, 847, 688, 691, 692, 693, 650, 651, 652, 655, 624, 627, 628, 629, 586, 587, 588, 591],
	[943, 942, 929, 928, 927, 926, 913, 912, 879, 878, 865, 864, 863, 862, 849, 848, 687, 686, 673, 672, 671, 670, 657, 656, 623, 622, 609, 608, 607, 606, 593, 592],
	[940, 941, 930, 931, 924, 925, 914, 915, 876, 877, 866, 867, 860, 861, 850, 851, 684, 685, 674, 675, 668, 669, 658, 659, 620, 621, 610, 611, 604, 605, 594, 595],
	[939, 936, 935, 932, 923, 920, 919, 916, 875, 872, 871, 868, 859, 856, 855, 852, 683, 680, 679, 676, 667, 664, 663, 660, 619, 616, 615, 612, 603, 600, 599, 596],
	[938, 937, 934, 933, 922, 921, 918, 917, 874, 873, 870, 869, 858, 857, 854, 853, 682, 681, 678, 677, 666, 665, 662, 661, 618, 617, 614, 613, 602, 601, 598, 597],
]

def farm():
	clear()
	while continue_condition():
		if not run_once():
			break

def run_once():
	global APPLE
	global DONE
	global BODY

	size = get_world_size()
	if size != 32:
		quick_print("dino_fractal needs 32x32")
		return False

	clear()
	move_to_start(START)
	change_hat(Hats.Dinosaur_Hat)

	BODY = [START]
	APPLE = measure()
	DONE = False
	if check_apple():
		BODY.append(START)

	index = 0
	while APPLE and not DONE:
		shortcut_index = None
		if ENABLE_SHORTCUTS:
			shortcut_index = try_shortcut(index)
		if shortcut_index != None:
			index = shortcut_index
		else:
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

def try_shortcut(index):
	if not APPLE:
		return None

	x = get_pos_x()
	y = get_pos_y()
	apple_x = APPLE[0]
	apple_y = APPLE[1]
	apple_index = INDEX_BY_Y[apple_y][apple_x]
	apple_distance = (apple_index - index) % len(DIRECTIONS)

	if apple_distance < shortcut_min():
		return None

	directions = shortcut_directions(x, y, apple_x, apple_y)
	for direction in directions:
		next_pos = step_pos(x, y, direction)
		if can_move(direction) and is_safe_shortcut(index, next_pos[0], next_pos[1], apple_distance):
			if not safe_move(direction):
				return None
			return INDEX_BY_Y[get_pos_y()][get_pos_x()]

	return None

def shortcut_directions(x, y, apple_x, apple_y):
	if len(BODY) < 128:
		return greedy_directions(x, y, apple_x, apple_y)

	return straight_directions(x, y, apple_x, apple_y)

def greedy_directions(x, y, apple_x, apple_y):
	x_direction = x_axis_direction(x, apple_x)
	y_direction = y_axis_direction(y, apple_y)
	x_distance = abs(apple_x - x)
	y_distance = abs(apple_y - y)
	directions = []

	if x_distance >= y_distance:
		if x_direction != None:
			directions.append(x_direction)
		if y_direction != None:
			directions.append(y_direction)
		return directions

	if y_direction != None:
		directions.append(y_direction)
	if x_direction != None:
		directions.append(x_direction)
	return directions

def straight_directions(x, y, apple_x, apple_y):
	if y == apple_y:
		direction = x_axis_direction(x, apple_x)
		if direction != None:
			return [direction]
	if x == apple_x:
		direction = y_axis_direction(y, apple_y)
		if direction != None:
			return [direction]
	return []

def x_axis_direction(x, apple_x):
	if x < apple_x:
		return East
	if x > apple_x:
		return West
	return None

def y_axis_direction(y, apple_y):
	if y < apple_y:
		return North
	if y > apple_y:
		return South
	return None

def step_pos(x, y, direction):
	next_x = x
	next_y = y
	if direction == East:
		next_x = x + 1
	elif direction == West:
		next_x = x - 1
	elif direction == North:
		next_y = y + 1
	elif direction == South:
		next_y = y - 1
	return (next_x, next_y)

def is_safe_shortcut(index, next_x, next_y, apple_distance):
	next_index = INDEX_BY_Y[next_y][next_x]
	next_distance = (next_index - index) % len(DIRECTIONS)
	if next_distance <= 0:
		return False
	if next_distance > apple_distance:
		return False

	tail = BODY[0]
	tail_index = INDEX_BY_Y[tail[1]][tail[0]]
	tail_distance = (tail_index - index) % len(DIRECTIONS)
	if tail_distance == 0:
		tail_distance = len(DIRECTIONS)
	return next_distance < tail_distance

def shortcut_min():
	body_length = len(BODY)
	if body_length < 128:
		return SHORTCUT_MIN_SHORT
	if body_length < 512:
		return SHORTCUT_MIN_MEDIUM
	return SHORTCUT_MIN_LONG

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

	ate = check_apple()
	track_body(ate)
	return True

def check_apple():
	global APPLE
	global DONE

	ate = False
	while APPLE and get_pos_x() == APPLE[0] and get_pos_y() == APPLE[1]:
		ate = True
		APPLE = measure()
		if not APPLE:
			DONE = True
			return ate
	return ate

def track_body(ate):
	BODY.append((get_pos_x(), get_pos_y()))
	if not ate:
		BODY.pop(0)

def continue_condition():
	if __name__ == '__main__':
		return True
	return targets.want(Items.Bone)

if __name__ == '__main__':
	farm()
