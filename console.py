#!/usr/bin/python3
"""Comment """
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()

