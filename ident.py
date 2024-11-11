#! /usr/bin/env python3
from sys import argv, exit
from os.path import isfile
from hashlib import sha3_256 as sig
argv.pop(0)

def help(arg_error: bool = False):
    if arg_error: print("\033[91mIncorrect amount of arguments!\nExpected 2, got", str(len(argv)) + ".\x1b[0m\n")
    print("Usage: python3 ident.py [file1] [file2]")
    exit(arg_error)

if len(argv) == 0:
    help()

if len(argv) != 2:
    help(True)

file1_name = argv[0]
file2_name = argv[1]

if not isfile(file1_name):
    print("\033[91mFile", file1_name, "doesn't exist or is a directory.\x1b[0m")
    exit(1)

if not isfile(file2_name):
    print("\033[91mFile", file2_name, "doesn't exist or is a directory.\x1b[0m")
    exit(1)

try:
    with open(file1_name, "rb") as file1, open(file2_name, "rb") as file2:
        file1_hash = sig(file1.read()).hexdigest()
        file2_hash = sig(file2.read()).hexdigest()
except Exception as e:
    print("\033[91mError!\n" + str(e) + "\x1b[0m")
    exit(1)


print(file1_name + ":", file1_hash[:18] + "...")
print(file2_name + ":", file2_hash[:18] + "...")

if file1_hash == file2_hash:
    print("\033[92mIdentical.\033[0m")
else:
    print("\033[93mNot identical.\033[0m")
