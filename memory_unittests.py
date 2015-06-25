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
		empty_tuple = ()
		first_val = memory.grid[0][0]

		# Find coord with a value that is equal to first_val
		fval_matching_coord = None
		for i in range(rows):
			for j in range(columns):
				if (i, j) != (0, 0):  # Skip (0, 0), coord already chosen
					if memory.grid[i][j] == first_val:
						fval_matching_coord = (i, j)
		self.assertIsNotNone(fval_matching_coord)

		# Find coord with a value that is NOT equal to first_val
		nonmatching_coord = (0, 0)
		while nonmatching_coord in ((0, 0), fval_matching_coord):
			i = randint(0, rows - 1)
			j = randint(0, columns - 1)
			nonmatching_coord = (i, j)
		self.assertNotEqual(nonmatching_coord, (0, 0))
		self.assertNotEqual(nonmatching_coord, fval_matching_coord)

		# Check that all selections/matchings are empty
		self.assertEqual(memory.get_selected_coords(), empty_tuple)
		self.assertEqual(memory.get_matched_coord_pairs(), empty_tuple)

		# Check that first selection returns nothing, gets added to list of selected
		# coords and adds nothing to the list of matched coord pairs
		first_sel_res = memory.select_item(0, 0)
		self.assertEqual(first_sel_res, empty_tuple)
		self.assertIn((0, 0), memory.get_selected_coords())
		self.assertEqual(memory.get_matched_coord_pairs(), empty_tuple)

		# Check that second selection, with a nonmatching coord, returns nothing,
		# clears the list of selected coords and adds nothing to the list of matched
		# coord pairs
		second_sel_res = memory.select_item(*nonmatching_coord)
		self.assertEqual(second_sel_res, empty_tuple)
		self.assertEqual(memory.get_selected_coords(), empty_tuple)
		self.assertEqual(memory.get_matched_coord_pairs(), empty_tuple)

		# Check that selecting two matching coords returns the coord pair, clears the
		# list of selected coord and adds it to the list of matched coord pairs
		memory.select_item(0, 0)
		third_sel_res = memory.select_item(*fval_matching_coord)
		expected_coords = ((0, 0), fval_matching_coord)
		self.assertEqual(third_sel_res, expected_coords)
		self.assertEqual(memory.get_selected_coords(), empty_tuple)
		self.assertEqual(memory.get_matched_coord_pairs()[0], expected_coords)

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
