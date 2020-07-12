#!/usr/bin/python3
''' console log '''
import json
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']


class HBNBCommand(cmd.Cmd):
    ''' class to get prompt '''
    prompt = '(hbnb) '

    def emptyline(self):
        ''' pass empty lines '''
        pass

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        ''' end cmd for press EOF '''
        return True

    def do_create(self, line):
        ''' Create an instance of specific class '''
        if line:
            try:
                new_obj = eval(line)()
                print(new_obj.id)
                new_obj.save()
            except Exception:
                print('** class doesn\'t exist **')
        else:
            print('** class name missing **')

    def do_show(self, line):
        ''' show an instance of specific class '''
        if line:
            if not line.split()[0] in classes:
                print('** class doesn\'t exist **')
                return
            if len(line.split()) != 2:
                print('** instance id missing **')
                return
            try:
                dic = storage.all()
                new_l = line.replace(' ', '.')
                print(dic[new_l])
            except Exception:
                print('** no instance found **')
        else:
            print('** class name missing **')

    def do_destroy(self, line):
        ''' destroy an instance of specific class '''
        if line:
            if not line.split()[0] in classes:
                print('** class doesn\'t exist **')
                return
            if len(line.split()) != 2:
                print('** instance id missing **')
                return
            try:
                new_l = line.replace(' ', '.')
                del storage.all()[new_l]
                storage.save()
            except Exception:
                print('** no instance found **')
        else:
            print('** class name missing **')

    def do_all(self, line):
        ''' show an instance of specific class or all instances'''
        new_d = storage.all()
        if line:
            if line in classes:
                lis = [new_d[key].__str__() for key in new_d if line ==
                       key.split('.')[0]]
                print(lis)
            else:
                print('** class doesn\'t exist **')
        else:
            lis = [new_d[key].__str__() for key in new_d]
            print(lis)

    def do_update(self, line):
        ''' update an instance of specific class '''
        if line:
            lin = line.split()
            if lin[0] in classes:
                if len(lin) < 2:
                    print('** instance id missing **')
                    return
                try:
                    new_l = lin[0] + '.' + lin[1]
                    obj = storage.all()[new_l]
                except Exception:
                    print('** no instance found **')
                    return
                if len(lin) < 3:
                    print('** attribute name missing **')
                    return
                if len(lin) < 4:
                    print('** value missing **')
                    return
                setattr(obj, str(lin[2]), str(lin[3][1:-1]))
                storage.save()
            else:
                print('** class doesn\'t exist **')
        else:
            print('** class name missing **')

    def default(self, linea):
        new_l = linea.split('.')
        id_l = new_l[1].split('(')
        new_d = storage.all()
        if new_l[0] not in classes:
            print('** class doesn\'t exist')
            return
        if new_l[1] == 'all()':
            lis = [new_d[key].__str__() for key in new_d if new_l[0] ==
                   key.split('.')[0]]
            print(lis)
        elif new_l[1] == 'count()':
            lis = [new_d[key].__str__() for key in new_d if new_l[0] ==
                   key.split('.')[0]]
            print(len(lis))
        elif id_l[0] == 'show':
            try:
                print(new_d[new_l[0] + '.' + id_l[1][1:-2]])
            except Exception:
                print('** no instance found **')
                return
        elif id_l[0] == 'destroy':
            try:
                new_l = new_l[0] + '.' + id_l[1][1:-2]
                del storage.all()[new_l]
                storage.save()
            except Exception:
                print('** no instance found **')
                return
        elif id_l[0] == 'update':
            values = id_l[1].split(', {')
            try:
                va = id_l[1].split(', ')
                new = new_l[0] + '.' + va[0][1:-1]
                obj = storage.all()[new]
            except Exception:
                print('** no instance found **')
                return
            if len(values) != 2:
                values = values[0].split(', ')
                setattr(obj, str(values[1][1:-1]), str(values[2][1:-2]))
                storage.save()
            else:
                li_values = values[1][:-2].split(', ')
                for i in li_values:
                    key = i.split(': ')[0]
                    value = i.split(': ')[1]
                    if key[0] == '"' or key[0] == '\'':
                        key = key[1:-1]
                    if value[0] == '"' or value[0] == '\'':
                        value = value[1:-1]
                    setattr(obj, str(key), str(value))
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
