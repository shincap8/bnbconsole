#!/usr/bin/python3
"""Comment"""


import json
import os.path as path
import models


class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects
 
    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        self.models.to_dict()
        with open(self.__file_path, mode="w") as f:
            text = json.dumps(self.__objects)
            f.write(text)

    def reload(self):
        if path.isfile(self.__file_path):
            with open(self.__file_path, mode="r") as f:
                text = f.read()
                self.__objects = json.loads(text)
            
