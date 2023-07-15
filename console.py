#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review


def parse(line):
    curly_braces = re.search(r"\{(.*?)\}", line)
    brackets = re.search(r"\[(.*?)\]", line)
    if curly_braces is None:
        if brackets is None:
            return [k.strip(",") for k in split(line)]
        else:
            lexer = split(line[:brackets.span()[0]])
            retL = [k.strip(",") for k in lexer]
            retL.append(brackets.group())
            return retL
    else:
        lexer = split(line[:curly_braces.span()[0]])
        retL = [k.strip(",") for k in lexer]
        retL.append(curly_braces.group())
        return retL


class HBNBCommand(cmd.Cmd):
    """Airbnb clone Command Interpreter"""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "Amenity",
        "Place",
        "State",
        "City",
        "Review"
    }

    def emptyline(self):
        """Do nothing """
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """ Returning true quits the program """
        print("")
        return True

    def default(self, line):
        """The default behavior for the console when input is invalid"""
        linedict = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        match = re.search(r"\.", line)
        if match is not None:
            lineL = [line[:match.span()[0]], line[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", lineL[1])
            if match is not None:
                command = [lineL[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in linedict.keys():
                    call = "{} {}".format(lineL[0], command[1])
                    return linedict[command[0]](call)
        print("*** Unknown syntax: {}".format(line))
        return False

    def do_create(self, line):
        """
        Creates a new class instance and print its id.
        """
        lineL = parse(line)
        if len(lineL) == 0:
            print("** class name missing **")
        elif lineL[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(lineL[0])().id)
            storage.save()

    def do_show(self, line):
        """ Displays a string representation of a class instance of a given id
        Usage: show <class> <id> or <class>.show(<id>)
        """
        lineL = parse(line)
        objdict = storage.all()
        if len(lineL) == 0:
            print("** class name missing **")
        elif lineL[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(lineL) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(lineL[0], lineL[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(lineL[0], lineL[1])])

    def do_destroy(self, line):
        """Deletes a class instance of a given id.
        Usage: destroy <class> <id> or <class>.destroy(<id>)
        """
        lineL = parse(line)
        objdict = storage.all()
        if len(lineL) == 0:
            print("** class name missing **")
        elif lineL[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(lineL) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(lineL[0], lineL[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(lineL[0], lineL[1])]
            storage.save()

    def do_all(self, line):
        """ Displays all instances of a given class as string representations.
        If no class is specified, displays all instantiated objects.
        Usage: all or all <class> or <class>.all()
        """
        lineL = parse(line)
        if len(lineL) > 0 and lineL[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(lineL) > 0 and lineL[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(lineL) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, line):
        """Retrieves the number of instances of a given class
        Usage: count <class> or <class>.count()
        """
        lineL = parse(line)
        count = 0
        for obj in storage.all().values():
            if lineL[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, line):
        """ Updates a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        """
        lineL = parse(line)
        objdict = storage.all()

        if len(lineL) == 0:
            print("** class name missing **")
            return False
        if lineL[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(lineL) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(lineL[0], lineL[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(lineL) == 2:
            print("** attribute name missing **")
            return False
        if len(lineL) == 3:
            try:
                type(eval(lineL[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(lineL) == 4:
            obj = objdict["{}.{}".format(lineL[0], lineL[1])]
            if lineL[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[lineL[2]])
                obj.__dict__[lineL[2]] = valtype(lineL[3])
            else:
                obj.__dict__[lineL[2]] = lineL[3]
        elif type(eval(lineL[2])) == dict:
            obj = objdict["{}.{}".format(lineL[0], lineL[1])]
            for k, v in eval(lineL[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
