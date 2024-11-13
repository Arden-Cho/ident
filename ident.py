#! /usr/bin/env python3
from sys import argv, exit
from os.path import isfile, isdir
from hashlib import sha3_256 as get_hash
argv.pop(0)

def colored(color: str, msg: str) -> str:
    colors = {
        "FAIL": "\033[91m",
        "OKGREEN": "\033[92m",
        "WARNING": "\033[93m"
    }
    try:
        return colors[color] + msg + "\033[0m"
    except KeyError:
        return msg

def print_help(arg_error: bool = False):
    if arg_error: print(colored("FAIL", f"Incorrect amount of arguments!\nExpected 2, got {len(argv)}."))
    print("Usage: python3 ident.py [file1] [file2]")
    exit(arg_error)

if len(argv) == 0:
    print_help()

if len(argv) != 2:
    print_help(True)

file1_name = argv[0]
file2_name = argv[1]

if not isfile(file1_name) or not isfile(file2_name):
    if not isfile(file1_name):
        if isdir(file1_name): print(colored("FAIL", f"\"{file1_name}\" is a directory."))
        else: print(colored("FAIL", f"\"{file1_name}\" does not exist."))

    if not isfile(file2_name):
        if isdir(file2_name): print(colored("FAIL", f"\"{file2_name}\" is a directory."))
        else: print(colored("FAIL", f"\"{file2_name}\" does not exist."))
    exit(1)

try:
    with open(file1_name, "rb") as file1, open(file2_name, "rb") as file2:
        file1_hash = get_hash(file1.read()).hexdigest()
        file2_hash = get_hash(file2.read()).hexdigest()
except Exception as e:
    print(colored("FAIL", f"Error while reading file.\n{str(e)}"))
    exit(1)

print(file1_name + ":", file1_hash[:18] + "...")
print(file2_name + ":", file2_hash[:18] + "...")

if file1_hash == file2_hash:
    print(colored("OKGREEN", "Identical."))
else:
    print(colored("WARNING", "Not identical."))
