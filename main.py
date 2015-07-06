from memory_model import MemoryModel
from memory_gui import MemoryWindow

rows, columns = (4, 5)
memory = MemoryModel(rows, columns)
print(memory.grid_str_repr(True))
score = 0


def btn_callback(i: int, j: int, gui: MemoryWindow):
	global score
	rows = memory.get_rows()
	columns = memory.get_columns()
	val = memory.get_val_at(i, j)
	print(str((i, j)) + " -> " + str(val))

	match = memory.select_item(i, j)
	selected_coords = memory.get_selected_coords()
	matched_coords = memory.get_matched_coords()
	for n in range(rows):
		for m in range(columns):
			if (n, m) in matched_coords:
				gui.set_btn_text(n, m, 'M')
			elif (n, m) in selected_coords:
				coord_val = memory.get_val_at(n, m)
				gui.set_btn_text(n, m, str(coord_val))
			else:
				gui.set_btn_text(n, m, 'X')

	if match:
		score += 1
		print('Score is ' + str(score))


gui = MemoryWindow(memory, btn_callback)
gui.start()
