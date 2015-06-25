import unittest
from random import randint
from memory_board import MemoryModel

rows = 2
columns = 3


class MemoryBoardTest(unittest.TestCase):

	def testCorrectInitialization(self):
		self.assertEqual(rows * columns % 2, 0)
		memory = MemoryModel(rows, columns)

		self.assertEqual(rows, memory.get_rows())
		self.assertEqual(columns, memory.get_columns())

		# Check grid is correctly filled with values
		for n in range(1, len(memory.values)):
			i = (int)(n / columns)
			j = (int)(n % columns)
			self.assertEqual(memory.grid[i][j], memory.values[n])

	def testIncorrectInitialization(self):
		incorr_rows = 3
		incorr_cols = 3
		self.assertNotEqual(incorr_rows * incorr_cols % 2, 0)
		self.assertRaises(ValueError, MemoryModel, incorr_rows, incorr_cols)

	def testSelection(self):
		memory = MemoryModel(rows, columns)

		first_val = memory.grid[0][0]
		# Get a coord with same value as the one at (0, 0)
		fval_matching_coord = None
		for i in range(rows):
			for j in range(columns):
				if (i, j) != (0, 0):  # Skip (0, 0), coord already chosen
					if memory.grid[i][j] == first_val:
						fval_matching_coord = (i, j)

		self.assertIsNotNone(fval_matching_coord)
		self.assertEqual(memory.selected_coords, [])

		first_sel_res = memory.select_item(0, 0)
		self.assertFalse(first_sel_res)
		self.assertIn((0, 0), memory.selected_coords)

		# Find coord of value other than first_val
		nonmatching_coord = (0, 0)
		while nonmatching_coord in ((0, 0), fval_matching_coord):
			i = randint(0, rows - 1)
			j = randint(0, columns - 1)
			nonmatching_coord = (i, j)

		second_sel_res = memory.select_item(*nonmatching_coord)
		self.assertFalse(second_sel_res)
		self.assertEqual(memory.selected_coords, [])

		memory.select_item(0, 0)
		third_sel_res = memory.select_item(*fval_matching_coord)
		self.assertTrue(third_sel_res)
		self.assertEqual(memory.selected_coords, [])

	def testPrintGrid(self):
		memory = MemoryModel(rows, columns)
		grid_repr = memory.grid_str_representation(True)
		grid_str = str(memory.grid)

		# Remove all commas, spaces and newlines  from both string representations of
		# the grid for easier comparison
		prep_grid_repr = '[' + grid_repr.replace(' ', '').replace('\n', '') + ']'
		prep_grid_str = grid_str.replace(' ', '').replace(',', '')

		self.assertEqual(prep_grid_repr, prep_grid_str)


def main():
	unittest.main()

if __name__ == '__main__':
	main()
