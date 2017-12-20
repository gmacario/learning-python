#!/usr/bin/env python3
#
# Purpose: TODO
# Recursively crawl flexelint_outdir and read all "*.out" files
# Then compute how many lines contain "Error", "Warning", "Info", "Note"
# When finished, dump the result in a JSON structure

import os

print("Hello, world!")

# FIXME: Should parse command line parameters instead
flexelint_outdir = "/home/gmacario/tmp/linux-4.4.50-min-lint"
linux_sourcedir = "/home/gmacario/minimized-tree-v4.4.50-bradocaj"

def traverse_tree(rootDir):
    """Traverse a Directory Tree
    Reference: https://www.pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
    """
    print('DEBUG: traverse_tree(rootDir=%s)' % rootDir)
    for dirName, subdirList, fileList in os.walk(rootDir):
        print('DEBUG: Found directory: %s' % dirName)
        for fname in fileList:
            print('\t%s' % fname)

def main():
    # traverse_tree('.')
    traverse_tree(flexelint_outdir)

# ---------------------------------

if __name__ == '__main__':
    main()

# EOF
