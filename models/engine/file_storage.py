#!/usr/bin/python3
"""Comment"""


import json
import os.path as path
import models
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        new_dictionary = {}
        with open(self.__file_path, mode="w", encoding='UTF-8') as f:
            for k, v in self.__objects.items():
                new_dictionary[k] = v.to_dict()
            json.dump(new_dictionary, f, indent="\t")

    def reload(self):
        if path.isfile(self.__file_path):
            with open(self.__file_path, mode="r", encoding='UTF-8') as f:
                for k, v in (json.load(f)).items():
                    v = eval(v["__class__"])(**v)
                    self.__objects[k] = v
