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

def traverse_tree(rootdir):
    """Traverse a Directory Tree
    See also:
    * https://docs.python.org/3/library/os.html
    * https://www.pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
    """
    print('DEBUG: traverse_tree(rootDir=%s)' % rootdir)
    for dirpath, dirnames, filenames in os.walk(rootdir):
        print('DEBUG: Found directory: %s' % dirpath)
        for fname in filenames:
            print('\t%s' % fname)

def main():
    # traverse_tree('.')
    traverse_tree(flexelint_outdir)

# ---------------------------------

if __name__ == '__main__':
    main()

# EOF
