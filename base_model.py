#!/usr/bin/python3
"""A script that contains a class that all other
classes will inherit from"""

import uuid
from datetime import datetime

class BaseModel:
    """a class BaseModel that defines all 
    common attributes/methods for other classes"""
    def __init__(self):
        """Initializes class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns an official string representation of the class"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)
    
    def save(self):
        """updates the public instance attribute 
        updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all 
        keys/values of __dict__ of the instance"""
        dict = self.__dict__.copy()
        dict["__class__"] = type(self).__name__
        dict["created_at"] = dict["created_at"].isoformat()
        dict["updated_at"] = dict["updated_at"].isoformat()
        return dict