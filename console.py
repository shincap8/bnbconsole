#!/usr/bin/python3
"""Program that contains the entry point of the command interpreter:"""
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
    """check for the arg to print if something is missing"""
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
    """Class HBNBCommand"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id\n"""
        if len(arg) <= 0:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        class name and id\n"""
        if check_arg(arg) is False:
            my_list = arg.split(" ")
            key = my_list[0] + "." + my_list[1]
            allobjs = storage.all()
            try:
                print(allobjs[key])
            except Exception:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the
        change into the JSON file).\n"""
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
        """Prints all string representation of all instances based
        or not on the class name.\n"""
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
        """Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file).\n"""
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
