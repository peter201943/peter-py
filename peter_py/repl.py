# MIT License 2021 Peter James Mangelsdorf
# 
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files 
# (the "Software"), to deal in the Software without restriction, 
# including without limitation the rights to use, copy, modify, merge, 
# publish, distribute, sublicense, and/or sell copies of the Software, 
# and to permit persons to whom the Software is furnished to do so, 
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be 
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# https://opensource.org/licenses/MIT

# About
# Peter's REPL Aid
# 
# Useful Functions for using the Python REPL

# Usage
# At Python-Command-Line
# Type `from repl import *`
# Then`opt()`

# Changes
# 
# 2021-09-16
# Added `rm`;
# Cleaned up `opts`;
# Added License;
# Added Intro;
# Reordered Functions by name order
# List all used-imports as hidden

# Hidden Imports
from platform   import system as __about_system
from os         import getcwd as __getcwd
from os         import remove as __remove_file
from shutil     import rmtree as __rmtree
from datetime   import datetime as __datetime
from datetime   import timezone as __timezone

# Enable easy object prototyping
from types import SimpleNamespace
class Obj(SimpleNamespace): pass
del(SimpleNamespace)

# Change Directories
from os import chdir as cd

# Execute a generic command
from os import system as cmd

# Enable Reading from System Execution
from subprocess import PIPE, run

# Test if a Path exists
from os.path import exists as fe

# Is File or Folder
from os.path import isfile

# List Contents of Directory as a List
from os import listdir as lsl

# Rename Files
from os import rename

# Allow REPL-Level Inspection
from inspect import getsource as srcl

# Configure Settings for each OS
__clear_word = "clear"
if __about_system() == "Windows":
    __clear_word = "cls"

# Readable System Executions
# https://stackoverflow.com/questions/3503879/assign-output-of-os-system-to-a-variable-and-prevent-it-from-being-displayed-on
def scmd(command: str) -> str:
    result = run(
        command,
        stdout=PIPE,
        stderr=PIPE,
        universal_newlines=True,
        shell=True)
    return result.stdout

# Clear the Screen
def c() -> None:
    _ = cmd(__clear_word)

# Display contents of File (String)
def cats(filepath: str) -> str:
    if not fe(filepath):
        return ""
    final = ""
    with open(filepath) as file:
        for line in file.readlines():
            final = final + line
    return final

# Display contents of File (Print)
def cat(filepath: str) -> None:
    print(cats(filepath))

# String the LS
def lss(path: str = ".") -> str:
    list_names = lsl(path)
    names = ""
    for name in list_names:
        names = names + name + "\n"
    return names

# Print the LS
def ls(path: str = ".") -> None:
    print(lss(path))

# Display Options (String)
if "opts" not in globals(): opts = ""
opts += """

## Peter's REPL Aid

### Command Line
c  ( None )         Clear Screen      (None)
opt( None )         Help (This)       (Print)
timenow( None )     Time Now          (String)

### Files
cat( str )          Display File      (Print)
cd ( str )          Change Directory  (None)
cmd( str )          Execute Command   (int)
fe ( str )          File Exists       (Bool)
ls ( str )          List Directory    (Print)
pwd( None )         Current Path      (String)
rm ( str )          Delete File/Dir   (None)

### Inspection
pub( list or str )  Public Strings    (Print)
pdt( obj )          Public Obj Tree   (Print)
ipl( list )         Indent Print List (Print)
src( obj )          Print Definition  (Print)

### Special
Obj                 SimpleNamespace   (Object)
lsl ( str )         List Directory    (String)
lsl ( str )         List Directory    (List)
cats( str )         Display File      (String)
opts( None )        Help              (String)
publ( list or str ) Public Strings    (List/String)
pdtl( obj )         Public Obj Tree   (List of List)
ipls( list )        Indent Print List (String)
srcl( obj )         Print Definition  (Lines)

### Combos
pub(dir(obj))       Show Public Members
mf = open(filename) New File
mf.write('text')    Edit File
mf.close()          Close File
"""

# Display Options (Print)
def opt() -> str:
    print(opts)

# Find Current Path
def pwd() -> str:
    path = __getcwd()
    path = path.replace("\\", "/")
    return path

# Delete File or Folder
def rm(filepath: str) -> None:
    if not fe(filepath):
        print("-- Not a File --")
        return
    if isfile(filepath):
        __remove_file(filepath)
        return
    if not isfile(filepath):
        __rmtree(filepath)
        return
    print("-- Unknown Error --")
    return

# Show only Public Strings (Print)
def pub(a_list_or_str):
    if type(a_list_or_str) == list:
        for astr in a_list_or_str:
            if astr[0] != "_":
                print(astr)
        return
    if type(a_list_or_str) == str:
        if a_list_or_str[0] == "_":
            print(a_list_or_str)
        return
    print("-- unknown type --")

# Show only Public Strings (List/String)
def publ(a_list_or_str):
    if type(a_list_or_str) == list:
        pub_list = []
        for astr in a_list_or_str:
            if astr[0] != "_":
                pub_list.append(astr)
        return pub_list
    if type(a_list_or_str) == str:
        if a_list_or_str[0] == "_":
            return a_list_or_str
        return
    return "-- unknown type --"

# Public Dir Tree (List of Lists)
# How can I get the name of an object in Python?
# https://stackoverflow.com/questions/1538342/how-can-i-get-the-name-of-an-object-in-python
def pdtl(
    subject:  object  = None
) -> list:
    global ignored_types
    child_tree = []
    for child_name in publ(dir(subject)):
        child_tree.append(child_name)
        child = getattr(subject, child_name)
        if(
            not     isinstance(child, str)
            and not isinstance(child, int)
            and not isinstance(child, list)
            and not isinstance(child, type)
            and not callable(child)
        ):
            child_tree.append(
                pdtl(
                    subject     = child
                )
            )
        else:
            child_tree.append(
                [child]
            )
    return child_tree

# Public Dir Tree (Print)
def pdt(
    subject:      object  = None,
    **params
) -> None:
    ipl(
        pdtl(
            subject
        ),
        **params
    )

# Indent Print a List of Lists (String)
def ipls(
    subject:      list = [],
    indent_size:  int  = 0,
    indent_chars: str  = "  ",
    prefix_chars: str  = ""
) -> str:
    indent = indent_chars * indent_size + prefix_chars
    final = ""
    if not subject:
        final += indent + "(empty)" + "\n"
    for item in subject:
        if not isinstance(item, list):
            final += indent + str(item) + "\n"
        else:
            final += ipls(
                subject      = item,
                indent_size  = indent_size + 1,
                indent_chars = indent_chars,
                prefix_chars = prefix_chars
            )
    return final

# Indent Print a List of Lists
def ipl( *args, **params ) -> None:
    print( ipls( *args, **params ) )

# View Source of Object
def src( subject: object ) -> None:
    print( srcl( subject ) )

# Time Now Formatted My Style
def timenow() -> str:
    return str(__datetime.now(__timezone.utc)).replace(" ","T").replace("-00:00","").replace("+00:00","") + "Z"

# Time Now for File Names on Windows
def timename() -> str:
    return str(__datetime.now(__timezone.utc)).replace(" ","T").replace("-00:00","").replace("+00:00","").replace(":",".") + "Z"

# Ensure everything is working
def __test() -> None:
    # TODO Later
    pass
