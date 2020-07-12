#!/usr/bin/python3
''' documentation be here '''
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class FileStorage:
    ''' File storage documentation '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' return objects '''
        return self.__objects

    def new(self, obj):
        ''' add new object '''
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        ''' serialization of objects to file'''
        n_dic = {}
        for key, value in self.__objects.items():
            n_dic[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(n_dic, file)

    def reload(self):
        ''' reload files in object dictionary '''
        try:
            n_dic = {}
            with open(self.__file_path, 'r') as file:
                n_dic = json.load(file)
            for key, value in n_dic.items():
                self.__objects[key] = eval(value['__class__'])(**value)
        except Exception:
            pass
