#!/usr/bin/env python3
#
# Purpose: TODO
# Recursively crawl flexelint_outdir and read all "*.out" files
# Then compute how many lines contain "Error", "Warning", "Info", "Note"
# When finished, dump the result in a JSON structure

import os

# print("Hello, world!")

# FIXME: Should parse command line parameters instead
flexelint_outdir = "/home/gmacario/tmp/linux-4.4.50-min-lint"
linux_sourcedir = "/home/gmacario/minimized-tree-v4.4.50-bradocaj"

def compute_statistics(report_path, module_name):
    print('DEBUG: compute_statistics(report_path=%s, module_name=%s)' % (report_path, module_name))
    # TODO
    return None

def traverse_tree(rootdir):
    """Traverse a Directory Tree
    See also:
    * https://docs.python.org/3/library/os.html
    * https://www.pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
    """
    print('DEBUG: traverse_tree(rootdir=%s)' % rootdir)
    for dirpath, dirnames, filenames in os.walk(rootdir):
        print('DEBUG: Found directory: %s' % dirpath)
        for fname in filenames:
            print('DEBUG: Found file: \t%s' % fname)
            if fname.endswith('.out'):
                report_path = dirpath + '/' + fname
                module_name = '.' + dirpath[len(rootdir):] + '/' + fname[0:len(fname)-4]
                print('TODO: compute_statistics(%s, %s)' % (report_path, module_name))
                compute_statistics(report_path, module_name)

def main():
    # traverse_tree('.')
    traverse_tree(flexelint_outdir)

# ---------------------------------

if __name__ == '__main__':
    main()

# EOF
