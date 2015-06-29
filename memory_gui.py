import tkinter
from memory_model import MemoryModel


class MemoryWindow:

	def __init__(self, memory: MemoryModel, btn_callback):
		self.memory = memory
		self.rows = memory.get_rows()
		self.columns = memory.get_columns()
		self.btns = [None] * self.rows
		for i in range(self.rows):
			self.btns[i] = [None] * self.columns

		root = tkinter.Tk()
		root.title("Memory")
		content = tkinter.Frame(root)

		show = tkinter.BooleanVar(root)
		show.set(False)
		menubar = tkinter.Menu(content)
		menubar.add_checkbutton(
			label="Show values",
			variable=show,
			command=lambda: self.show_values(show.get()))

		content = tkinter.Frame(root)
		for i in range(self.rows):
			for j in range(self.columns):
				val = memory.get_val_at(i, j)
				grid_btn = tkinter.Button(
					content,
					text=str(val),
					width=8,
					height=3,
					command=lambda i=i, j=j, val=val: btn_callback(i, j, val))

				grid_btn.grid(row=i, column=j, sticky="NSWE")
				self.btns[i][j] = grid_btn

		content.grid(row=0, column=0)
		root.config(menu=menubar)
		root.mainloop()

	def show_values(self, show: bool):
		# print('show_values')
		# print('checkbtn_checked = ' + str(self.checkbtn_checked.get()))
		for i in range(self.rows):
			for j in range(self.columns):
				if show:
					val = self.memory.get_val_at(i, j)
					self.btns[i][j].config(text=str(val))
				else:
					self.btns[i][j].config(text='X')

	def show_btn_val(self, i: int, j: int, show: bool):
		if show:
			val = self.memory.get_val_at(i, j)
			self.btns[i][j].config(text=str(val))
		else:
			self.btns[i][j].config(text='X')
