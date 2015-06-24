from random import shuffle


class MemoryModel:

	def __init__(self, rows: int, columns: int):
		self.rows = rows
		self.columns = columns
		self.selected_coords = []
		self.values = self.generate_values(rows, columns)
		self.grid = self.generate_grid(rows, columns, self.values)

	def get_rows(self) -> int:
		return self.rows

	def get_columns(self) -> int:
		return self.columns

	def select_item(self, i: int, j: int) -> bool:
		if self.grid[i][j] is None:
			return False

		if len(self.selected_coords) < 1:
			self.selected_coords.append((i, j))
			return False

		elif len(self.selected_coords == 1):
			self.selected_coords.append((i, j))

		selected_vals = self.get_selected_values()
		match = selected_vals[0] == selected_vals[1]
		if match:
			for coord in self.selected_coords:
				i, j = *coord
				self.grid[i][j] = None

		self.selected_coords.clear()
		return match

	def get_selected_item_coords(self) -> list:
		return self.selected_coords

	def generate_values(self, rows: int, columns: int) -> list:
		if (rows * columns) % 2 != 0:
			raise ValueError('rows * columns must be an even number')
		values = []
		max_val = (int)(rows * columns / 2)
		for i in range(1, max_val + 1):
			values.append(i)
			values.append(i)
		shuffle(values)
		return values

	def generate_grid(self, rows: int, columns: int, values: list) -> list:
		grid = [None] * columns
		for i in range(columns):
			grid[i] = [None] * rows

		for i in range(rows):
			for j in range(columns):
				grid[i][j] = values[i * columns + j]
		return grid

	def grid_str_representation(self, show_values: bool=False) -> str:
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
			# added an extra space as the length of a stringifed
			# value in the grid is always at least 1
			spacing = ' ' * len(str(max(selected_vals))) + ' '

			for i in range(self.rows):
				grid_str += '['
				for j in range(self.columns):
					if self.selected_coords.contains((i, j)):
						val = self.grid[i][j]
						adjusted_space = spacing[len(str(val)):]
						grid_str += adjusted_space + str(val)
					else:
						grid_str += spacing[1:] + 'x'
					grid_str += spacing[1:] + ']\n'

		return grid_str

	def get_selected_values(self) -> tuple:
		selected_vals = []
		for coord in self.selected_coords:
			i, j = *coord
			selected_vals.append(self.grid[i][j])
		return (val for val in selected_vals)
