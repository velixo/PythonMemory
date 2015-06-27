import tkinter
from memory_model import MemoryModel


class MemoryWindow:

	def __init__(self, memory: MemoryModel, btn_callback):
		self.memory = memory
		self.rows = memory.get_rows()
		self.columns = memory.get_columns()

		self.root = tkinter.Tk()
		self.root.title("Memory")

		for i in range(self.rows):
			for j in range(self.columns):
				val = self.memory.get_val_at(i, j)
				grid_btn = tkinter.Button(
					self.root, text=str(val),
					command=lambda: btn_callback(i, j, val))
				grid_btn.grid(row=i, column=j)

		self.root.mainloop()
