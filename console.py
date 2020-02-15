#!/usr/bin/python3
"""Comment """
import cmd
from models import storage
from models.base_model import BaseModel
import json

def check_arg(arg):
    my_list = arg.split(" ")
    string = ""
    if len(arg) < 1:
        print("** class name missing **")
        return True
    elif my_list[0] != "BaseModel":
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
        if len(arg) <= 0:
            print("** class name missing **")
        if arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, arg):
        check = check_arg(arg)
        if check == False:
            my_list = arg.split(" ")
            string = my_list[0] + "." + my_list[1]
            allobjs = storage.all()
            try:
                print(allobjs[string])
            except Exception:
                print("** no instance found **")

    def do_destroy(self, arg):
        check = check_arg(arg)
        if check == False:
            try:
                my_list = arg.split(" ")
                string = my_list[0] + "." + my_list[1]
                allobjs = storage.all()
                del allobjs[string]
                with open("file.json", mode="w", encoding='UTF-8') as f:
                    text = json.dumps(allobjs)
                    f.write(allobjs)
            except Exception:
                print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
