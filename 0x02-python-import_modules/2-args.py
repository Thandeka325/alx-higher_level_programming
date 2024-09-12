#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    arg_count = len(argv) -1

    if arg_count == 0:
        print("{} arguments.".format(arg_count))
    elif arg_count == 1:
        print("{} argument:".format(arg_count))
    else:
        print("{} arguments:".format(arg_count))

    for i in range( arg_count):
        print("{}: {}".format(i + 1, argv[i + 1]))
