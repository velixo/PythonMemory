import tkinter
from memory_model import MemoryModel


class MemoryWindow:

	def __init__(self, memory: MemoryModel, btn_callback):
		self.memory = memory
		self.rows = memory.get_rows()
		self.columns = memory.get_columns()

		self.root = tkinter.Tk()
		self.root.title("Memory")
		self.content = tkinter.Frame(self.root)
		self.btn_grid = tkinter.Frame(
			self.content, borderwidth=5,
			width=500, height=400
		)

		for i in range(self.rows):
			for j in range(self.columns):
				val = self.memory.get_val_at(i, j)
				grid_btn = tkinter.Button(
					self.btn_grid,
					text=str(val),
					command=lambda: btn_callback(i, j, val),
				)
				grid_btn.grid(row=i, column=j, sticky="NSWE")

		self.content.grid(row=0, column=0)
		self.btn_grid.grid(row=0, column=0)
		self.root.mainloop()
