#!/usr/bin/python3
"""Comment"""


class FileStorage:
	def __init__(self):
		__file_path = "file.json"
		objects = {}

	@property
	def objects(self):
		return self.__objects

	@objects.setter
	def objects(self, **Kwargs)
		for k, v in Kwargs.items():
			self