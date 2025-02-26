# findtextinfiles.py

#  Looking for a specific word or phrase in a file but you forgot where it is?
#  Tis program walks through a directory looking for a matchword with files
#  that have the specified extension. Using Purepath means it should work in
#  windows just as well as Linux

#   author:Peter Suchsland
#   last edit: 7/30/2021

#   [ -d, --dir /path/to/directory/ ] Defaults to current working directory
#   [ -x, --ext .txt ] Look for the pattern in files with the extension .txt
#   Default is all files.
#   EXAMPLE:
#     $ python3 findtextinfiles.py pattern -d /home/peter/ -x .py


import argparse
import os
from pathlib import PurePath


def findTextInFile(directory, extension, matchword):
    directory = PurePath(directory)
    for root, dirs, files in os.walk(directory):
        for fname in files:
            fname = PurePath(os.path.join(root, fname))
            if ((extension is False) or (fname.suffix == extension)):
                try:
                    fh = open(fname, "r")
                    lineCnt = 0
                    for line in fh:
                        lineCnt += 1
                        if matchword in line:
                            print("\nLine: %d, File: %s\nMatch: %s" %
                                  (lineCnt, fname, line.lstrip()), end=""),
                    fh.close()

                except OSError as err:
                    fh.close()
                    print("OSError: could not open: %s:\n%s" % (fname, err))
                except IOError as err:
                    fh.close()
                    print("IOError: could not open: %s:\n%s" % (fname, err))
                except UnicodeDecodeError:
                    fh.close()


parser = argparse.ArgumentParser(description='Find string in multiple files')

parser.add_argument("match")
parser.add_argument('-x', '--ext', default="empty")
parser.add_argument('-d', '--dir', default="current")

args = vars(parser.parse_args())

if args['dir'] == 'current':
    directory = r'.'
else:
    directory = args['dir']

if args['ext'] == 'empty':
    extension = False
else:
    extension = args['ext']

matchword = args['match']

if (__name__ == "__main__"):
    findTextInFile(directory, extension, matchword)
