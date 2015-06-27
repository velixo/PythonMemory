import memory_model
import memory_gui

rows, columns = (4, 5)
memory = memory_model.MemoryModel(rows, columns)
print(memory.grid_str_repr())


def btn_callback(i: int, j: int, val: int):
	print(str((i, j)) + " -> " + str(val))

gui = memory_gui.MemoryWindow(memory, btn_callback)
