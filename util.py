#!/bin/python

class Matrix:

	def __init__(self, rows, columns):
		self.items = [None] * (rows * columns)
		self.rows = rows
		self.columns = columns

	#i is which row, j is which column
	def get(self, i, j):
		return self.items[i * self.rows + j]

	#i is which row, j is which column
	def set(self, value, i, j):
		self.items[i * self.rows + j] = value