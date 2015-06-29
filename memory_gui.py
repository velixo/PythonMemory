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

		for i in range(self.rows):
			for j in range(self.columns):
				val = self.memory.get_val_at(i, j)
				grid_btn = tkinter.Button(
					# self.btn_grid,
					self.content,
					text=str(val),
					width=8,
					height=3,
					command=lambda i=i, j=j, val=val: btn_callback(i, j, val)
				)
				grid_btn.grid(row=i, column=j, sticky="NSWE")

		self.content.grid(row=0, column=0)
		self.root.mainloop()
