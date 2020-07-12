#!/usr/bin/python3
''' Define model class to another classes '''
import uuid
from datetime import datetime
import models


class BaseModel:
    ''' Base Model class '''
    def __init__(self, *args, **kwargs):
        ''' constructor funciont of BaseModel class '''
        if kwargs is not None and kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        ''' string representation of class'''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        ''' save function of base model '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' function that returns a new dictionary of class '''
        dicto = dict(self.__dict__)
        dicto['__class__'] = self.__class__.__name__
        dicto['updated_at'] = dicto['updated_at'].isoformat()
        dicto['created_at'] = dicto['created_at'].isoformat()
        return dicto
