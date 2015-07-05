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

		self.root = tkinter.Tk()
		self.root.title("Memory")
		content = tkinter.Frame(self.root)

		show = tkinter.BooleanVar(self.root)
		show.set(False)
		menubar = tkinter.Menu(content)
		menubar.add_checkbutton(
			label="Show values",
			variable=show,
			command=lambda: self.show_values(show.get()))

		content = tkinter.Frame(self.root)
		for i in range(self.rows):
			for j in range(self.columns):
				grid_btn = tkinter.Button(
					content,
					text='X',
					width=8,
					height=3,
					command=lambda i=i, j=j: btn_callback(i, j, self))

				grid_btn.grid(row=i, column=j, sticky="NSWE")
				self.btns[i][j] = grid_btn

		content.grid(row=0, column=0)
		self.root.config(menu=menubar)

	def start(self):
		self.root.mainloop()

	def show_values(self, show: bool):
		print('self = ' + str(self) + '\n')  # #####
		for i in range(self.rows):
			for j in range(self.columns):
				if show:
					val = self.memory.get_val_at(i, j)
					self.btns[i][j].config(text=str(val))
				else:
					self.btns[i][j].config(text='X')

	def set_btn_text(self, i: int, j: int, txt: str):
		# print(str(i) + str(j) + txt)
		self.btns[i][j].config(text=txt)
