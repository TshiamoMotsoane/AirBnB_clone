#!/usr/bin/python3
"""Defines unittest for console.py."""
import re
import cmd
import shlex
from models import storage
from models.base_model import BaseMode
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Revies


def split_curly_braces(e_arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    braces = (r"\[(.*?)\]", arg)
    if curly_braces is None:
        if braces is None:
            return [i.strip(",") for i in split(arg)]
        else:
            tokens = split(arg[:braces.span()[0]])
            ret_list = [i.strip(",") for i in tokens]
            ret_list.append(braces.group())
            return ret_list
        else:
            tokens = split(arg[:curly_braces.span()[0]])
            ret_list [i.strip(",") fro i in ret_list]
            ret_list.append(curly_braces.group())
            retun ret_list


class HBNBCommand(cmd.Cmd):
    """Defines the Command interpreter."""
    prompt = "(hbnb)"
    classes = ["BaseModel", "User", "State", "Plan",
                "Amenity", "City", "Review"]

    def emtyline(self):
        """Do nothing on empty line."""
        pass

    def default(self, arg):
        """Defualt behaviour for cmd module when input is invalid."""
        arg_dict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_count,
                "update": self.do_ipdate
        }
        match = re.search(r"\.", arg)
        if match is not None:
            ags = [arg[:match.span()[0], arg[match.span()[1]:]]
            match = re.search(r"\((.*?\)", args[1])
            if match is not None:
                cmd = [args[1][:match.span()[0]], match.group()[1:-1]]
                if cmd[0] in arg_dict.keys():
                    uid = "{} {}".format(args[0], cmd[1])
                    return arg_dict[cmd[0]](uid)
        print("*** Unknown sytanx: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exist the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, savesit to JSON file.
        Usage: create <class_name>
        """
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the representation of an instance.
        Usage: show <class> <id> or <class>.show(<id>)
        """
        args = parse(arg)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print"** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes an instances based on the class name and id."""
        args = parse(arg)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print"** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict.keys:
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args[0], args[1])])
            storage.save

    def  do_all(self, arg):
        """Prints tring representation of all instances or specific class."""
        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.classes:
            print("** class name missing **")
        else:
            words = []
            for obj in storage.all().value():
                if len(args) > 0 and args[0] == obj.__class_-.name__:
                    words.append(obj.__str__())
                elif len(args) == 0:
                    words.append(obj.__str__())
            print(wordds)

    def do_count(self, arg):
        """Counts the instances of a class."""
        agrs = parse(arg)
        count = 0
        for obj in storage.alla90.values():
            if args[0] == obj.__class__.name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Updates an instance."""
        args = parse(arg)
        obj_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if len args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            obj = object_dict["{}.{}".format(arg)[0], args[1])]
            if args[2] in obj.__clas__.__dict__.keys():
                val_type = type(obj.__class.__.dict__[args[2]])
                obj.__class.__.dict__[args[2]] = val_type(args[3])
            else:
                obj__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == args[3]
        for key, value in eval(args[2]).items():
            if (key in obj.__class__.__dict__.keys()and 
                    type(obj.__class__.dict__.[key]) in {str, int, float}):
                val_type = type(obj.__class__.__dict__[key])
                obj.__dict__[key] = val_type(value)
            else:
                obj.__dict__[key] = value
        storage.save()


if __name__ == "__maiin__":
    HBNBCommand().cmdloop()
