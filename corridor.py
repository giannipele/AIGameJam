import random
import numpy as np

DEBUG = False


def print_direction(direction):
	if direction == Corridor_generator.SOUTH:
		return "SOUTH"
	elif direction == Corridor_generator.NORTH:
		return "NORTH"
	elif direction == Corridor_generator.WEST:
		return "WEST"
	elif direction == Corridor_generator.EAST:
		return "EAST"


class Corridor_generator:
	NORTH = 0
	EAST = 1
	SOUTH = 2
	WEST = 3
	CORRIDOR_FLOOR_CODE = 2


	

	"""
	
	"""
	def __init__(self, matrix_size, corridor_min_length, corridor_max_length):
		self.matrix_size = matrix_size
		self.corridor_min_length = corridor_min_length
		self.corridor_max_length = corridor_max_length



	def generate(self, direction):

		self.target_direction = direction


		corridor = np.zeros((self.matrix_size, self.matrix_size), dtype=np.int)
		# Define target point depending on area and min_length
		starting_point = self._get_starting_point(direction)
		# target = self.get_target(startint_point)

		x, y = starting_point

		corridor[y][x] = Corridor_generator.CORRIDOR_FLOOR_CODE
		# Length of the corridor
		corridor_length = random.randint(self.corridor_min_length, self.corridor_max_length)


		if DEBUG:
			print("Corridor length", corridor_length, "direction : ", print_direction(direction))
			print("Starting point : ", x, y)
		

		i = 1
		first = True
		finish = False
		exception_direction = False
		# Main loop
		while not finish:
			# choose direction
			last_direction = direction
			if not first:
				direction = self._choose_direction(direction)
			else:
				first = False
			direction_length = random.randint(1, corridor_length - i)

			if direction_length == 1:
				exception = True
			else:
				exception = False
			
			if DEBUG:
				print(print_direction(direction), direction_length)


			j = 0
			while j < direction_length and not finish:
				x, y = self._update_point(x, y, direction)

				corridor[y][x] = Corridor_generator.CORRIDOR_FLOOR_CODE
				if DEBUG:
					print(x, y)

				j += 1
				i += 1

				if x >= self.matrix_size - 1 or y >= self.matrix_size - 1 or x <= 0 or y <= 0 or i >= corridor_length:
					finish = True

		return corridor, (x, y), direction




	def _update_point(self, old_x, old_y, direction):
		if direction == Corridor_generator.SOUTH:
			x = old_x
			y = old_y + 1
		elif direction == Corridor_generator.NORTH:
			x = old_x
			y = old_y - 1
		elif direction == Corridor_generator.WEST:
			x = old_x - 1
			y = old_y
		elif direction == Corridor_generator.EAST:
			x = old_x + 1
			y = old_y
		return x, y

	def _choose_direction(self, direction, exception=False, last_direction=None):
		if exception:
			return last_direction

		else:
			if direction == Corridor_generator.SOUTH or direction == Corridor_generator.NORTH:
				next_direction = random.choice([Corridor_generator.EAST, Corridor_generator.WEST])
			else:
				next_direction = random.choice([Corridor_generator.SOUTH, Corridor_generator.NORTH])

		if next_direction == self._get_reverse_direction(self.target_direction):
			next_direction = self.target_direction

		return next_direction

	def _get_reverse_direction(self, direction):
		if direction == Corridor_generator.SOUTH:
			return Corridor_generator.NORTH
		if direction == Corridor_generator.EAST:
			return Corridor_generator.WEST
		if direction == Corridor_generator.WEST:
			return Corridor_generator.EAST
		if direction == Corridor_generator.NORTH:
			return Corridor_generator.SOUTH



	def _get_starting_point(self, direction):
		
		if direction == Corridor_generator.SOUTH:
			y = 0
			x = int(np.floor(self.matrix_size/2))
		if direction == Corridor_generator.EAST:
			x = 0
			y = int(np.floor(self.matrix_size/2))
		if direction == Corridor_generator.WEST:
			x = self.matrix_size - 1
			y = int(np.floor(self.matrix_size/2))
		if direction == Corridor_generator.NORTH:
			y = self.matrix_size - 1
			x = int(np.floor(self.matrix_size/2))

		return x, y




	# def get_target(self, startint_point):
	# 	# random y and random x
	# 	x = random.randint(start[0]+self.corridor_min_length, start[0]+self.corridor_max_length)



	# 	tmp = self.corridor_max_length - (x - start[0])
	# 	y = random.randint(start[1]-tmp, start[1]+tmp)

	# 	return x, y





		


