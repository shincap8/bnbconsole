#!/usr/bin/python3
"""Comment """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

import json


classes = ["BaseModel", "User", "Place", "City", "State", "Amenity", "Review"]


def check_arg(arg):
    my_list = arg.split(" ")
    key = ""
    if len(arg) < 1:
        print("** class name missing **")
        return True
    elif my_list[0] not in classes:
        print("** class doesn't exist **")
        return True
    elif len(my_list) < 2:
        print("** instance id missing **")
        return True
    else:
        return False

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, arg):
        """create command to create an instance of the class given\n"""
        if len(arg) <= 0:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """show command to print the representation of the instance based on the class and id given\n"""
        if check_arg(arg) is False:
            my_list = arg.split(" ")
            key = my_list[0] + "." + my_list[1]
            allobjs = storage.all()
            try:
                print(allobjs[key])
            except Exception:
                print("** no instance found **")

    def do_destroy(self, arg):
        """destroy command to destroy the instance based on the class and id given\n"""
        if check_arg(arg) is False:
            try:
                my_list = arg.split(" ")
                key = my_list[0] + "." + my_list[1]
                allobjs = storage.all()
                del allobjs[key]
                with open("file.json", mode="w", encoding='UTF-8') as f:
                    for k, v in allobjs.items():
                        allobjs[k] = v.to_dict()
                    json.dump(allobjs, f)
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        """all command to print all objects saved if no class is passed, if class is passed
        prints all objects from that class\n"""
        allobjs = storage.all()
        objlist = []
        if len(arg) <= 0:
            for k, v in allobjs.items():
                objlist.append(str(v))
            print(objlist)
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            for k, v in allobjs.items():
                allclass = (k.split(".")[0])
                if allclass == arg:
                    objlist.append(str(v))
            print(objlist)
                
    def do_update(self, arg):
        """update command updates the object of class and id passed, with the attribute and value given\n"""
        if check_arg(arg) is False:
            my_list = arg.split(" ")
            key = my_list[0] + "." + my_list[1]
            allobjs = storage.all()
            if key in allobjs:
                if len(my_list) < 3:
                    print("** attribute name missing **")
                elif len(my_list) < 4:
                    print("** value missing **")
                else:
                    setattr(allobjs[key], my_list[2], eval(my_list[3]))
                    with open("file.json", mode="w", encoding='UTF-8') as f:
                        for k, v in allobjs.items():
                            allobjs[k] = v.to_dict()
                        json.dump(allobjs, f)
                    allobjs = storage.reload()
            else:
                print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
