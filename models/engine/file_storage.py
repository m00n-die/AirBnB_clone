#!/usr/bin/python3
"""Script that contains a class that serializes
instances to a JSON file and deserializes JSON file to instances"""

import json
import os


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dictionary = {key: value.to_dict() for key,
                          value in FileStorage.__objects.items()}
            json.dump(dictionary, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        path = "FileStorage.__file_path"
        if not os.path.isfile(path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            rld = json.load(f)
            FileStorage.__objects = rld
