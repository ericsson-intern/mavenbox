import shutil as fs
import os

def search_files(directory='.', extension='', callback=()):
    extension = extension.lower()
    for dirpath, dirnames, files in os.walk(directory):
        for name in files:
            if extension and name.lower().endswith(extension):
                callback(dirpath, name)
            elif not extension:
                print(os.path.join(dirpath, name))



def p(a,b):
    print(a,b)
search_files('pom','xml',p)



def main(*args):
    syntax = """Syntax: %s [%s] [command arguments]""" % (
        os.path.basename(args[0]), "|".join(commands.keys()))
    len(args) < 2 and usage(syntax)

    program_name, command_name = args[:2]
    arguments = args[2:]

    try:
        fun = commands[command_name]
    except KeyError:
        raise NoSuchCommandError("No such command: %s" % command_name)

    validate_arguments(fun, arguments, name=command_name)

    result = fun(*arguments)


if __name__ == "__main__":
    main(*sys.argv)