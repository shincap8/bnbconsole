#!/usr/bin/python3
"""Comment"""
from datetime import datetime, date
import uuid


class BaseModel:
        def __init__(self, *args, **kwargs):
                if len(kwargs) > 0:
                        for k, v in kwargs.items():
                                if k == "updated_at" or k == "created_at":
                                        setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                                elif k is not "__class__":
                                        setattr(self, k, v)
                else:
                        self.id = str(uuid.uuid4())
                        self.created_at = datetime.now()
                        self.updated_at = datetime.now()

        def save(self):
                self.updated_at = datetime.now()

        def to_dict(self):
                keys = self.__dict__
                keys['__class__'] = self.__class__.__name__
                keys["created_at"] = keys["created_at"].isoformat()
                keys["updated_at"] = keys["updated_at"].isoformat()
                return keys

        def __str__(self):
                return ("[BaseModel] (" + self.id + ") " + str(self.__dict__))
