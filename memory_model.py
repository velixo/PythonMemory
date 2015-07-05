from random import shuffle


class MemoryModel:

	def __init__(self, rows: int, columns: int):
		self.rows = rows
		self.columns = columns
		self.selected_coords = []
		self.values = self.__generate_values(rows, columns)
		self.grid = self.__generate_grid(rows, columns, self.values)
		self.matched_coords = []

	def get_rows(self) -> int:
		return self.rows

	def get_columns(self) -> int:
		return self.columns

	def get_val_at(self, i: int, j: int) -> int:
		return self.grid[i][j]

	def select_item(self, i: int, j: int) -> bool:

		if len(self.selected_coords) > 1:
			if self.selected_coords[0] == self.selected_coords[1]:
				self.selected_coords.clear()
				self.selected_coords.append((i, j))
				return False
			else:
				first_coord_val = self.get_val_at(*self.selected_coords[0])
				second_coord_val = self.get_val_at(*self.selected_coords[1])
				match = first_coord_val == second_coord_val
				self.selected_coords.clear()
				self.selected_coords.append((i, j))
				return match

		elif (i, j) not in self.matched_coords:
			self.selected_coords.append((i, j))

		return False

# 		if len(self.selected_coords) > 1:
#
# 			selected_vals = self.get_selected_values()
# 			match = selected_vals[0] == selected_vals[1]
# 			if match:
# 				for coord in self.selected_coords:
# 					i, j = coord
# 					self.grid[i][j] = None
#
# 				for coord in self.selected_coords:
# 					self.matched_coords.append(coord)
# 				self.selected_coords.clear()
# 				return True
# 			else:
# 				self.selected_coords.clear()
#
# 		return False

	def get_selected_coords(self) -> tuple:
		return tuple(self.selected_coords)

	def get_selected_values(self) -> tuple:
		selected_vals = []
		for coord in self.selected_coords:
			i, j = coord
			selected_vals.append(self.grid[i][j])
		return tuple(selected_vals)

	def get_matched_coords(self) -> tuple:
		return tuple(self.matched_coords)

	def __generate_values(self, rows: int, columns: int) -> tuple:
		if (rows * columns) % 2 != 0:
			raise ValueError('rows * columns must be an even number')
		values = []
		max_val = (int)(rows * columns / 2)
		for i in range(1, max_val + 1):
			values.append(i)
			values.append(i)
		shuffle(values)
		return tuple(values)

	def __generate_grid(self, rows: int, columns: int, values: list) -> list:
		grid = [None] * rows
		for i in range(rows):
			grid[i] = [None] * columns

		for i in range(rows):
			for j in range(columns):
				grid[i][j] = values[i * columns + j]
		return grid

	def grid_str_repr(self, show_values: bool=False) -> str:
		grid_str = ''
		if show_values:
			spacing = ' ' + ' ' * len(str(max(self.values)))
			for i in range(self.rows):
				grid_str += '['
				for j in range(self.columns):
					val = self.grid[i][j]
					adjusted_space = spacing[len(str(val)):]
					grid_str += adjusted_space + str(val)
				grid_str += spacing[1:] + ']\n'

		else:
			selected_vals = self.get_selected_values()
			# added an extra space, as the length of a stringifed
			# value in the grid is always at least 1
			spacing = ' '
			if len(selected_vals) > 0:
				spacing += ' ' * len(str(max(selected_vals)))

			for i in range(self.rows):
				grid_str += '['
				for j in range(self.columns):
					if (i, j) in self.selected_coords:
						val = self.grid[i][j]
						adjusted_space = spacing[len(str(val)):]
						grid_str += adjusted_space + str(val)
					else:
						grid_str += spacing[1:] + 'x'
					grid_str += spacing[1:] + ']\n'

		return grid_str
