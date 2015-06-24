import random


class MemoryBoard:

	def __init__(self, rows: int, columns: int):
		pass

	def get_rows(self) -> int:
		pass

	def get_columns(self) -> int:
		pass

	def select_item(self, i: int, j: int) -> bool:
		pass

	def get_selected_item_coords(self) -> list:
		pass

	def generate_values(self, rows: int, columns: int) -> list:
		pass

	def generate_grid(self, rows: int, columns: int, values: list) -> list:
		pass

	def print_grid(self, show_values: bool=False):
		pass

	def get_selected_values(self) -> tuple:
		pass