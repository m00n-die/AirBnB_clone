#!/usr/bin/python3
"""Script that contains the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
import json
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exits the program"""
        print()
        return True

    def do_quit(self, line):
        """Exits the program"""
        return True

    def emptyline(self):
        """Does not do anything"""
        pass

    def do_create(self, line):
        """creates a new instance"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            var = storage.classes()[line]()
            var.save()
            print(var.id)

    def do_destroy(self, line):
        """deletes an instance based on class name and id
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            chars = line.split(' ')
            if chars[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(chars) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(chars[0], chars[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based on class name
        """
        if line != "":
            chars = line.split(' ')
            if chars[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                vari = [str(obj) for key, obj in storage.all().items()
                        if type(obj).__name__ == chars[0]]
                print(vari)
        else:
            list_a = [str(obj) for key, obj in storage.all().items()]
            print(list_a)

    def do_update(self, line):
        """Updates an instance
        """
        if line == "" or line is None:
            print("** class name missing **")
            return

        regex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(regex, line)
        class_name = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        val = match.group(4)
        if not match:
            print("** class name missing **")
        elif class_name not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(class_name, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not val:
                print("** value missing **")
            else:
                var = None
                if not re.search('^".*"$', val):
                    if '.' in val:
                        var = float
                    else:
                        var = int
                else:
                    val = val.replace('"', '')
                attributes = storage.attributes()[class_name]
                if attribute in attributes:
                    val = attributes[attribute](val)
                elif var:
                    try:
                        val = var(val)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, val)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
