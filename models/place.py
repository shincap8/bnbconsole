#!/usr/bin/python3
"""Comment"""
from models.base_model import BaseModel
from datetime import datetime, date


class Place(BaseModel):
    def __init__(self, **kwargs):
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "updated_at" or k == "created_at":
                    setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k != "__class__":
                    setattr(self, k, v)
        else:
            self.city_id = ""
            self.user_id = ""
            self.name = ""
            self.description = ""
            self.number_rooms = 0
            self.number_bathrooms = 0
            self.max_guest = 0
            self.price_by_night = 0
            self.latitude = 0.0
            self.longitude = 0.0
            self.amenity_ids = []
            BaseModel.__init__(self)
