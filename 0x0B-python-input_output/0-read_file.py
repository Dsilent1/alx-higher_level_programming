#!/usr/bin/python3

def read_file(filename=""):
    """
        read_file reads teaxt file and prints to stdout
    """
    with open(filename, "r", encoding='utf-8') as a_file:
        print("{}".format(a_file.read()), end="")
