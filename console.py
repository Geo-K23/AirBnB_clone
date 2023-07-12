#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Airbnb Command Interpreter"""
    prompt = "(hbnb)"

    def emptyline(self):
        """Do nothing """
        pass
    def do_quit(self, line):
        """ Quits program """
        return True
    def do_EOF(self, line):
        """ Returning true quits program """
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
