#!/usr/bin/python3
"""Comment"""
from models.base_model import BaseModel
from datetime import datetime, date


class Review(BaseModel):
    def __init__(self, **kwargs):
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "updated_at" or k == "created_at":
                    setattr(self, k, datetime.strptime(
                        v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k != "__class__":
                    setattr(self, k, v)
        else:
            self.place_id = ""
            self.user_id = ""
            self.text = ""
            BaseModel.__init__(self)
